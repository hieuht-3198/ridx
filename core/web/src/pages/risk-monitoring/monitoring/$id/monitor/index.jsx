import { likelihoodToType, riskLevelNumberToType, riskLevelToType, riskLikelihoodNumberToType, riskSeverityNumberToType, severityToType, toFixNumber } from '@/shared/common';
import { Line } from '@ant-design/charts';
import ProForm, { ProFormDigit, ProFormUploadButton } from '@ant-design/pro-form';
import { Col, Divider, Form, message, Row, Select } from 'antd';
import { useEffect, useRef, useState } from 'react';
import { getNodeAttackGraph, postRiskMonitoring } from '../service';
import readXlsxFile from 'read-excel-file';
import * as Excel from "exceljs";
import FileSaver from 'file-saver';
import { getDeploymentScenario } from '@/pages/deployment-scenarios/service';
import { getSystemProfile } from '@/pages/system-profiles/list/service';

const MonitoringForm = ({deployment_scenario_id, sync, setSync}) => {
    const fileExtension = '.xlsx';
    const fileName = 'risk_monitoring_observer_data_template'

    const id = deployment_scenario_id
    const formRef = useRef();

    const [loading, setLoading] = useState(false)

    const timeStepInit = 2
    const nodeTemporalsInit = ['All']

    const [dataRisk, setDataRisk] = useState([])
    const [dataAssets, setDataAssets] = useState([])

    const [dataNode, setDataNode] = useState([])
    const [deploymentScenario, setDeploymentScenario] = useState({})
    const [systemProfile, setSystemProfile] = useState({})

    const configRiskChart = {
        data: dataRisk,
        xField: 'Step',
        yField: 'risk level',
        label: {},
        yAxis: {
            label: {
                formatter: (v) => riskLevelNumberToType(parseInt(v)),
                offset: 1,
            },
            min: 0,
            max: 5,
        },
        point: {
            size: 5,
            shape: 'diamond',
            style: {
                fill: 'white',
                stroke: '#5B8FF9',
                lineWidth: 2,
            },
        },
        tooltip: {
            showMarkers: false,
            fields: ['Severity', 'Likelihood', 'Risk level'],
        },
        state: {
            active: {
                style: {
                    shadowBlur: 4,
                    stroke: '#000',
                    fill: 'red',
                },
            },
        },
        interactions: [
            {
                type: 'marker-active',
            },
        ],
    };

    const configSeverityChart = {
        ...configRiskChart,
        yField: 'severity',
        yAxis: {
            label: {
                formatter: (v) => riskSeverityNumberToType(parseInt(v)),
                offset: 1,
            },
            min: 0,
            max: 6,
        },

    };

    const configLikelihoodChart = {
        ...configRiskChart,
        yField: 'likelihood',
        yAxis: {
            label: {
                formatter: (v) => riskLikelihoodNumberToType(parseInt(v)),
                offset: 1,
            },
            min: 0,
            max: 6,
        },
    };

    const configAssetSeverity = {
        data: dataAssets,
        xField: 'Step',
        yField: 'Severity',
        seriesField: 'Asset name',
        label: {},
        point: {
            size: 5,
            shape: 'diamond',
            style: {
                fill: 'white',
                stroke: '#5B8FF9',
                lineWidth: 2,
            },
        },
        tooltip: {
            showMarkers: false,
        },
        yAxis: {
            label: {
                offset: 1,
            },
            min: -1,
            max: 10,
        },
        legend: {
            position: 'top',
        },
    }

    const fetchData = async () => {
        setLoading(true)
        const res = await getNodeAttackGraph(id)
        if (res){
            setDataNode(res.data)
            const resDeploy = await getDeploymentScenario(id)
            setDeploymentScenario(resDeploy.data)
            if (resDeploy?.data){
                const resSys = await getSystemProfile(resDeploy.data.system_profile_id)
                setSystemProfile(resSys?.data)
            }
            await handleSubmitMonitoring(formRef?.current?.getFieldsValue())
        }
        setLoading(false)
    }

    const monitoringAPI = async (sendData) => {
        const res = await postRiskMonitoring(id, sendData)

        let tmpAssetCIA = []
        
        if (res) {
            res.data.cia.map((asset) => {
                asset.cia.map((cia, index) => {
                    tmpAssetCIA.push({
                        'Asset name': asset.name,
                        'Severity': toFixNumber(9 - cia),
                        'step': index,
                        'Step': `Step ${index}`,
                        'CIA': toFixNumber(cia),
                    })
                    return cia
                })
                return asset
            })
            // console.log('tmpAssetCIA', tmpAssetCIA)
            let tmpRiskLikelihood = res.data.likelihood.outcomes.map((likelihood, index) => ({
                'Likelihood': likelihoodToType(likelihood['True']),
                'Step': index,
                'likelihood': likelihood['True'],
            }))
            let tmpRiskSeverity = []
            for (let i = 0; i < sendData.time_step; i++) {
                tmpRiskSeverity.push({
                    'Step': i,
                    'Severity': severityToType(tmpAssetCIA.filter(as => as.step == i).reduce((prev, next) => prev + next.Severity, 0) / tmpAssetCIA.length * sendData.time_step),
                    'severity': tmpAssetCIA.filter(as => as.step == i).reduce((prev, next) => prev + next.Severity, 0) / tmpAssetCIA.length * sendData.time_step,
                })
            }
            // console.log('tmpRiskSeverity', tmpRiskSeverity);
            let tmpRiskLevel = []
            for (let i = 0; i < sendData.time_step; i++) {
                tmpRiskLevel.push({
                    'Step': `Step ${i}`,
                    'Severity': tmpRiskSeverity[i].Severity[0],
                    'severity': tmpRiskSeverity[i].Severity[1],
                    'Likelihood': tmpRiskLikelihood[i].Likelihood[0],
                    'likelihood': tmpRiskLikelihood[i].Likelihood[1],
                    'Risk level': riskLevelToType(tmpRiskSeverity[i].Severity[1], tmpRiskLikelihood[i].Likelihood[1])[0],
                    'risk level': riskLevelToType(tmpRiskSeverity[i].Severity[1], tmpRiskLikelihood[i].Likelihood[1])[2],
                })
            }
            setDataAssets(tmpAssetCIA)
            setDataRisk(tmpRiskLevel)
            return true
        }
        return false
    }

    const handleDownloadTemplateObserverData = async () => {

        const workbook = new Excel.Workbook();

        // General
        const generalWorksheet = workbook.addWorksheet("General");
        let index = 5
        generalWorksheet.mergeCells('A1', 'B1')
        generalWorksheet.getCell('A1').value = 'System profile'
        generalWorksheet.getRow(2).values = [null, 'ID', systemProfile.id]
        generalWorksheet.getRow(3).values = [null, 'Name', systemProfile.name]
        generalWorksheet.getRow(4).values = [null, 'Description', systemProfile.description]
        Object.keys(systemProfile?.custom_fields)?.map(field => {
            generalWorksheet.getRow(index).values = [null, field, systemProfile.custom_fields[field]]
            index++
        })
        generalWorksheet.getRow(index++).values = [null, 'Created by', systemProfile.created_by]
        generalWorksheet.getRow(index++).values = [null, 'Updated by', systemProfile.updated_by]
        generalWorksheet.getRow(index++).values = [null, 'Created at', systemProfile.created_at]
        generalWorksheet.getRow(index++).values = [null, 'Updated at', systemProfile.updated_at]

        generalWorksheet.mergeCells(`A${index}`, `B${index}`)
        generalWorksheet.getCell(`A${index}`).value = 'Deployment scenario'
        index++
        generalWorksheet.getRow(index++).values = [null, 'Name', deploymentScenario.name]
        generalWorksheet.getRow(index++).values = [null, 'Description', deploymentScenario.description]
        generalWorksheet.getRow(index++).values = [null, 'Stage', deploymentScenario.status]

        generalWorksheet.mergeCells(`A${index}`, `B${index}`)
        generalWorksheet.getCell(`A${index}`).value = 'Asset'
        index++
        generalWorksheet.getRow(index++).values = [null, 'ID', 'Name', 'Number CVE']
        dataNode.map((asset) => {
            generalWorksheet.getRow(index++).values = [null, asset.asset_id, asset.asset_name, asset.cves.length]
        })


        const observerDataSheet = workbook.addWorksheet('Observer data')
        observerDataSheet.mergeCells('A1', 'B1')
        observerDataSheet.getCell('A1').value = 'Observer data'
        observerDataSheet.mergeCells('D3', 'X3')
        observerDataSheet.getCell('D3').value = 'Observer step'
        let counter = 4
        observerDataSheet.getRow(counter++).values = [null, null, null, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        observerDataSheet.getRow(counter++).values = ['ID', 'Asset name', 'CVE']
        dataNode.map((asset) => {
            observerDataSheet.getRow(counter++).values = [asset.asset_id, asset.asset_name]
            asset.cves.map(cve => {
                observerDataSheet.getRow(counter++).values = [null, null, cve]
            })
            counter++
        })

        await workbook.xlsx.writeBuffer()
            .then(buffer => FileSaver.saveAs(new Blob([buffer]), fileName + fileExtension))
            .catch(err => {
                message.error(`Download error: ${err}`)
            })
    }

    const handleSubmitMonitoring = async (values) => {
        let observerData = []
        if (values?.observer_data?.length) {
            const file = values.observer_data[0].originFileObj
            let max_step = 0
            try {
                const observerDataSheet = await readXlsxFile(file, { sheet: 'Observer data' });
                for (let counter = 5; counter < observerDataSheet.length; counter++) {
                    let asset_id = observerDataSheet[counter][0]
                    counter++
                    if (counter >= observerDataSheet.length) {
                        break
                    }
                    let step = 0
                    while (observerDataSheet[counter][2]) {
                        let cve_id = observerDataSheet[counter][2]
                        let observer_data = []
                        for (let index = 3; index < observerDataSheet[counter].length; index++) {
                            if (observerDataSheet[counter][index] !== null) {
                                observer_data.push({
                                    step: index - 3,
                                    value: observerDataSheet[counter][index]
                                })
                                step = index - 2
                            }
                        }
                        max_step = max_step > step ? max_step : step
                        observerData.push({
                            asset_id,
                            cve_id,
                            observer_data,
                        })
                        counter++
                        if (counter == observerDataSheet.length) {
                            break
                        }
                    }
                }

            } catch (err) {
                console.log(err);
                message.error('Please check observer data file!')
                return true
            }
            // TODO: Validation

            if (max_step > values.time_step) {
                message.error(`Observer step (${max_step}) is greater than Time step (${values.time_step})`)
                return true
            }
        }
        let sendData = {
            time_step: values.time_step,
            observer_data: observerData,
            node_temporals: [],
        }
        if (values.node_temporals.includes('All')) {
            sendData.node_temporals = ['All']
        } else {
            let tmp = {}
            values.node_temporals.map((node) => {
                let tmpStr = node.split('_')
                tmp[tmpStr[1]] = tmp[tmpStr[1]] ? [...tmp[tmpStr[1]], tmpStr[0]] : [tmpStr[0]]
                return node
            })
            sendData.node_temporals = Object.keys(tmp).map((as) => ({
                'asset_id': as,
                'cves': tmp[as],
            }))
        }
        setLoading(true)
        await monitoringAPI(sendData)
        setLoading(false)
    }

    useEffect(() => {
        fetchData()
    }, [sync])


    return (
        <Row gutter={20}>
            <Col span={18}>
                <h3>Risk level</h3>
                <Line
                    {...configRiskChart}
                />
                <Divider />
                <h3>Likelihood</h3>
                <Line
                    {...configLikelihoodChart}
                    loading={loading}
                />
                <Divider />
                <h3>Severity</h3>
                <Line
                    {...configSeverityChart}
                />
                <Divider />
                <h3>Asset severity</h3>
                <Line
                    {...configAssetSeverity}
                    loading={loading}
                />
            </Col>
            <Col span={6}>
                <ProForm
                    initialValues={{
                        time_step: timeStepInit,
                        node_temporals: nodeTemporalsInit,
                    }}
                    onFinish={handleSubmitMonitoring}
                    formRef={formRef}
                >
                    <ProFormDigit
                        label="Time step"
                        name="time_step"
                        min={2}
                        max={20}
                        rules={[
                            {
                                required: true
                            }
                        ]}
                    />
                    <Form.Item
                        label="Node temporal(s)"
                        name="node_temporals"
                        rules={[
                            {
                                required: true
                            }
                        ]}
                    >
                        <Select
                            mode="multiple"
                            options={
                                [
                                    {
                                        label: 'All',
                                        value: 'All',
                                    },
                                    ...dataNode?.map(asset => ({
                                        label: asset.asset_name,
                                        options: asset.cves.map((cve) => ({
                                            label: `${cve} on ${asset.asset_name}`,
                                            value: `${cve}_${asset.asset_id}`,
                                        }))
                                    })),
                                ]
                            }
                        />
                    </Form.Item>
                    <ProFormUploadButton
                        name="observer_data"
                        label="Observer data"
                        max={1}
                        action="/api/upload_file"
                        accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        fieldProps={{
                            name: 'file',
                        }}
                        title="Click to Upload"
                        extra={(
                            <a
                                onClick={handleDownloadTemplateObserverData}
                            >
                                Download template observer data
                            </a>
                        )}
                    />
                </ProForm>
            </Col>
        </Row>
    );
};

export default MonitoringForm;