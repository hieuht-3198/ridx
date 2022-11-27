import { PageContainer } from '@ant-design/pro-layout';
import ProTable from '@ant-design/pro-table';
import React, { useRef, useState } from 'react';
import { Button, Empty, Upload } from 'antd'
import { UploadOutlined } from '@ant-design/icons';
import readXlsxFile from 'read-excel-file';

const Asset = () => {
  const actionRef = useRef()
  const [assets, setAssets] = useState([])

  const columns = [
    {
      title: 'ID',
      dataIndex: 'asset_id',
      sorter: true,
      width: '10%',
      key: 'id'
    },
    {
      title: 'Name',
      dataIndex: 'name',
      sorter: true,
      width: '20%',
      key: 'name'
    },
    {
      title: 'Description',
      dataIndex: 'attributes',
      hideInForm: true,
      key: 'attributes',
      render: (val) => <span>{`${val.product} ${val.version}${val.update ? ` ${val.update}` : ''}${val.edition ? ` ${val.edition}` : ''}`}</span>
    },
    {
      title: 'C',
      tip: 'Confidentiality',
      dataIndex: 'attributes',
      key: 'confidentiality',
      render: (val) => <span>{`${val.confidentiality}`}</span>
    },
    {
      title: 'I',
      tip: 'Integrity',
      dataIndex: 'attributes',
      key: 'integrity',
      render: (val) => <span>{`${val.integrity}`}</span>
    },
    {
      title: 'A',
      tip: 'Availability',
      dataIndex: 'attributes',
      key: 'availability',
      render: (val) => <span>{`${val.availability}`}</span>
    },
    {
      title: 'CPE',
      key: 'cpe',
      width: '20%',
      dataIndex: 'attributes',
      render: (val) => val.cpe ? <span>{val.cpe}</span> : <Button type='link'>CPE Match</Button>
    }
  ];
  const handleSelectFile = async (info) => {
    if (info.file.status === 'done') {
      try {
        const readData = await readXlsxFile(info.file.originFileObj)
        let tmp = {}
        let result = []
        console.log(readData.slice(5, readData.length));
        readData.slice(5, readData.length).map(row => {
          if (row[0]){
            if(Object.keys(tmp).length !== 0){
              result.push(tmp)
            }
            tmp = {
              asset_id: row[0],
              name: row[1],
              attributes: {
                [row[13]]: row[14],
              }
            }
          }else{
            tmp = {
              ...tmp,
              attributes: {
                ...tmp.attributes,
                [row[13]]: row[14]
              }
            }
          }
        })
        result.push(tmp)
        setAssets(result)
      } catch (e) {
        console.log(e);
      }
    }
  }

  return (
    <PageContainer>
      <ProTable
        // headerTitle="查询表格"
        actionRef={actionRef}
        rowKey="cwe_id"
        search={{
          labelWidth: 120,
        }}
        columns={columns}
        dataSource={assets}
        pagination={{
          pageSize: 10,
        }}
        toolbar={{
          settings: []
        }}
        locale={{
          emptyText: (
            <Empty>
              <Upload
                onChange={(info) => handleSelectFile(info)}
                accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                showUploadList={false}
              >
                <Button icon={<UploadOutlined />}>Upload</Button>
              </Upload>
            </Empty>
          )
        }}
        bordered
      />
    </PageContainer>
  );
};

export default Asset;
