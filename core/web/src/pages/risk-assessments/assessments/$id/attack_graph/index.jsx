import { KEY_DATA_GRAPH } from '@/shared/constant';
import { AppstoreOutlined, LoadingOutlined } from '@ant-design/icons';
import { ModalForm } from '@ant-design/pro-form';
import { Affix, Button, Col, message, Modal, Row, Select, Table } from 'antd';
import GGEditor, { Flow, EditableLabel } from 'gg-editor';
import React, { useEffect, useState } from 'react';
import { getAttackGraphDeploymentScenario } from '../service';
import { FlowContextMenu } from './components/EditorContextMenu';
import { FlowDetailPanel } from './components/EditorDetailPanel';
import { FlowItemPanel } from './components/EditorItemPanel';
import EditorMinimap from './components/EditorMinimap';
import { FlowToolbar } from './components/EditorToolbar';
import CustomFlow from './CustomFlow';
import CustomFlowAsset from './CustomFlowAsset';
import styles from './index.less';
import { updateAttackGraph } from './service';
GGEditor.setTrackable(false);


const FlowChart = ({ deployment_scenario_id }) => {

    const [loading, setLoading] = useState(false)
    const [target, setTarget] = useState('')
    const [dataGraph, setDataGraph] = useState({
        'nodes': [],
        'edges': [],
    })
    const [cves, setCVEs] = useState([])
    const [attackers, setAttackers] = useState([])
    const [isViewAsset, setIsViewAsset] = useState(false)

    useEffect(() => {
        const fetchData = async () => {
            setLoading(true)
            const resData = await getAttackGraphDeploymentScenario(deployment_scenario_id)
            if (resData) {
                setDataGraph(resData.attack_graph)
                setCVEs(resData.cves)
                setAttackers(resData.attackers)
                let tmpA = resData.cves?.find(as => as?.cves?.length)
                let tmpVal = ''
                if (tmpA) {
                    tmpVal = `${tmpA?.asset_id}_${tmpA?.cves[0]?.cve_id}`
                } else {
                    tmpVal = 'Not found CVE'
                }
                setTarget(tmpVal)
                localStorage.setItem(KEY_DATA_GRAPH, JSON.stringify(resData.attack_graph))
            }
            setLoading(false)
        }
        fetchData()
    }, [deployment_scenario_id])

    const handleClickSave = async () => {
        const graph = JSON.parse(localStorage.getItem(KEY_DATA_GRAPH))
        setDataGraph(graph)

        const targetRes = {
            'asset_id': target.split('_')[0],
            'cve_id': target.split('_')[1],
        }
        let flag = false
        graph?.nodes?.forEach((node) => {
            if (node.cve_id == targetRes.cve_id && node.asset_id == targetRes.asset_id) {
                flag = true
            }
        })
        if (flag) {
            const res = await updateAttackGraph(deployment_scenario_id, {
                attack_graph: graph,
                target: targetRes
            })
            if (res) {
                message.success('Save done!')
            }
        } else {
            message.error('Please select target is CVE in attack graph!')
        }
    }

    const onChangeTarget = (value) => {
        setTarget(value)
    }

    if (loading)
        return <LoadingOutlined style={{ 'fontSize': 25 }} />
    return (
        <>
            <Row
                style={{
                    marginBottom: 15,
                }}
            >
                <Col span={2}>
                    Target
                </Col>
                <Col span={20}>
                    <Select
                        style={{
                            minWidth: '400',
                        }}
                        value={target}
                        onChange={onChangeTarget}
                        showSearch
                    // filterOption={(input, option) => option.children.toLowerCase().includes(input.toLowerCase())}
                    >
                        {
                            cves.map((asset) => (
                                <Select.OptGroup label={asset.asset_name} key={asset.asset_name} >
                                    {
                                        asset.cves.map(cve => (
                                            <Select.Option key={`${asset.asset_id}_${cve.cve_id}`} value={`${asset.asset_id}_${cve.cve_id}`}>
                                                {`${cve.cve_id} on ${asset.asset_name}`}
                                            </Select.Option>
                                        ))
                                    }
                                </Select.OptGroup>
                            ))
                        }
                    </Select>
                </Col>
                <Col span={2}>
                    <AppstoreOutlined style={{ fontSize: '200%' }} onClick={() => setIsViewAsset(!isViewAsset)} />
                </Col>
            </Row>
            <GGEditor className={styles.editor}>
                {/* <SaveButton setGraph={setGraph} /> */}
                <Row className={styles.editorHd}>
                    <Col span={24}>
                        <FlowToolbar />
                    </Col>
                </Row>
                <Row className={styles.editorBd}>
                    <Col span={3} className={styles.editorSidebar}>
                        <FlowItemPanel />
                    </Col>
                    <Col span={16} className={styles.editorContent}>
                        <CustomFlow
                            className={styles.flow}
                            data={dataGraph}
                            cves={cves}
                            attackers={attackers}
                        />
                    </Col>
                    <Col span={5} className={styles.editorSidebar}>
                        <FlowDetailPanel cves={cves} setDataGraph={setDataGraph} attackers={attackers} />
                        {/* <EditorMinimap /> */}
                    </Col>
                </Row>
                <FlowContextMenu />
            </GGEditor>
            <Modal
                title="Attack graph info"
                destroyOnClose={true}
                wrapClassName='modal-fullscreen'
                visible={isViewAsset}
                onOk={() => setIsViewAsset(false)}
                onCancel={() => setIsViewAsset(false)}
            >
               <Table
                    columns={[
                        {
                            title: 'Asset',
                            dataIndex: 'asset_name',
                        }
                    ]}
                    rowKey='asset_name'
                    dataSource={cves}
                    scroll={{y: 350}}
                    expandable={{
                        expandedRowRender: (row) => (
                            <Table
                                columns={[
                                    {
                                        title: 'CVE ID',
                                        dataIndex: 'cve_id',
                                    },
                                    {
                                        title: 'Attack Vector',
                                        dataIndex: 'attack_vector',
                                    },
                                    {
                                        title: 'Prerequisite',
                                        dataIndex: 'condition',
                                        render: (_) => _.preCondition,
                                    },
                                    {
                                        title: 'Postcondition',
                                        dataIndex: 'condition',
                                        render: (_) => _.postCondition,
                                    },
                                    {
                                        title: 'In Attack Graph',
                                        dataIndex: 'cve_id',
                                        render: (_) => {
                                            let nodes = JSON.parse(localStorage.getItem(KEY_DATA_GRAPH))
                                            nodes = nodes.nodes.filter(n => !n.is_attacker && n?.asset_id === row.asset_id).map(n => n.cve_id)
                                            return nodes.includes(_) ? '✅' : '❌'
                                        }
                                    },
                                ]}
                                dataSource={row.cves}
                            />
                        ),
                    }}
               />
            </Modal>

            {/* {
                isViewAsset && (
                    <GGEditor className={styles.editor}>
                        <Row className={styles.editorHd}>
                            <Col span={24}>
                                <FlowToolbar />
                            </Col>
                        </Row>
                        <Row className={styles.editorBd}>
                            <Col span={3} className={styles.editorSidebar}>
                                <FlowItemPanel />
                            </Col>
                            <Col span={16} className={styles.editorContent}>
                                <CustomFlowAsset
                                    className={styles.flow}
                                    data={() => {
                                        let d = JSON.parse(localStorage.getItem(KEY_DATA_GRAPH))
                                        let a = []
                                        d.nodes.map(node => {
                                            if (!node.is_attacker) {
                                                a.push(node.asset_id)
                                                return {
                                                    ...node,
                                                    groupId: node.asset_id
                                                }
                                            }
                                            return node
                                        })
                                        d.nodes = [...nodes, ...a.map(as => ({
                                            groupId: as,
                                            name: as,
                                            id: as,
                                        }))]
                                        return d
                                    }}
                                    cves={cves}
                                    attackers={attackers}
                                />
                            </Col>
                            <Col span={5} className={styles.editorSidebar}>
                                <FlowDetailPanel cves={cves} setDataGraph={setDataGraph} attackers={attackers} />
                            </Col>
                        </Row>
                        <FlowContextMenu />
                    </GGEditor>
                )
            } */}

            <Affix style={{ position: 'fixed', right: 50, bottom: 50, zIndex: 1000 }} >
                <Button
                    type="primary"
                    onClick={handleClickSave}
                >
                    Save
                </Button>
            </Affix>
        </>
    )
}

export default FlowChart
