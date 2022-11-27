import { PageContainer } from '@ant-design/pro-layout';
import { Card, Descriptions, Tabs } from 'antd';
import { useEffect, useState } from 'react';
import { getNodeAttackGraph } from './service';
import { getDeploymentScenario } from '@/pages/deployment-scenarios/service';
import { getSystemProfile } from '@/pages/system-profiles/list/service';
import MonitoringForm from './monitor';
import { MonitorOutlined, RocketFilled, RocketOutlined, SettingOutlined, SyncOutlined } from '@ant-design/icons';
import ScanVulnerability from './scan-vulnerability/$id';
import VulnerabilySettingMonitoring from './update/vulnerability-setting';
import AttackGraphMonitoring from './update/attack_graph';
import DetectThreat from './detect-threat';

const { TabPane } = Tabs

const Monitoring = (props) => {

    const { id } = props?.match?.params
    const [deploymentScenario, setDeploymentScenario] = useState({})
    const [systemProfile, setSystemProfile] = useState({})
    const [sync, setSync] = useState(true)

    const fetchData = async () => {
        const resDeploy = await getDeploymentScenario(id)
        setDeploymentScenario(resDeploy.data)
        if (resDeploy?.data) {
            const resSys = await getSystemProfile(resDeploy.data.system_profile_id)
            setSystemProfile(resSys.data)
        }
    }

    useEffect(() => {
        fetchData()
    }, [])


    return (
        <PageContainer
            header={{
                title: 'Risk monitoring',
            }}
            content={
                <Descriptions column={2} style={{ marginBottom: -16 }}>
                    <Descriptions.Item label="System profile">
                        <a
                            onClick={() => {

                            }}
                        >
                            {systemProfile.name}
                        </a>
                    </Descriptions.Item>
                    <Descriptions.Item label="Deployment scenario">
                        <a
                            onClick={() => {

                            }}
                        >
                            {deploymentScenario.name}
                        </a>
                    </Descriptions.Item>
                </Descriptions>
            }
        >
            <Card>
                <Tabs defaultActiveKey="1" destroyInactiveTabPane>
                    <TabPane
                        tab={
                            <span>
                                <MonitorOutlined />
                                Monitoring
                            </span>
                        }
                        key="1"
                    >
                        <MonitoringForm deployment_scenario_id={id} sync={sync} setSync={setSync}/>
                    </TabPane>
                    <TabPane
                        tab={
                            <span>
                                <RocketOutlined />
                                Update CVE
                            </span>
                        }
                        key="2"
                    >
                        <VulnerabilySettingMonitoring deployment_scenario_id={id} sync={sync} setSync={setSync}/>
                    </TabPane>
                    <TabPane
                        tab={
                            <span>
                                <RocketOutlined />
                                Update attack graph
                            </span>
                        }
                        key="4"
                    >
                        <AttackGraphMonitoring deployment_scenario_id={id} sync={sync} setSync={setSync}/>
                    </TabPane>
                    <TabPane
                        tab={
                            <span>
                                <SyncOutlined />
                                Scan vulnerability
                            </span>
                        }
                        key="3"
                    >
                        <ScanVulnerability deployment_scenario_id={id} sync={sync} setSync={setSync}/>
                    </TabPane>
                    <TabPane
                        tab={
                            <span>
                                <SyncOutlined />
                                Detect threat
                            </span>
                        }
                        key="5"
                    >
                        <DetectThreat deployment_scenario_id={id} />
                    </TabPane>
                </Tabs>
            </Card>
        </PageContainer>
    );
};

export default Monitoring;