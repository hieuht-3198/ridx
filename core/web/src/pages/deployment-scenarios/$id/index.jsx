import { DetailIconAction } from "@/components/TableAction"
import { getHistoryAssessmentDeploymentScenario } from "@/pages/risk-assessments/service"
import { getSystemProfile } from "@/pages/system-profiles/list/service"
import { PageContainer } from "@ant-design/pro-layout"
import ProTable from "@ant-design/pro-table"
import { Card, Col, Descriptions, Row, Space, Tabs } from "antd"
import { useState } from "react"
import { useEffect } from "react"
import DeploymentScenarioInfo from "../components/info"
import { getDeploymentScenario } from "../service"
import { history } from 'umi';
import { riskLevelToColor } from "@/shared/common"
import { DEPLOYMENT_SCENARIO_REQUIREMENTS_ANALYSIS } from "@/shared/constant"
import RiskRatingBreakdownPie from "./components/RiskRating"
import RiskHeatMap from "./components/RiskHeadMap"
import IntroduceRowDeploymentScenarioDetail from "./components/IntroduceRow"
import TopVulnerability from "./components/TopVulnerability"
import TopAsset from "./components/TopAsset"
import TopRiskAssessment from "./components/TopRiskAssessment"

const { TabPane } = Tabs

const DeploymentScenarioDetail = (props) => {

    const { id } = props?.match?.params
    const [deploymentScenario, setDeploymentScenario] = useState({})
    const [systemProfile, setSystemProfile] = useState({})


    const fetchData = async () => {
        const res = await getDeploymentScenario(id)
        setDeploymentScenario(res.data)
        if (res.data) {
            const resSys = await getSystemProfile(res.data.system_profile_id)
            setSystemProfile(resSys.data)
        }
    }

    useEffect(() => {
        fetchData()
    }, [])

    const columns = [
        {
            title: 'Name',
            dataIndex: 'name',
            key: 'name',
            width: '30%',
        },
        {
            title: 'Risk',
            hideInForm: true,
            hideInSearch: true,
            children: [
                {
                    title: "With countermeasures",
                    dataIndex: "i_r",
                    key: 'i_r',
                    align: 'center',
                    render: (_, record) => {
                        const riskLevel = record?.result?.risk?.risk_level?.countermeasures[0]
                        return <b style={{ color: riskLevelToColor(riskLevel) }}>{riskLevel}</b>
                    },
                    width: '20%',
                },
                {
                    title: "Not implemented",
                    dataIndex: "n_r",
                    key: 'n_r',
                    align: 'center',
                    render: (_, record) => {
                        const riskLevel = record?.result?.risk?.risk_level?.countermeasures[0]
                        return <b style={{ color: riskLevelToColor(riskLevel) }}>{riskLevel}</b>
                    },
                    width: '20%',
                },
            ]
        },
        {
            title: 'Created at',
            dataIndex: 'created_at',
            key: 'created_at',
            hideInForm: true,
            hideInSearch: true,
            valueType: 'date',
            align: 'center',
            width: '15%',
        },
        {
            title: 'Action',
            dataIndex: 'action',
            key: 'action',
            hideInForm: true,
            hideInSearch: true,
            align: 'center',
            width: '15%',
            render: (_, record) => (
                <DetailIconAction
                    title="Detail assessment"
                    onClick={() => {
                        history.push(`/risk-assessments/${record.id}`)
                    }}
                />
            )
        },
    ]


    return (
        <PageContainer
            header={{
                title: "Deployment scenario detail",
            }}
            content={
                <Descriptions column={2} style={{ marginBottom: -16 }}>
                    <Descriptions.Item label="Name">
                        <a
                            onClick={() => {

                            }}
                        >
                            {deploymentScenario.name}
                        </a>
                    </Descriptions.Item>
                    <Descriptions.Item label="System profile">
                        <a
                            onClick={() => {
                                history.push(`/system-profiles/${systemProfile.id}`)
                            }}
                        >
                            {systemProfile.name}
                        </a>
                    </Descriptions.Item>
                    <Descriptions.Item label="Description">{deploymentScenario.description}</Descriptions.Item>
                    <Descriptions.Item label="Stage">{deploymentScenario.status}</Descriptions.Item>
                </Descriptions>
            }

        >
            {/* <Space direction="vertical" size="large"> */}
            <IntroduceRowDeploymentScenarioDetail />
            <Row gutter={20} style={{ marginBottom: 20 }}>
                <Col span={12}>
                    <RiskRatingBreakdownPie />
                </Col>
                <Col span={12}>
                    <RiskHeatMap />
                </Col>
            </Row>
            <Row gutter={20} style={{ marginBottom: 20 }}>
                <Col span={8}>
                    <TopRiskAssessment />
                </Col>
                <Col span={8}>
                    <TopAsset />
                </Col>
                <Col span={8}>
                    <TopVulnerability />
                </Col>
            </Row>
            <Row gutter={20}>
                <Col span={24}>
                    {
                        deploymentScenario?.status === DEPLOYMENT_SCENARIO_REQUIREMENTS_ANALYSIS ? (
                            <Card
                                title="Risk assessment history"
                            >
                                <ProTable
                                    request={async (params) => {
                                        return await getHistoryAssessmentDeploymentScenario(id, params)
                                    }}
                                    columns={columns}
                                    bordered
                                    toolBarRender={false}
                                    rowKey="created_at"
                                />

                            </Card>
                        ) : (
                            <Card
                            >
                                <Tabs defaultActiveKey="1">
                                    <TabPane tab="Risk monitoring" key="1">
                                        Risk monitoring
                                    </TabPane>
                                    <TabPane tab="Risk assessment history" key="2">
                                        <ProTable
                                            request={async (params) => {
                                                return await getHistoryAssessmentDeploymentScenario(id, params)
                                            }}
                                            columns={columns}
                                            bordered
                                            toolBarRender={false}
                                            rowKey="created_at"
                                        />
                                    </TabPane>
                                </Tabs>
                            </Card>
                        )
                    }
                </Col>
            </Row>
            {/* </Space> */}
        </PageContainer>
    )

}

export default DeploymentScenarioDetail