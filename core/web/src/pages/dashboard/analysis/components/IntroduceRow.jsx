import { InfoCircleOutlined } from '@ant-design/icons';
import { TinyArea, TinyColumn, Progress } from '@ant-design/charts';
import { Card, Col, Row, Tooltip } from 'antd';
import numeral from 'numeral';
import { ChartCard, Field } from '../../../../components/Dashboard/Charts';
import Trend from '../../../../components/Dashboard/Trend';
import styles from '../style.less';
import Metric from '@/components/Dashboard/Metric';
const topColResponsiveProps = {
  xs: 24,
  sm: 12,
  md: 12,
  lg: 12,
  xl: 6,
  style: {
    marginBottom: 24,
  },
};

const IntroduceRow = ({ loading, visitData }) => (
  <Row gutter={24}>
    <Col {...topColResponsiveProps}>
      <ChartCard
        loading={loading}
        bordered={false}
        title="Risk"
        action={
          <Tooltip title="指标说明">
            <InfoCircleOutlined />
          </Tooltip>
        }
        total="78%"
        contentHeight={150}
      >
        You should fix your high severity issues as soon as possible and ideally within thirty days to minimise your risk of a breach.
        {/* <Progress
          height={46}
          percent={0.78}
          color="#13C2C2"
          forceFit
          size={8}
          marker={[
            {
              value: 0.8,
              style: {
                stroke: '#13C2C2',
              },
            },
          ]}
        /> */}
      </ChartCard>
    </Col>
    <Col {...topColResponsiveProps}>
      <ChartCard
        bordered={false}
        title="Deployment profiles"
        action={
          <Tooltip title="指标说明">
            <InfoCircleOutlined />
          </Tooltip>
        }
        loading={loading}
        total={numeral(12).format('0,0')}
      // footer={<Field label="日销售额" value={`￥${numeral(12423).format('0,0')}`} />}
      contentHeight={150}
      >
        <Metric data={{
          critical: 2,
          high: 3,
          medium: 5,
          low: 6,
        }}/>
      </ChartCard>
    </Col>

    <Col {...topColResponsiveProps}>
      <ChartCard
        bordered={false}
        loading={loading}
        title="Deployment scenarios"
        action={
          <Tooltip title="指标说明">
            <InfoCircleOutlined />
          </Tooltip>
        }
        total={numeral(300).format('0,0')}
        // footer={<Field label="日访问量" value={numeral(1234).format('0,0')} />}
        contentHeight={150}
      >
        <Metric data={{
          critical: 20,
          high: 30,
          medium: 50,
          low: 60,
        }}/>
      </ChartCard>
    </Col>
    <Col {...topColResponsiveProps}>
      <ChartCard
        bordered={false}
        loading={loading}
        title="Vulnerabilities"
        action={
          <Tooltip title="指标说明">
            <InfoCircleOutlined />
          </Tooltip>
        }
        total={numeral(6560).format('0,0')}
        // footer={<Field label="转化率" value="60%" />}
        contentHeight={150}
      >
        <Metric data={{
          critical: 200,
          high: 3000,
          medium: 5000,
          low: 6000,
        }}/>
      </ChartCard>
    </Col>
  </Row>
);

export default IntroduceRow;
