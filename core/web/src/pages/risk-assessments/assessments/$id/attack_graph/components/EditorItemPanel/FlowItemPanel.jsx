import { Item, ItemPanel } from 'gg-editor';
import { Card } from 'antd';
import styles from './index.less';

const FlowItemPanel = () => (
  <ItemPanel className={styles.itemPanel}>
    <Card bordered={false}>
      <Item
        type="node"
        size="72*72"
        shape="flow-circle"
        model={{
          color: '#FA8C16',
          label: 'Threat',
          is_attacker: true,
        }}
        src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcKICAgd2lkdGg9IjgwIgogICBoZWlnaHQ9IjgwIgogICB2ZXJzaW9uPSIxLjEiCiAgIGlkPSJzdmcyOCIKICAgc29kaXBvZGk6ZG9jbmFtZT0iYXR0YWNrLnN2ZyIKICAgaW5rc2NhcGU6dmVyc2lvbj0iMS4xLjIgKDE6MS4xKzIwMjIwMjA1MDk1MCswYTAwY2Y1MzM5KSIKICAgeG1sbnM6aW5rc2NhcGU9Imh0dHA6Ly93d3cuaW5rc2NhcGUub3JnL25hbWVzcGFjZXMvaW5rc2NhcGUiCiAgIHhtbG5zOnNvZGlwb2RpPSJodHRwOi8vc29kaXBvZGkuc291cmNlZm9yZ2UubmV0L0RURC9zb2RpcG9kaS0wLmR0ZCIKICAgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiCiAgIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgeG1sbnM6c3ZnPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHNvZGlwb2RpOm5hbWVkdmlldwogICAgIGlkPSJuYW1lZHZpZXczMCIKICAgICBwYWdlY29sb3I9IiNmZmZmZmYiCiAgICAgYm9yZGVyY29sb3I9IiM2NjY2NjYiCiAgICAgYm9yZGVyb3BhY2l0eT0iMS4wIgogICAgIGlua3NjYXBlOnBhZ2VzaGFkb3c9IjIiCiAgICAgaW5rc2NhcGU6cGFnZW9wYWNpdHk9IjAuMCIKICAgICBpbmtzY2FwZTpwYWdlY2hlY2tlcmJvYXJkPSIwIgogICAgIHNob3dncmlkPSJmYWxzZSIKICAgICBpbmtzY2FwZTp6b29tPSI2LjM4NzUiCiAgICAgaW5rc2NhcGU6Y3g9IjU0LjI0NjU3NSIKICAgICBpbmtzY2FwZTpjeT0iNDYuNjUzNjIiCiAgICAgaW5rc2NhcGU6d2luZG93LXdpZHRoPSIxMzEwIgogICAgIGlua3NjYXBlOndpbmRvdy1oZWlnaHQ9IjcwNCIKICAgICBpbmtzY2FwZTp3aW5kb3cteD0iNTYiCiAgICAgaW5rc2NhcGU6d2luZG93LXk9IjI3IgogICAgIGlua3NjYXBlOndpbmRvdy1tYXhpbWl6ZWQ9IjEiCiAgICAgaW5rc2NhcGU6Y3VycmVudC1sYXllcj0iZzI2IiAvPgogIDxkZWZzCiAgICAgaWQ9ImRlZnMxMiI+CiAgICA8Y2lyY2xlCiAgICAgICBpZD0iYiIKICAgICAgIGN4PSIzNiIKICAgICAgIGN5PSIzNiIKICAgICAgIHI9IjM2IiAvPgogICAgPGZpbHRlcgogICAgICAgeD0iLTAuMDY2NjY2NjY3IgogICAgICAgeT0iLTAuMDY2NjY2NjY3IgogICAgICAgd2lkdGg9IjEuMTMzMzMzMyIKICAgICAgIGhlaWdodD0iMS4xNjExMTExIgogICAgICAgZmlsdGVyVW5pdHM9Im9iamVjdEJvdW5kaW5nQm94IgogICAgICAgaWQ9ImEiPgogICAgICA8ZmVPZmZzZXQKICAgICAgICAgZHk9IjIiCiAgICAgICAgIGluPSJTb3VyY2VBbHBoYSIKICAgICAgICAgcmVzdWx0PSJzaGFkb3dPZmZzZXRPdXRlcjEiCiAgICAgICAgIGlkPSJmZU9mZnNldDMiIC8+CiAgICAgIDxmZUdhdXNzaWFuQmx1cgogICAgICAgICBzdGREZXZpYXRpb249IjIiCiAgICAgICAgIGluPSJzaGFkb3dPZmZzZXRPdXRlcjEiCiAgICAgICAgIHJlc3VsdD0ic2hhZG93Qmx1ck91dGVyMSIKICAgICAgICAgaWQ9ImZlR2F1c3NpYW5CbHVyNSIgLz4KICAgICAgPGZlQ29tcG9zaXRlCiAgICAgICAgIGluPSJzaGFkb3dCbHVyT3V0ZXIxIgogICAgICAgICBpbjI9IlNvdXJjZUFscGhhIgogICAgICAgICBvcGVyYXRvcj0ib3V0IgogICAgICAgICByZXN1bHQ9InNoYWRvd0JsdXJPdXRlcjEiCiAgICAgICAgIGlkPSJmZUNvbXBvc2l0ZTciIC8+CiAgICAgIDxmZUNvbG9yTWF0cml4CiAgICAgICAgIHZhbHVlcz0iMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMC4wNCAwIgogICAgICAgICBpbj0ic2hhZG93Qmx1ck91dGVyMSIKICAgICAgICAgaWQ9ImZlQ29sb3JNYXRyaXg5IiAvPgogICAgPC9maWx0ZXI+CiAgPC9kZWZzPgogIDxnCiAgICAgZmlsbD0ibm9uZSIKICAgICBmaWxsLXJ1bGU9ImV2ZW5vZGQiCiAgICAgaWQ9ImcyNiI+CiAgICA8ZwogICAgICAgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNCAyKSIKICAgICAgIGlkPSJnMjAiPgogICAgICA8dXNlCiAgICAgICAgIGZpbGw9IiMwMDAiCiAgICAgICAgIGZpbHRlcj0idXJsKCNhKSIKICAgICAgICAgeGxpbms6aHJlZj0iI2IiCiAgICAgICAgIGlkPSJ1c2UxNCIgLz4KICAgICAgPHVzZQogICAgICAgICBmaWxsLW9wYWNpdHk9Ii45MiIKICAgICAgICAgZmlsbD0iI0ZGRjJFOCIKICAgICAgICAgeGxpbms6aHJlZj0iI2IiCiAgICAgICAgIGlkPSJ1c2UxNiIgLz4KICAgICAgPGNpcmNsZQogICAgICAgICBzdHJva2U9IiNGRkMwNjkiCiAgICAgICAgIGN4PSIzNiIKICAgICAgICAgY3k9IjM2IgogICAgICAgICByPSIzNS41IgogICAgICAgICBpZD0iY2lyY2xlMTgiIC8+CiAgICA8L2c+CiAgICA8dGV4dAogICAgICAgZm9udC1mYW1pbHk9IlBpbmdGYW5nU0MtUmVndWxhciwgJ1BpbmdGYW5nIFNDJyIKICAgICAgIGZvbnQtc2l6ZT0iMTJweCIKICAgICAgIGZpbGw9IiMwMDAwMDAiCiAgICAgICBmaWxsLW9wYWNpdHk9IjAuNjUiCiAgICAgICBpZD0idGV4dDI0IgogICAgICAgeD0iLTIuMjc5MTYyOSIKICAgICAgIHk9IjIuOTk4MTI5MSI+PHRzcGFuCiAgICAgICAgIHg9IjIwLjcyMDgzOSIKICAgICAgICAgeT0iNDMuOTk4MTMxIgogICAgICAgICBpZD0idHNwYW4yMiI+VGhyZWF0PC90c3Bhbj48L3RleHQ+CiAgPC9nPgo8L3N2Zz4K"
      />
      {/* <Item
        type="node"
        size="100*48"
        shape="flow-rect"
        model={{
          color: '#1890FF',
          label: 'Countermeasure',
        }}
        src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODgiIGhlaWdodD0iNTYiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiPjxkZWZzPjxyZWN0IGlkPSJiIiB4PSIwIiB5PSIwIiB3aWR0aD0iODAiIGhlaWdodD0iNDgiIHJ4PSI0Ii8+PGZpbHRlciB4PSItOC44JSIgeT0iLTEwLjQlIiB3aWR0aD0iMTE3LjUlIiBoZWlnaHQ9IjEyOS4yJSIgZmlsdGVyVW5pdHM9Im9iamVjdEJvdW5kaW5nQm94IiBpZD0iYSI+PGZlT2Zmc2V0IGR5PSIyIiBpbj0iU291cmNlQWxwaGEiIHJlc3VsdD0ic2hhZG93T2Zmc2V0T3V0ZXIxIi8+PGZlR2F1c3NpYW5CbHVyIHN0ZERldmlhdGlvbj0iMiIgaW49InNoYWRvd09mZnNldE91dGVyMSIgcmVzdWx0PSJzaGFkb3dCbHVyT3V0ZXIxIi8+PGZlQ29tcG9zaXRlIGluPSJzaGFkb3dCbHVyT3V0ZXIxIiBpbjI9IlNvdXJjZUFscGhhIiBvcGVyYXRvcj0ib3V0IiByZXN1bHQ9InNoYWRvd0JsdXJPdXRlcjEiLz48ZmVDb2xvck1hdHJpeCB2YWx1ZXM9IjAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAuMDQgMCIgaW49InNoYWRvd0JsdXJPdXRlcjEiLz48L2ZpbHRlcj48L2RlZnM+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSg0IDIpIj48dXNlIGZpbGw9IiMwMDAiIGZpbHRlcj0idXJsKCNhKSIgeGxpbms6aHJlZj0iI2IiLz48dXNlIGZpbGwtb3BhY2l0eT0iLjkyIiBmaWxsPSIjRTZGN0ZGIiB4bGluazpocmVmPSIjYiIvPjxyZWN0IHN0cm9rZT0iIzE4OTBGRiIgeD0iLjUiIHk9Ii41IiB3aWR0aD0iNzkiIGhlaWdodD0iNDciIHJ4PSI0Ii8+PC9nPjx0ZXh0IGZvbnQtZmFtaWx5PSJQaW5nRmFuZ1NDLVJlZ3VsYXIsIFBpbmdGYW5nIFNDIiBmb250LXNpemU9IjEyIiBmaWxsPSIjMDAwIiBmaWxsLW9wYWNpdHk9Ii42NSIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNCAyKSI+PHRzcGFuIHg9IjIxIiB5PSIyOSI+Tm9ybWFsPC90c3Bhbj48L3RleHQ+PC9nPjwvc3ZnPg=="
      /> */}
      <Item
        type="node"
        size="100*48"
        shape="flow-capsule"
        model={{
          color: '#722ED1',
          label: 'CVE',
          is_attacker: false,
        }}
        src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcKICAgd2lkdGg9Ijg4IgogICBoZWlnaHQ9IjU2IgogICB2ZXJzaW9uPSIxLjEiCiAgIGlkPSJzdmcyOCIKICAgc29kaXBvZGk6ZG9jbmFtZT0iY3ZlLnN2ZyIKICAgaW5rc2NhcGU6dmVyc2lvbj0iMS4xLjIgKDE6MS4xKzIwMjIwMjA1MDk1MCswYTAwY2Y1MzM5KSIKICAgeG1sbnM6aW5rc2NhcGU9Imh0dHA6Ly93d3cuaW5rc2NhcGUub3JnL25hbWVzcGFjZXMvaW5rc2NhcGUiCiAgIHhtbG5zOnNvZGlwb2RpPSJodHRwOi8vc29kaXBvZGkuc291cmNlZm9yZ2UubmV0L0RURC9zb2RpcG9kaS0wLmR0ZCIKICAgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiCiAgIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgeG1sbnM6c3ZnPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHNvZGlwb2RpOm5hbWVkdmlldwogICAgIGlkPSJuYW1lZHZpZXczMCIKICAgICBwYWdlY29sb3I9IiNmZmZmZmYiCiAgICAgYm9yZGVyY29sb3I9IiM2NjY2NjYiCiAgICAgYm9yZGVyb3BhY2l0eT0iMS4wIgogICAgIGlua3NjYXBlOnBhZ2VzaGFkb3c9IjIiCiAgICAgaW5rc2NhcGU6cGFnZW9wYWNpdHk9IjAuMCIKICAgICBpbmtzY2FwZTpwYWdlY2hlY2tlcmJvYXJkPSIwIgogICAgIHNob3dncmlkPSJmYWxzZSIKICAgICBpbmtzY2FwZTp6b29tPSI5LjEyNSIKICAgICBpbmtzY2FwZTpjeD0iNjUuNjk4NjMiCiAgICAgaW5rc2NhcGU6Y3k9IjI4LjA1NDc5NSIKICAgICBpbmtzY2FwZTp3aW5kb3ctd2lkdGg9IjEzMTAiCiAgICAgaW5rc2NhcGU6d2luZG93LWhlaWdodD0iNzA0IgogICAgIGlua3NjYXBlOndpbmRvdy14PSI1NiIKICAgICBpbmtzY2FwZTp3aW5kb3cteT0iMjciCiAgICAgaW5rc2NhcGU6d2luZG93LW1heGltaXplZD0iMSIKICAgICBpbmtzY2FwZTpjdXJyZW50LWxheWVyPSJnMjYiIC8+CiAgPGRlZnMKICAgICBpZD0iZGVmczEyIj4KICAgIDxyZWN0CiAgICAgICBpZD0iYiIKICAgICAgIHg9IjAiCiAgICAgICB5PSIwIgogICAgICAgd2lkdGg9IjgwIgogICAgICAgaGVpZ2h0PSI0OCIKICAgICAgIHJ4PSIyNCIgLz4KICAgIDxmaWx0ZXIKICAgICAgIHg9Ii0wLjA2IgogICAgICAgeT0iLTAuMSIKICAgICAgIHdpZHRoPSIxLjEyIgogICAgICAgaGVpZ2h0PSIxLjI0MTY2NjciCiAgICAgICBmaWx0ZXJVbml0cz0ib2JqZWN0Qm91bmRpbmdCb3giCiAgICAgICBpZD0iYSI+CiAgICAgIDxmZU9mZnNldAogICAgICAgICBkeT0iMiIKICAgICAgICAgaW49IlNvdXJjZUFscGhhIgogICAgICAgICByZXN1bHQ9InNoYWRvd09mZnNldE91dGVyMSIKICAgICAgICAgaWQ9ImZlT2Zmc2V0MyIgLz4KICAgICAgPGZlR2F1c3NpYW5CbHVyCiAgICAgICAgIHN0ZERldmlhdGlvbj0iMiIKICAgICAgICAgaW49InNoYWRvd09mZnNldE91dGVyMSIKICAgICAgICAgcmVzdWx0PSJzaGFkb3dCbHVyT3V0ZXIxIgogICAgICAgICBpZD0iZmVHYXVzc2lhbkJsdXI1IiAvPgogICAgICA8ZmVDb21wb3NpdGUKICAgICAgICAgaW49InNoYWRvd0JsdXJPdXRlcjEiCiAgICAgICAgIGluMj0iU291cmNlQWxwaGEiCiAgICAgICAgIG9wZXJhdG9yPSJvdXQiCiAgICAgICAgIHJlc3VsdD0ic2hhZG93Qmx1ck91dGVyMSIKICAgICAgICAgaWQ9ImZlQ29tcG9zaXRlNyIgLz4KICAgICAgPGZlQ29sb3JNYXRyaXgKICAgICAgICAgdmFsdWVzPSIwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwLjA0IDAiCiAgICAgICAgIGluPSJzaGFkb3dCbHVyT3V0ZXIxIgogICAgICAgICBpZD0iZmVDb2xvck1hdHJpeDkiIC8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPGcKICAgICBmaWxsPSJub25lIgogICAgIGZpbGwtcnVsZT0iZXZlbm9kZCIKICAgICBpZD0iZzI2Ij4KICAgIDxnCiAgICAgICB0cmFuc2Zvcm09InRyYW5zbGF0ZSg0IDIpIgogICAgICAgaWQ9ImcyMCI+CiAgICAgIDx1c2UKICAgICAgICAgZmlsbD0iIzAwMCIKICAgICAgICAgZmlsdGVyPSJ1cmwoI2EpIgogICAgICAgICB4bGluazpocmVmPSIjYiIKICAgICAgICAgaWQ9InVzZTE0IiAvPgogICAgICA8dXNlCiAgICAgICAgIGZpbGwtb3BhY2l0eT0iLjkyIgogICAgICAgICBmaWxsPSIjRjlGMEZGIgogICAgICAgICB4bGluazpocmVmPSIjYiIKICAgICAgICAgaWQ9InVzZTE2IiAvPgogICAgICA8cmVjdAogICAgICAgICBzdHJva2U9IiNCMzdGRUIiCiAgICAgICAgIHg9Ii41IgogICAgICAgICB5PSIuNSIKICAgICAgICAgd2lkdGg9Ijc5IgogICAgICAgICBoZWlnaHQ9IjQ3IgogICAgICAgICByeD0iMjMuNSIKICAgICAgICAgaWQ9InJlY3QxOCIgLz4KICAgIDwvZz4KICAgIDx0ZXh0CiAgICAgICBmb250LWZhbWlseT0iUGluZ0ZhbmdTQy1SZWd1bGFyLCAnUGluZ0ZhbmcgU0MnIgogICAgICAgZm9udC1zaXplPSIxMnB4IgogICAgICAgZmlsbD0iIzAwMDAwMCIKICAgICAgIGZpbGwtb3BhY2l0eT0iMC42NSIKICAgICAgIGlkPSJ0ZXh0MjQiCiAgICAgICB4PSI3LjUxNDIzMDMiCiAgICAgICB5PSIwLjg5NzU2Nzk5Ij48dHNwYW4KICAgICAgICAgeD0iMzEuNTE0MjMxIgogICAgICAgICB5PSIyOS44OTc1NjgiCiAgICAgICAgIGlkPSJ0c3BhbjIyIj5DVkU8L3RzcGFuPjwvdGV4dD4KICA8L2c+Cjwvc3ZnPgo="
      />
    </Card>
  </ItemPanel>
);

export default FlowItemPanel;
