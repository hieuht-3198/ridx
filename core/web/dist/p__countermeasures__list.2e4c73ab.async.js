(self.webpackChunkant_design_pro=self.webpackChunkant_design_pro||[]).push([[184],{5966:function(W,D,r){"use strict";var n=r(22122),v=r(81253),b=r(67294),s=r(39178),m=["fieldProps","proFieldProps"],p=["fieldProps","proFieldProps"],c="text",O=function(u){var a=u.fieldProps,t=u.proFieldProps,o=(0,v.Z)(u,m);return b.createElement(s.Z,(0,n.Z)({mode:"edit",valueType:c,fieldProps:a,filedConfig:{valueType:c},proFieldProps:t},o))},E=function(u){var a=u.fieldProps,t=u.proFieldProps,o=(0,v.Z)(u,p);return b.createElement(s.Z,(0,n.Z)({mode:"edit",valueType:"password",fieldProps:a,proFieldProps:t,filedConfig:{valueType:c}},o))},M=O;M.Password=E,M.displayName="ProFormComponent",D.Z=M},25185:function(W,D,r){"use strict";r.d(D,{UN:function(){return O},lu:function(){return E},G1:function(){return M}});var n=r(22385),v=r(61580),b=r(95357),s=r(8212),m=r(73171),p=r(85893),c=function(u){var a=u.icon,t=u.title,o=u.onClick;return(0,p.jsx)("a",{onClick:o,children:(0,p.jsx)(v.Z,{title:t,children:a})})},O=function(u){var a=u.title,t=u.onClick;return(0,p.jsx)(c,{icon:(0,p.jsx)(b.Z,{}),title:a||"Detail",onClick:t})},E=function(u){var a=u.title,t=u.onClick;return(0,p.jsx)(c,{icon:(0,p.jsx)(s.Z,{}),title:a||"Edit",onClick:t})},M=function(u){var a=u.title,t=u.onClick;return(0,p.jsx)(c,{icon:(0,p.jsx)(m.Z,{}),title:a||"Delete",onClick:t})};D.ZP=c},29628:function(W,D,r){"use strict";r.r(D);var n=r(57663),v=r(71577),b=r(34792),s=r(48086),m=r(3182),p=r(71194),c=r(50146),O=r(11849),E=r(2824),M=r(94043),_=r.n(M),u=r(49101),a=r(37476),t=r(5966),o=r(51885),T=r(27596),h=r(67294),i=r(40727),I=r(44743),l=r(25185),e=r(85893),L=function(){var k=(0,h.useState)(!1),S=(0,E.Z)(k,2),H=S[0],B=S[1],G=(0,h.useState)(!0),F=(0,E.Z)(G,2),Z=F[0],K=F[1],V=(0,h.useState)({}),x=(0,E.Z)(V,2),N=x[0],w=x[1],Y=function(f){B(f),f||(K(!0),w({}))},R=(0,h.useRef)(),$=[{title:"Name",dataIndex:"name",width:"40%"},{title:"Cover CVE",dataIndex:"cover_cves",width:"30%",render:function(f,A){return(0,e.jsx)("ul",{children:A.cover_cves.map(function(P){return(0,e.jsx)("li",{children:P},P)})})}},{title:"Created at",dataIndex:"created_at",width:"10%",hideInForm:!0,hideInSearch:!0,render:function(f){return(0,I.gu)(f)}},{title:"Updated at",dataIndex:"updated_at",width:"10%",hideInForm:!0,hideInSearch:!0,render:function(f){return(0,I.gu)(f)}},{title:"Action",dataIndex:"option",valueType:"option",width:"10%",render:function(f,A){return[(0,e.jsx)(l.lu,{onClick:function(){B(!0),K(!1),w((0,O.Z)((0,O.Z)({},A),{},{cover_cves:A.cover_cves.join(",")}))}},"edit"),(0,e.jsx)(l.G1,{onClick:function(){c.Z.confirm({title:"Delete countermeasure",content:"Are you sure\uFF1F",okText:"Ok",cancelText:"Cancel",onOk:function(){var U=(0,m.Z)(_().mark(function d(){return _().wrap(function(y){for(;;)switch(y.prev=y.next){case 0:return y.next=2,z(A.id);case 2:return y.abrupt("return",y.sent);case 3:case"end":return y.stop()}},d)}));function C(){return U.apply(this,arguments)}return C}()})}},"delete")]}}],z=function(){var g=(0,m.Z)(_().mark(function f(A){var P;return _().wrap(function(C){for(;;)switch(C.prev=C.next){case 0:return C.prev=0,C.next=3,(0,i.ah)(A);case 3:P=C.sent,P&&(s.default.success("Delete successful!"),R.current&&R.current.reload()),C.next=10;break;case 7:C.prev=7,C.t0=C.catch(0),s.default.error("Delete failed!");case 10:case"end":return C.stop()}},f,null,[[0,7]])}));return function(A){return g.apply(this,arguments)}}(),J=function(){var g=(0,m.Z)(_().mark(function f(A){var P,U;return _().wrap(function(d){for(;;)switch(d.prev=d.next){case 0:if(P=(0,O.Z)({},A),P.cover_cves=P.cover_cves.split(","),!Z){d.next=8;break}return d.next=5,(0,i.qc)(P);case 5:d.t0=d.sent,d.next=11;break;case 8:return d.next=10,(0,i.g5)(N.id,P);case 10:d.t0=d.sent;case 11:if(U=d.t0,!U){d.next=18;break}return s.default.success("".concat(Z?"Add":"Edit"," countermeasure successful!")),R.current&&R.current.reload(),K(!0),w({}),d.abrupt("return",!0);case 18:return s.default.error("".concat(Z?"Add":"Edit"," countermeasure failed!")),d.abrupt("return",!1);case 20:case"end":return d.stop()}},f)}));return function(A){return g.apply(this,arguments)}}();return(0,e.jsxs)(o.ZP,{children:[(0,e.jsx)(T.ZP,{actionRef:R,rowKey:"id",search:{labelWidth:120},request:i.Gl,columns:$,pagination:{pageSize:10},toolbar:{settings:[]},toolBarRender:function(){return[(0,e.jsxs)(v.Z,{type:"primary",onClick:function(){B(!0)},children:[(0,e.jsx)(u.Z,{})," Add"]},"primary")]},bordered:!0}),(0,e.jsxs)(a.Y,{title:"".concat(Z?"Add":"Edit"," countermeasure"),width:"600px",visible:H,onVisibleChange:Y,modalProps:{destroyOnClose:!0},onFinish:J,initialValues:N,layout:"vertical",children:[(0,e.jsx)(t.Z,{label:"Name",rules:[{required:!0}],name:"name"}),(0,e.jsx)(t.Z,{label:"Cover CVE",rules:[{required:!0}],name:"cover_cves"})]})]})};D.default=L},40727:function(W,D,r){"use strict";r.d(D,{Gl:function(){return p},qc:function(){return O},g5:function(){return M},ah:function(){return u}});var n=r(11849),v=r(3182),b=r(94043),s=r.n(b),m=r(64172);function p(t,o){return c.apply(this,arguments)}function c(){return c=(0,v.Z)(s().mark(function t(o,T){return s().wrap(function(i){for(;;)switch(i.prev=i.next){case 0:return i.abrupt("return",(0,m.ZP)("/api/countermeasures",(0,n.Z)({method:"GET",params:(0,n.Z)({},o)},T||{})));case 1:case"end":return i.stop()}},t)})),c.apply(this,arguments)}function O(t,o){return E.apply(this,arguments)}function E(){return E=(0,v.Z)(s().mark(function t(o,T){return s().wrap(function(i){for(;;)switch(i.prev=i.next){case 0:return i.abrupt("return",(0,m.ZP)("/api/countermeasures",(0,n.Z)({data:o,method:"POST"},T||{})));case 1:case"end":return i.stop()}},t)})),E.apply(this,arguments)}function M(t,o,T){return _.apply(this,arguments)}function _(){return _=(0,v.Z)(s().mark(function t(o,T,h){return s().wrap(function(I){for(;;)switch(I.prev=I.next){case 0:return I.abrupt("return",(0,m.ZP)("/api/countermeasures/".concat(o),(0,n.Z)({data:T,method:"PUT"},h||{})));case 1:case"end":return I.stop()}},t)})),_.apply(this,arguments)}function u(t,o){return a.apply(this,arguments)}function a(){return a=(0,v.Z)(s().mark(function t(o,T){return s().wrap(function(i){for(;;)switch(i.prev=i.next){case 0:return i.abrupt("return",(0,m.ZP)("/api/countermeasures/".concat(o),(0,n.Z)({method:"DELETE"},T||{})));case 1:case"end":return i.stop()}},t)})),a.apply(this,arguments)}},44743:function(W,D,r){"use strict";r.d(D,{w7:function(){return v},JS:function(){return b},Zb:function(){return s},gu:function(){return m},$U:function(){return c},O3:function(){return O},vh:function(){return E},rJ:function(){return M},zd:function(){return _},Ou:function(){return u},Vd:function(){return a},eX:function(){return t},jv:function(){return o},lf:function(){return T},xe:function(){return h},AC:function(){return i},Mc:function(){return I}});var n=r(32611),v=function(e){switch(e){case"OS":return"o";case"APPLICATION":return"a";case"HARDWARE":return"h";default:return}},b=function(e){switch(e){case"o":return"OS";case"a":return"APPLICATION";case"h":return"HARDWARE";default:return}},s=function(e){switch(e){case"HIGH":return 3;case"MEDIUM":return 2;case"LOW":return 1;default:return}},m=function(e){return e.substring(0,10)},p=function(e){return e.replace(/\w\S*/g,function(L){return L.charAt(0).toUpperCase()+L.substr(1).toLowerCase()})},c=function(e){return e>=9?["Critical",n.jv]:e>=7?["High",n.U1]:e>=4?["Medium",n.WY]:["Low",n.q6]},O=function(e){return e==="Critical"?n.jv:e==="High"?n.U1:e==="Medium"?n.WY:n.q6},E=function(e){return e<=1.8?["Negligible",1]:e<=3.6?["Low",2]:e<=5.4?["Moderate",3]:e<=7.2?["Significant",4]:["Catastrophic",5]},M=function(e){return e<=.2?["Improbable",1]:e<=.4?["Remote",2]:e<=.6?["Occsional",3]:e<=.8?["Probale",4]:["Frequent",5]},_=function(e,L){var j=e*L;return j>12?["Critical",n.jv,4]:j>7?["High",n.U1,3]:j>3?["Medium",n.WY,2]:["Low",n.q6,1]},u=function(e){return e===4?"Critical":e===3?"High":e===2?"Medium":e===1?"Low":""},a=function(e){return e===5?"Catastrophic":e===4?"Significant":e===3?"Moderate":e===2?"Low":e===1?"Negligible":""},t=function(e){return e===5?"Frequent":e===4?"Probale":e===3?"Occsional":e===2?"Remote":e===1?"Improbable":""},o=function(e){return Math.round(e*100)/100},T=function(e){return e<=.25?["Low",n.q6]:e<=.5?["Medium",n.WY]:e<=.75?["High",n.U1]:["Critical",n.jv]},h=function(e){return e==="Negligible"?n.Fe:e==="Low"?n.q6:e==="Moderate"?n.WY:e==="Significant"?n.U1:n.jv},i=function(e){return e==="Improbable"?n.Fe:e==="Low"?n.q6:e==="Occsional"?n.WY:e==="Significant"?n.U1:n.jv},I=function(e){return e==="None"?n.Fe:e==="Low"?n.q6:e==="Medium"?n.WY:e==="High"?n.U1:n.jv}}}]);
