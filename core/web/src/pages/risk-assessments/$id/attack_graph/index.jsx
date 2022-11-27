import { KEY_DATA_GRAPH } from '@/shared/constant';
import { Col, Input, Row } from 'antd';
import GGEditor, {  } from 'gg-editor';
import React, { useEffect, useState } from 'react';
import { FlowContextMenu } from './components/EditorContextMenu';
import { FlowDetailPanel } from './components/EditorDetailPanel';
import { FlowItemPanel } from './components/EditorItemPanel';
import { FlowToolbar } from './components/EditorToolbar';
import CustomFlow from './CustomFlow';
import styles from './index.less';
GGEditor.setTrackable(false);


const FlowChart = ({ riskAssessmentReport }) => {

    const [target, setTarget] = useState('')
    const [dataGraph, setDataGraph] = useState(riskAssessmentReport?.deployment_scenario?.attack_graph)
    const [cves, setCVEs] = useState([])
    const [attackers, setAttackers] = useState([])

    useEffect(() => {
        const fetchData = async () => {
            setDataGraph(riskAssessmentReport?.deployment_scenario?.attack_graph)
            const assets = riskAssessmentReport?.deployment_scenario?.assets
            const target = riskAssessmentReport?.deployment_scenario?.target
            const tmpCVEs = riskAssessmentReport?.deployment_scenario?.cves.map((cve) => ({
                ...cve,
                asset_name: assets?.find(as => as.id === cve.asset_id)?.name
            }))
            setCVEs(tmpCVEs)
            setAttackers(riskAssessmentReport?.deployment_scenario?.attackers)
            setTarget(`${target?.cve_id} on ${assets?.find(as => as.id === target?.asset_id)?.name}`)
            localStorage.setItem(KEY_DATA_GRAPH, JSON.stringify(riskAssessmentReport?.deployment_scenario?.attack_graph))
        }
        fetchData()
    }, [])

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
                <Col span={15}>
                    <Input
                        value={target}
                        disabled
                        style={{
                            minWidth: 400
                        }}
                    />
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
                    {/* <Col span={3} className={styles.editorSidebar}>
                        <FlowItemPanel />
                    </Col> */}
                    <Col span={19} className={styles.editorContent}>
                        <CustomFlow
                            className={styles.flow}
                            data={dataGraph}
                        />
                    </Col>
                    <Col span={5} className={styles.editorSidebar}>
                        <FlowDetailPanel cves={cves} setDataGraph={setDataGraph} attackers={attackers}/>
                    </Col>
                </Row>
                <FlowContextMenu />
            </GGEditor>
        </>
    )
}

export default FlowChart
