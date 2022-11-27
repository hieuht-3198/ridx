import { convertImpactToNumber, likelihoodToType, riskLevelToType, severityToType, toFixNumber } from '@/shared/common'
import { CRITICAL_COLOR, HIGH_COLOR, LOW_COLOR, MEDIUM_COLOR, NODE_CPT, NODE_DECISION, NODE_DECISION_TRUE, RISK_MATRIX } from '@/shared/constant'
import { Bar, Scatter, Heatmap } from '@ant-design/charts'
import { CheckCircleOutlined, CheckOutlined, CloseCircleOutlined, CloseOutlined } from '@ant-design/icons'
import ProTable from '@ant-design/pro-table'
import { Button, Collapse, Row, Col, Table, Space, message, Affix } from 'antd'
import React, { useState } from 'react'
import { useEffect } from 'react'
import { postAssessments, postStatisAssessments } from '../service'

const { Panel } = Collapse


const Assessment = ({ deployment_scenario_id, damageCriterion, benefitCriterion }) => {

    const [isAssessment, setIsAssessment] = useState(false)
    const [dataVuls, setDataVuls] = useState([])
    const [dataSystem, setDataSystem] = useState([
        {
            attribute: 'Severity',
            not_implemented: '',
            implemented: '',
        },
        {
            attribute: 'Likelihood',
            not_implemented: '',
            implemented: '',
        },
        {
            attribute: 'Risk level',
            not_implemented: '',
            implemented: '',
        },
    ])
    const [dataCountermeasures, setDataCountermeasures] = useState([])
    const [loading, setLoading] = useState(false)

    const [assetsCountermeasures, setAssetsCountermeasures] = useState([])
    const [assetsNotCountermeasures, setAssetsNotCountermeasures] = useState([])
    const [securityGoals, setSecurityGoals] = useState([])


    useEffect(() => {
        handleClickButtonStartAssessment()
    }, [])

    const handleClickButtonStartAssessment = async () => {
        try {
            setLoading(true)
            const assessmentRes = await postStatisAssessments(deployment_scenario_id, {
                'damage_criterion': parseFloat(damageCriterion),
                'benefit_criterion': parseFloat(benefitCriterion),
            })
            if (assessmentRes) {
                let tmpDataVuls = []
                let tmpDataCo = []
                assessmentRes.data.countermeasures.map((item) => {
                    if (item.type === NODE_CPT && !item.is_attacker) {
                        tmpDataVuls.push({
                            label: item.name,
                            type: 'With countermeasures',
                            value: item.outcomes.True,
                        })
                        return item
                    }
                    if (item.type === NODE_DECISION) {
                        tmpDataCo.push({
                            ...item,
                            'value': item.outcomes.True,
                        })
                    }
                    return item
                })
                assessmentRes.data.not_countermeasures.map((item) => {
                    if (item.type === NODE_CPT && !item.is_attacker) {
                        tmpDataVuls.push({
                            label: item.name,
                            type: "Without all countermeasures",
                            value: item.outcomes.True
                        })
                        return item
                    }
                })
                const tmpCoun = assessmentRes.data.cia.countermeasures.map(as => ({
                    ...as,
                    severity: toFixNumber(`${9 - (as.confidentiality + as.integrity + as.availability)}`),
                }))
                const tmpNotCoun = assessmentRes.data.cia.not_countermeasures.map(as => ({
                    ...as,
                    severity: toFixNumber(9 - (as.confidentiality + as.integrity + as.availability)),
                }))
                const s_n = severityToType(tmpNotCoun.reduce((pre, next) => pre + next.severity, 0) / tmpNotCoun.length)
                const s_i = severityToType(tmpCoun.reduce((pre, next) => pre + next.severity, 0) / tmpCoun.length)
                const l_n = likelihoodToType(assessmentRes.data.likelihood.countermeasures.outcomes[NODE_DECISION_TRUE])
                const l_i = likelihoodToType(assessmentRes.data.likelihood.not_countermeasures.outcomes[NODE_DECISION_TRUE])
                setDataSystem([
                    {
                        attribute: 'Severity',
                        not_implemented: s_n[0],
                        implemented: s_i[0],
                    },
                    {
                        attribute: 'Likelihood',
                        not_implemented: l_n[0],
                        implemented: l_i[0],
                    },
                    {
                        attribute: 'Risk level',
                        not_implemented: riskLevelToType(s_n[1], l_n[1]),
                        implemented: riskLevelToType(s_i[1], l_i[1]),
                    },
                ])
                setAssetsCountermeasures(tmpCoun)
                setAssetsNotCountermeasures(tmpNotCoun)
                setSecurityGoals(assessmentRes.data.security_goals)
                setDataVuls(tmpDataVuls)
                setDataCountermeasures(tmpDataCo.map((counter) => ({
                    Value: counter.value,
                    Name: counter.name,
                    Cost: counter.cost,
                })))
                setIsAssessment(true)
            } else {
                message.error('Please setup attack graph')
            }
            setLoading(false)
        } catch (e) {
            console.log(e);
        }
    }

    const configScatter = {
        data: dataCountermeasures,
        xField: 'Cost',
        yField: 'Value',
        colorField: 'Name',
        // color={(_) => '#000000'}
        // pointStyle={{
        //     fill: 'black',
        // }}
        tooltip: {
            fields: ['Name', 'Cost', 'Value'],
            showMarkers: false,
            showTitle: false,
        },
        yAxis: {
            nice: true,
            line: {
                style: {
                    stroke: '#aaa',
                },
            },
            title: {
                text: 'Value',
                position: 'end',
            }
        },
        xAxis: {
            title: {
                text: 'Cost',
                position: 'end',
            }
        },
        legend: {
            layout: 'vertical',
            position: 'right'
        }
    }

    const configHeadmap = {
        data: RISK_MATRIX,
        xField: 'Likelihood',
        yField: 'Severity',
        colorField: 'value',
        interactions: [{ type: 'element-active' }],
        tooltip: {
            fields: ['Risk level', 'Severity', 'Likelihood'],
            showMarkers: false,
            showTitle: false,
        },
        yAxis: {
            title: {
                text: 'Severity',
                position: 'center',
            }
        },
        xAxis: {
            title: {
                text: 'Likelihood',
                position: 'center',
            }
        },
        label: {
            style: {
                fontSize: 24,
                fontWeight: 500,
                textAlign: 'center',
                fill: 'black',
            },
        },
        color: (obj) => {
            const { value } = obj
            if (value <= 3)
                return LOW_COLOR
            if (value <= 7)
                return MEDIUM_COLOR
            if (value <= 12)
                return HIGH_COLOR
            return CRITICAL_COLOR
        }
    }

    const columnsSeruityGoals = [
        {
            title: 'Security goal name',
            dataIndex: 'name',
            key: 'name',
            width: '20%',
        },
        {
            title: 'Asset',
            dataIndex: 'asset_id',
            key: 'asset_id',
            width: '20%',
            render: (asset_id) => assetsCountermeasures.find(asset => asset.id === asset_id)?.name
        },
        {
            title: 'C - I - A',
            children: [
                {
                    title: 'With countermeasures',
                    children: [
                        {
                            title: 'C',
                            dataIndex: 'i_c',
                            key: 'i_c',
                            align: 'center',
                            render: (_, record) => {
                                let asset = assetsCountermeasures.find(as => as.id === record.asset_id)
                                const flag = asset.confidentiality >= convertImpactToNumber(record.confidentiality) - 1
                                return <b style={{ color: flag ? LOW_COLOR : CRITICAL_COLOR }}>{record.confidentiality}</b>
                            },
                        },
                        {
                            title: 'I',
                            dataIndex: 'i_i',
                            key: 'i_i',
                            align: 'center',
                            render: (_, record) => {
                                let asset = assetsCountermeasures.find(as => as.id === record.asset_id)
                                const flag = asset.integrity >= convertImpactToNumber(record.integrity) - 1
                                return <b style={{ color: flag ? LOW_COLOR : CRITICAL_COLOR }}>{record.integrity}</b>
                            },
                        },
                        {
                            title: 'A',
                            dataIndex: 'i_a',
                            key: 'i_a',
                            align: 'center',
                            render: (_, record) => {
                                let asset = assetsCountermeasures.find(as => as.id === record.asset_id)
                                const flag = asset.availability >= convertImpactToNumber(record.availability) - 1
                                return <b style={{ color: flag ? LOW_COLOR : CRITICAL_COLOR }}>{record.availability}</b>
                            },
                        },
                        {
                            title: 'Result',
                            dataIndex: 'i_r',
                            key: 'i_r',
                            align: 'center',
                            render: (_, record) => {
                                let asset = assetsCountermeasures.find(as => as.id === record.asset_id)
                                const flag = asset.confidentiality >= convertImpactToNumber(record.confidentiality) - 1 && asset.integrity >= convertImpactToNumber(record.integrity) - 1 && asset.availability >= convertImpactToNumber(record.availability) - 1
                                return flag ? <CheckOutlined style={{ color: 'green', fontSize: '150%' }} /> : <CloseOutlined style={{ color: 'red', fontSize: '150%' }} />
                            },
                        },
                    ],
                },
                {
                    title: 'Without all countermeasures',
                    children: [
                        {
                            title: 'C',
                            dataIndex: 'n_c',
                            key: 'n_c',
                            align: 'center',
                            render: (_, record) => {
                                let asset = assetsNotCountermeasures.find(as => as.id === record.asset_id)
                                const flag = asset.confidentiality >= convertImpactToNumber(record.confidentiality) - 1
                                return <b style={{ color: flag ? LOW_COLOR : CRITICAL_COLOR }}>{record.confidentiality}</b>
                            },
                        },
                        {
                            title: 'I',
                            dataIndex: 'n_i',
                            key: 'n_i',
                            align: 'center',
                            render: (_, record) => {
                                let asset = assetsNotCountermeasures.find(as => as.id === record.asset_id)
                                const flag = asset.integrity >= convertImpactToNumber(record.integrity) - 1
                                return <b style={{ color: flag ? LOW_COLOR : CRITICAL_COLOR }}>{record.integrity}</b>
                            },
                        },
                        {
                            title: 'A',
                            dataIndex: 'n_a',
                            key: 'n_a',
                            align: 'center',
                            render: (_, record) => {
                                let asset = assetsNotCountermeasures.find(as => as.id === record.asset_id)
                                const flag = asset.availability >= convertImpactToNumber(record.availability) - 1
                                return <b style={{ color: flag ? LOW_COLOR : CRITICAL_COLOR }}>{record.availability}</b>
                            },
                        },
                        {
                            title: 'Result',
                            dataIndex: 'n_r',
                            key: 'n_r',
                            align: 'center',
                            render: (_, record) => {
                                let asset = assetsNotCountermeasures.find(as => as.id === record.asset_id)
                                const flag = asset.confidentiality >= convertImpactToNumber(record.confidentiality) - 1 && asset.integrity >= convertImpactToNumber(record.integrity) - 1 && asset.availability >= convertImpactToNumber(record.availability) - 1
                                return flag ? <CheckOutlined style={{ color: 'green', fontSize: '150%' }} /> : <CloseOutlined style={{ color: 'red', fontSize: '150%' }} />
                            },
                        },
                    ],
                },
            ],
        },
    ]

    const columnAssets = [
        {
            title: 'Asset name',
            dataIndex: 'name',
            key: 'name',
            width: '60%',
        },
        {
            title: 'Severity',
            children: [
                {
                    title: 'With countermeasures',
                    key: 'implemented',
                    dataIndex: 'implemented',
                    align: 'center',
                    width: '20%',
                    render: (_, record) => assetsCountermeasures.find(as => as.id === record.id)?.severity
                },
                {
                    title: 'Without all countermeasures',
                    key: 'not_implemented',
                    dataIndex: 'not_implemented',
                    align: 'center',
                    width: '20%',
                    render: (_, record) => assetsNotCountermeasures.find(as => as.id === record.id)?.severity
                }
            ]
        }
    ]

    const columnsAll = [
        {
            title: 'Attribute',
            dataIndex: 'attribute',
            key: 'attribute',
            width: '34%',
        },
        {
            title: 'Countermeasures',
            children: [
                {
                    title: 'With countermeasures',
                    key: 'implemented',
                    dataIndex: 'implemented',
                    align: 'center',
                    width: '33%',
                    render: (_, record) => {
                        if (record.attribute == 'Risk level') {
                            return <b style={{ color: record.implemented[1] }}>{record.implemented[0]}</b>
                        }
                        return _
                    }
                },
                {
                    title: 'Without all countermeasures',
                    key: 'not_implemented',
                    dataIndex: 'not_implemented',
                    align: 'center',
                    width: '33%',
                    render: (_, record) => {
                        if (record.attribute == 'Risk level') {
                            return <b style={{ color: record.not_implemented[1] }}>{record.not_implemented[0]}</b>
                        }
                        return _
                    }
                }
            ]
        }
    ]

    const handleSave = async () => {
        const sendData = {
            data_system: dataSystem,
            data_countermeasures: dataCountermeasures,
            assets_countermeasures: assetsCountermeasures,
            assets_not_countermeasures: assetsNotCountermeasures,
            security_goals: securityGoals,
        }
        console.log('sendData', sendData);
    }

    if (!isAssessment) {
        return ''
    }
    return (
        <>
            <Collapse defaultActiveKey={['1', '2', '3', '4']} >
                <Panel header={'Risk level'} key='1'>
                    {/* <Space direction="vertical" size="middle"> */}
                    <Row gutter={16}>
                        <Col span={12}>
                            <Row>
                                <Col span={24}>
                                    <h3>System profile</h3>
                                    <Table
                                        columns={columnsAll}
                                        dataSource={dataSystem}
                                        pagination={false}
                                        rowKey="attribute"
                                    />
                                </Col>
                            </Row>
                        </Col>
                        <Col span={12}>
                            <Heatmap
                                {...configHeadmap}
                            />
                        </Col>
                    </Row>
                    <Row>
                        <h3>Assets</h3>
                        <ProTable
                            columns={columnAssets}
                            dataSource={assetsCountermeasures}
                            rowKey="id"
                            search={false}
                            toolBarRender={false}
                            pagination={{
                                pageSize: 7
                            }}
                            style={{
                                width: '100%'
                            }}
                            bordered
                        />
                    </Row>
                    {/* </Space> */}
                </Panel>
                <Panel header={'Security goals'} key='2' >
                    <ProTable
                        columns={columnsSeruityGoals}
                        dataSource={securityGoals}
                        rowKey="id"
                        search={false}
                        toolBarRender={false}
                        bordered
                    // bordered
                    />
                </Panel>
                {/* <Panel header={'Vulnerabilities'} key='3'>
                <Bar
                    data={dataVuls}
                    isGroup={true}
                    xField={'value'}
                    yField={'label'}
                    seriesField={'type'}
                    marginRatio={0}
                    label={{
                        position: 'right',
                        offset: 4,
                    }}
                    barStyle={{
                        radius: [2, 2, 0, 0],
                    }}
                />
            </Panel> */}
                <Panel header={'Countermeasures'} key='3'>
                    <Scatter {...configScatter} />
                </Panel>
            </Collapse>
            <Affix style={{ position: 'fixed', right: 50, bottom: 50, zIndex: 1000 }} >
                <Button type="primary"
                    onClick={handleSave}
                >
                    Save
                </Button>
            </Affix>
        </>

    )
}

export default Assessment