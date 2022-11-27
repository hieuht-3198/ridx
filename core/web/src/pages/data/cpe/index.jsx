import { PageContainer } from '@ant-design/pro-layout';
import ProTable from '@ant-design/pro-table';
import React, { useRef } from 'react';
import { getCPEs } from './service';


const CVE = () => {
  const actionRef = useRef();

  const columns = [
    {
      title: 'CWE ID',
      dataIndex: 'cve_id',
      sorter: true,
      width: '10%',
    },
    {
      title: 'CWE Name',
      dataIndex: 'cwe_name',
      sorter: true,
      width: '30%',
    },
    {
      title: 'Description',
      dataIndex: 'description',
      hideInForm: true,
      hideInSearch: true, 
      // ellipsis: true, // oneline - tooltip khi over
    },
  ];
  return (
    <PageContainer>
      <ProTable
        // headerTitle="查询表格"
        actionRef={actionRef}
        rowKey="cve_id"
        search={{
          labelWidth: 120,
        }}
        request={getCPEs}
        columns={columns}
        pagination={{
          pageSize: 10,
        }}
        toolbar={{
          settings: []
        }}
        bordered        
      />
    </PageContainer>
  );
};

export default CVE;
