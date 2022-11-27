import { getDeploymentScenario } from '@/pages/deployment-scenarios/service';
import { KEY_DATA_GRAPH } from '@/shared/constant';
import { LoadingOutlined } from '@ant-design/icons';
import { Affix, Button, Col, message, Row, Select } from 'antd';
import GGEditor, { Flow, EditableLabel } from 'gg-editor';
import React, { useEffect, useState } from 'react';
import { getAttackGraphDeploymentScenario } from '../service';
import { FlowContextMenu } from './components/EditorContextMenu';
import { FlowDetailPanel } from './components/EditorDetailPanel';
import { FlowItemPanel } from './components/EditorItemPanel';
import EditorMinimap from './components/EditorMinimap';
import { FlowToolbar } from './components/EditorToolbar';
import CustomFlow from './CustomFlow';
import styles from './index.less';
import { updateAttackGraph } from './service';
GGEditor.setTrackable(false);


const AttackGraphMonitoring = ({ deployment_scenario_id, sync, setSync }) => {

    const [loading, setLoading] = useState(false)
    const [target, setTarget] = useState('')
    const [dataGraph, setDataGraph] = useState({
        'nodes': [],
        'edges': [],
    })
    const [cves, setCVEs] = useState([])
    const [attackers, setAttackers] = useState([])

    useEffect(() => {
        const fetchData = async () => {
            setLoading(true)
            const resData = await getAttackGraphDeploymentScenario(deployment_scenario_id)
            const resDeploy = await getDeploymentScenario(deployment_scenario_id)
            if (resDeploy){
                const t = resDeploy.data.target
                setTarget(`${t.asset_id}_${t.cve_id}`)
            }
            if (resData) {
                setDataGraph(resData.attack_graph)
                setCVEs(resData.cves)
                setAttackers(resData.attackers)
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
            if (node.cve_id == targetRes.cve_id && node.asset_id == targetRes.asset_id){
                flag = true
            }
        })
        if(flag){
            const res = await updateAttackGraph(deployment_scenario_id, {
                attack_graph: graph,
                target: targetRes
            })
            if (res) {
                message.success('Save done!')
                setSync(!sync)
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
                <Col span={22}>
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
                        />
                    </Col>
                    <Col span={5} className={styles.editorSidebar}>
                        <FlowDetailPanel cves={cves} setDataGraph={setDataGraph} attackers={attackers}/>
                        {/* <EditorMinimap /> */}
                    </Col>
                </Row>
                <FlowContextMenu />
            </GGEditor>
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

export default AttackGraphMonitoring
