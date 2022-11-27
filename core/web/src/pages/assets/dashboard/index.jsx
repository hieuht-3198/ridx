import { Suspense, useState } from 'react';
import { EllipsisOutlined } from '@ant-design/icons';
import { Col, Dropdown, Menu, Row } from 'antd';
import { GridContent } from '@ant-design/pro-layout';
import IntroduceRow from './components/IntroduceRow';
import SalesCard from './components/SalesCard';
import TopSearch from './components/TopSearch';
import ProportionSales from './components/ProportionSales';
import OfflineData from './components/OfflineData';
import { useRequest } from 'umi';
import { fakeChartData } from './service';
import PageLoading from '@/components/Dashboard/PageLoading';
import { getTimeDistance } from './utils/utils';
import styles from './style.less';

const res_data = {
  "visitData": [
      {
          "x": "2022-05-30",
          "y": 7
      },
      {
          "x": "2022-05-31",
          "y": 5
      },
      {
          "x": "2022-06-01",
          "y": 4
      },
      {
          "x": "2022-06-02",
          "y": 2
      },
      {
          "x": "2022-06-03",
          "y": 4
      },
      {
          "x": "2022-06-04",
          "y": 7
      },
      {
          "x": "2022-06-05",
          "y": 5
      },
      {
          "x": "2022-06-06",
          "y": 6
      },
      {
          "x": "2022-06-07",
          "y": 5
      },
      {
          "x": "2022-06-08",
          "y": 9
      },
      {
          "x": "2022-06-09",
          "y": 6
      },
      {
          "x": "2022-06-10",
          "y": 3
      },
      {
          "x": "2022-06-11",
          "y": 1
      },
      {
          "x": "2022-06-12",
          "y": 5
      },
      {
          "x": "2022-06-13",
          "y": 3
      },
      {
          "x": "2022-06-14",
          "y": 6
      },
      {
          "x": "2022-06-15",
          "y": 5
      }
  ],
  "visitData2": [
      {
          "x": "2022-05-30",
          "y": 1
      },
      {
          "x": "2022-05-31",
          "y": 6
      },
      {
          "x": "2022-06-01",
          "y": 4
      },
      {
          "x": "2022-06-02",
          "y": 8
      },
      {
          "x": "2022-06-03",
          "y": 3
      },
      {
          "x": "2022-06-04",
          "y": 7
      },
      {
          "x": "2022-06-05",
          "y": 2
      }
  ],
  "salesData": [
      {
          "x": "1月",
          "y": 311
      },
      {
          "x": "2月",
          "y": 979
      },
      {
          "x": "3月",
          "y": 972
      },
      {
          "x": "4月",
          "y": 884
      },
      {
          "x": "5月",
          "y": 533
      },
      {
          "x": "6月",
          "y": 658
      },
      {
          "x": "7月",
          "y": 906
      },
      {
          "x": "8月",
          "y": 1007
      },
      {
          "x": "9月",
          "y": 804
      },
      {
          "x": "10月",
          "y": 264
      },
      {
          "x": "11月",
          "y": 528
      },
      {
          "x": "12月",
          "y": 364
      }
  ],
  "searchData": [
      {
          "index": 1,
          "keyword": "搜索关键词-0",
          "count": 633,
          "range": 18,
          "status": 1
      },
      {
          "index": 2,
          "keyword": "搜索关键词-1",
          "count": 668,
          "range": 12,
          "status": 1
      },
      {
          "index": 3,
          "keyword": "搜索关键词-2",
          "count": 248,
          "range": 32,
          "status": 1
      },
      {
          "index": 4,
          "keyword": "搜索关键词-3",
          "count": 375,
          "range": 78,
          "status": 0
      },
      {
          "index": 5,
          "keyword": "搜索关键词-4",
          "count": 810,
          "range": 85,
          "status": 1
      },
      {
          "index": 6,
          "keyword": "搜索关键词-5",
          "count": 536,
          "range": 16,
          "status": 1
      },
      {
          "index": 7,
          "keyword": "搜索关键词-6",
          "count": 64,
          "range": 36,
          "status": 1
      },
      {
          "index": 8,
          "keyword": "搜索关键词-7",
          "count": 659,
          "range": 51,
          "status": 1
      },
      {
          "index": 9,
          "keyword": "搜索关键词-8",
          "count": 12,
          "range": 56,
          "status": 1
      },
      {
          "index": 10,
          "keyword": "搜索关键词-9",
          "count": 404,
          "range": 43,
          "status": 1
      },
      {
          "index": 11,
          "keyword": "搜索关键词-10",
          "count": 477,
          "range": 35,
          "status": 1
      },
      {
          "index": 12,
          "keyword": "搜索关键词-11",
          "count": 966,
          "range": 45,
          "status": 1
      },
      {
          "index": 13,
          "keyword": "搜索关键词-12",
          "count": 430,
          "range": 26,
          "status": 0
      },
      {
          "index": 14,
          "keyword": "搜索关键词-13",
          "count": 577,
          "range": 79,
          "status": 0
      },
      {
          "index": 15,
          "keyword": "搜索关键词-14",
          "count": 638,
          "range": 97,
          "status": 1
      },
      {
          "index": 16,
          "keyword": "搜索关键词-15",
          "count": 648,
          "range": 62,
          "status": 0
      },
      {
          "index": 17,
          "keyword": "搜索关键词-16",
          "count": 985,
          "range": 94,
          "status": 1
      },
      {
          "index": 18,
          "keyword": "搜索关键词-17",
          "count": 362,
          "range": 99,
          "status": 1
      },
      {
          "index": 19,
          "keyword": "搜索关键词-18",
          "count": 462,
          "range": 53,
          "status": 1
      },
      {
          "index": 20,
          "keyword": "搜索关键词-19",
          "count": 871,
          "range": 27,
          "status": 1
      },
      {
          "index": 21,
          "keyword": "搜索关键词-20",
          "count": 559,
          "range": 45,
          "status": 0
      },
      {
          "index": 22,
          "keyword": "搜索关键词-21",
          "count": 555,
          "range": 58,
          "status": 1
      },
      {
          "index": 23,
          "keyword": "搜索关键词-22",
          "count": 929,
          "range": 43,
          "status": 0
      },
      {
          "index": 24,
          "keyword": "搜索关键词-23",
          "count": 267,
          "range": 8,
          "status": 0
      },
      {
          "index": 25,
          "keyword": "搜索关键词-24",
          "count": 878,
          "range": 47,
          "status": 1
      },
      {
          "index": 26,
          "keyword": "搜索关键词-25",
          "count": 795,
          "range": 99,
          "status": 0
      },
      {
          "index": 27,
          "keyword": "搜索关键词-26",
          "count": 202,
          "range": 50,
          "status": 0
      },
      {
          "index": 28,
          "keyword": "搜索关键词-27",
          "count": 364,
          "range": 84,
          "status": 1
      },
      {
          "index": 29,
          "keyword": "搜索关键词-28",
          "count": 713,
          "range": 24,
          "status": 0
      },
      {
          "index": 30,
          "keyword": "搜索关键词-29",
          "count": 551,
          "range": 43,
          "status": 0
      },
      {
          "index": 31,
          "keyword": "搜索关键词-30",
          "count": 5,
          "range": 35,
          "status": 1
      },
      {
          "index": 32,
          "keyword": "搜索关键词-31",
          "count": 74,
          "range": 37,
          "status": 0
      },
      {
          "index": 33,
          "keyword": "搜索关键词-32",
          "count": 597,
          "range": 80,
          "status": 0
      },
      {
          "index": 34,
          "keyword": "搜索关键词-33",
          "count": 665,
          "range": 1,
          "status": 1
      },
      {
          "index": 35,
          "keyword": "搜索关键词-34",
          "count": 165,
          "range": 26,
          "status": 1
      },
      {
          "index": 36,
          "keyword": "搜索关键词-35",
          "count": 537,
          "range": 28,
          "status": 1
      },
      {
          "index": 37,
          "keyword": "搜索关键词-36",
          "count": 469,
          "range": 24,
          "status": 0
      },
      {
          "index": 38,
          "keyword": "搜索关键词-37",
          "count": 676,
          "range": 67,
          "status": 1
      },
      {
          "index": 39,
          "keyword": "搜索关键词-38",
          "count": 146,
          "range": 41,
          "status": 0
      },
      {
          "index": 40,
          "keyword": "搜索关键词-39",
          "count": 533,
          "range": 73,
          "status": 0
      },
      {
          "index": 41,
          "keyword": "搜索关键词-40",
          "count": 835,
          "range": 71,
          "status": 1
      },
      {
          "index": 42,
          "keyword": "搜索关键词-41",
          "count": 299,
          "range": 11,
          "status": 1
      },
      {
          "index": 43,
          "keyword": "搜索关键词-42",
          "count": 828,
          "range": 95,
          "status": 1
      },
      {
          "index": 44,
          "keyword": "搜索关键词-43",
          "count": 454,
          "range": 1,
          "status": 0
      },
      {
          "index": 45,
          "keyword": "搜索关键词-44",
          "count": 787,
          "range": 61,
          "status": 0
      },
      {
          "index": 46,
          "keyword": "搜索关键词-45",
          "count": 566,
          "range": 83,
          "status": 1
      },
      {
          "index": 47,
          "keyword": "搜索关键词-46",
          "count": 769,
          "range": 41,
          "status": 0
      },
      {
          "index": 48,
          "keyword": "搜索关键词-47",
          "count": 911,
          "range": 16,
          "status": 0
      },
      {
          "index": 49,
          "keyword": "搜索关键词-48",
          "count": 134,
          "range": 39,
          "status": 1
      },
      {
          "index": 50,
          "keyword": "搜索关键词-49",
          "count": 31,
          "range": 12,
          "status": 0
      }
  ],
  "offlineData": [
      {
          "name": "Stores 0",
          "cvr": 0.4
      },
      {
          "name": "Stores 1",
          "cvr": 0.1
      },
      {
          "name": "Stores 2",
          "cvr": 0.6
      },
      {
          "name": "Stores 3",
          "cvr": 0.1
      },
      {
          "name": "Stores 4",
          "cvr": 0.1
      },
      {
          "name": "Stores 5",
          "cvr": 0.2
      },
      {
          "name": "Stores 6",
          "cvr": 0.5
      },
      {
          "name": "Stores 7",
          "cvr": 0.2
      },
      {
          "name": "Stores 8",
          "cvr": 0.1
      },
      {
          "name": "Stores 9",
          "cvr": 0.1
      }
  ],
  "offlineChartData": [
      {
          "date": "04:24",
          "type": "客流量",
          "value": 50
      },
      {
          "date": "04:24",
          "type": "支付笔数",
          "value": 85
      },
      {
          "date": "04:54",
          "type": "客流量",
          "value": 37
      },
      {
          "date": "04:54",
          "type": "支付笔数",
          "value": 83
      },
      {
          "date": "05:24",
          "type": "客流量",
          "value": 99
      },
      {
          "date": "05:24",
          "type": "支付笔数",
          "value": 19
      },
      {
          "date": "05:54",
          "type": "客流量",
          "value": 105
      },
      {
          "date": "05:54",
          "type": "支付笔数",
          "value": 101
      },
      {
          "date": "06:24",
          "type": "客流量",
          "value": 28
      },
      {
          "date": "06:24",
          "type": "支付笔数",
          "value": 104
      },
      {
          "date": "06:54",
          "type": "客流量",
          "value": 12
      },
      {
          "date": "06:54",
          "type": "支付笔数",
          "value": 59
      },
      {
          "date": "07:24",
          "type": "客流量",
          "value": 46
      },
      {
          "date": "07:24",
          "type": "支付笔数",
          "value": 65
      },
      {
          "date": "07:54",
          "type": "客流量",
          "value": 58
      },
      {
          "date": "07:54",
          "type": "支付笔数",
          "value": 26
      },
      {
          "date": "08:24",
          "type": "客流量",
          "value": 90
      },
      {
          "date": "08:24",
          "type": "支付笔数",
          "value": 19
      },
      {
          "date": "08:54",
          "type": "客流量",
          "value": 59
      },
      {
          "date": "08:54",
          "type": "支付笔数",
          "value": 92
      },
      {
          "date": "09:24",
          "type": "客流量",
          "value": 58
      },
      {
          "date": "09:24",
          "type": "支付笔数",
          "value": 67
      },
      {
          "date": "09:54",
          "type": "客流量",
          "value": 21
      },
      {
          "date": "09:54",
          "type": "支付笔数",
          "value": 95
      },
      {
          "date": "10:24",
          "type": "客流量",
          "value": 92
      },
      {
          "date": "10:24",
          "type": "支付笔数",
          "value": 12
      },
      {
          "date": "10:54",
          "type": "客流量",
          "value": 66
      },
      {
          "date": "10:54",
          "type": "支付笔数",
          "value": 10
      },
      {
          "date": "11:24",
          "type": "客流量",
          "value": 29
      },
      {
          "date": "11:24",
          "type": "支付笔数",
          "value": 14
      },
      {
          "date": "11:54",
          "type": "客流量",
          "value": 23
      },
      {
          "date": "11:54",
          "type": "支付笔数",
          "value": 67
      },
      {
          "date": "12:24",
          "type": "客流量",
          "value": 108
      },
      {
          "date": "12:24",
          "type": "支付笔数",
          "value": 27
      },
      {
          "date": "12:54",
          "type": "客流量",
          "value": 33
      },
      {
          "date": "12:54",
          "type": "支付笔数",
          "value": 97
      },
      {
          "date": "13:24",
          "type": "客流量",
          "value": 48
      },
      {
          "date": "13:24",
          "type": "支付笔数",
          "value": 28
      },
      {
          "date": "13:54",
          "type": "客流量",
          "value": 14
      },
      {
          "date": "13:54",
          "type": "支付笔数",
          "value": 52
      }
  ],
  "salesTypeData": [
      {
          "x": "家用电器",
          "y": 4544
      },
      {
          "x": "食用酒水",
          "y": 3321
      },
      {
          "x": "个护健康",
          "y": 3113
      },
      {
          "x": "服饰箱包",
          "y": 2341
      },
      {
          "x": "母婴产品",
          "y": 1231
      },
      {
          "x": "其他",
          "y": 1231
      }
  ],
  "salesTypeDataOnline": [
      {
          "x": "家用电器",
          "y": 244
      },
      {
          "x": "食用酒水",
          "y": 321
      },
      {
          "x": "个护健康",
          "y": 311
      },
      {
          "x": "服饰箱包",
          "y": 41
      },
      {
          "x": "母婴产品",
          "y": 121
      },
      {
          "x": "其他",
          "y": 111
      }
  ],
  "salesTypeDataOffline": [
      {
          "x": "家用电器",
          "y": 99
      },
      {
          "x": "食用酒水",
          "y": 188
      },
      {
          "x": "个护健康",
          "y": 344
      },
      {
          "x": "服饰箱包",
          "y": 255
      },
      {
          "x": "其他",
          "y": 65
      }
  ],
  "radarData": [
      {
          "name": "个人",
          "label": "引用",
          "value": 10
      },
      {
          "name": "个人",
          "label": "口碑",
          "value": 8
      },
      {
          "name": "个人",
          "label": "产量",
          "value": 4
      },
      {
          "name": "个人",
          "label": "贡献",
          "value": 5
      },
      {
          "name": "个人",
          "label": "热度",
          "value": 7
      },
      {
          "name": "团队",
          "label": "引用",
          "value": 3
      },
      {
          "name": "团队",
          "label": "口碑",
          "value": 9
      },
      {
          "name": "团队",
          "label": "产量",
          "value": 6
      },
      {
          "name": "团队",
          "label": "贡献",
          "value": 3
      },
      {
          "name": "团队",
          "label": "热度",
          "value": 1
      },
      {
          "name": "部门",
          "label": "引用",
          "value": 4
      },
      {
          "name": "部门",
          "label": "口碑",
          "value": 1
      },
      {
          "name": "部门",
          "label": "产量",
          "value": 6
      },
      {
          "name": "部门",
          "label": "贡献",
          "value": 5
      },
      {
          "name": "部门",
          "label": "热度",
          "value": 7
      }
  ]
}

const Analysis = () => {
  const [salesType, setSalesType] = useState('all');
  const [currentTabKey, setCurrentTabKey] = useState('');
  const [rangePickerValue, setRangePickerValue] = useState(getTimeDistance('year'));
  const loading = false
  const data = res_data
  const selectDate = (type) => {
    setRangePickerValue(getTimeDistance(type));
  };

  const handleRangePickerChange = (value) => {
    setRangePickerValue(value);
  };

  const isActive = (type) => {
    if (!rangePickerValue) {
      return '';
    }

    const value = getTimeDistance(type);

    if (!value) {
      return '';
    }

    if (!rangePickerValue[0] || !rangePickerValue[1]) {
      return '';
    }

    if (
      rangePickerValue[0].isSame(value[0], 'day') &&
      rangePickerValue[1].isSame(value[1], 'day')
    ) {
      return styles.currentDate;
    }

    return '';
  };

  let salesPieData;

  if (salesType === 'all') {
    salesPieData = data?.salesTypeData;
  } else {
    salesPieData = salesType === 'online' ? data?.salesTypeDataOnline : data?.salesTypeDataOffline;
  }

  const menu = (
    <Menu>
      <Menu.Item>操作一</Menu.Item>
      <Menu.Item>操作二</Menu.Item>
    </Menu>
  );
  const dropdownGroup = (
    <span className={styles.iconGroup}>
      <Dropdown overlay={menu} placement="bottomRight">
        <EllipsisOutlined />
      </Dropdown>
    </span>
  );

  const handleChangeSalesType = (e) => {
    setSalesType(e.target.value);
  };

  const handleTabChange = (key) => {
    setCurrentTabKey(key);
  };

  const activeKey = currentTabKey || (data?.offlineData[0] && data?.offlineData[0].name) || '';
  return (
    <GridContent>
      <>
        <Suspense fallback={<PageLoading />}>
          <IntroduceRow loading={loading} visitData={data?.visitData || []} />
        </Suspense>

        <Suspense fallback={null}>
          <SalesCard
            rangePickerValue={rangePickerValue}
            salesData={data?.salesData || []}
            isActive={isActive}
            handleRangePickerChange={handleRangePickerChange}
            loading={loading}
            selectDate={selectDate}
          />
        </Suspense>

        <Row
          gutter={24}
          style={{
            marginTop: 24,
          }}
        >
          <Col xl={12} lg={24} md={24} sm={24} xs={24}>
            <Suspense fallback={null}>
              <TopSearch
                loading={loading}
                visitData2={data?.visitData2 || []}
                searchData={data?.searchData || []}
                dropdownGroup={dropdownGroup}
              />
            </Suspense>
          </Col>
          <Col xl={12} lg={24} md={24} sm={24} xs={24}>
            <Suspense fallback={null}>
              <ProportionSales
                dropdownGroup={dropdownGroup}
                salesType={salesType}
                loading={loading}
                salesPieData={salesPieData || []}
                handleChangeSalesType={handleChangeSalesType}
              />
            </Suspense>
          </Col>
        </Row>

        <Suspense fallback={null}>
          <OfflineData
            activeKey={activeKey}
            loading={loading}
            offlineData={data?.offlineData || []}
            offlineChartData={data?.offlineChartData || []}
            handleTabChange={handleTabChange}
          />
        </Suspense>
      </>
    </GridContent>
  );
};

export default Analysis;
