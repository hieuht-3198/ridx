(self.webpackChunkant_design_pro=self.webpackChunkant_design_pro||[]).push([[852],{64317:function(y,C,r){"use strict";var t=r(22122),m=r(28991),O=r(81253),c=r(22270),l=r(67294),_=r(66758),p=r(39178),b=["fieldProps","children","params","proFieldProps","mode","valueEnum","request","showSearch","options"],v=["fieldProps","children","params","proFieldProps","mode","valueEnum","request","options"],D=l.forwardRef(function(n,P){var A=n.fieldProps,u=n.children,T=n.params,s=n.proFieldProps,e=n.mode,I=n.valueEnum,f=n.request,Z=n.showSearch,j=n.options,B=(0,O.Z)(n,b),W=(0,l.useContext)(_.Z);return l.createElement(p.Z,(0,t.Z)({mode:"edit",valueEnum:(0,c.h)(I),request:f,params:T,valueType:"select",filedConfig:{customLightMode:!0},fieldProps:(0,m.Z)({options:j,mode:e,showSearch:Z,getPopupContainer:W.getPopupContainer},A),ref:P,proFieldProps:s},B),u)}),d=l.forwardRef(function(n,P){var A=n.fieldProps,u=n.children,T=n.params,s=n.proFieldProps,e=n.mode,I=n.valueEnum,f=n.request,Z=n.options,j=(0,O.Z)(n,v),B=(0,m.Z)({options:Z,mode:e||"multiple",labelInValue:!0,showSearch:!0,showArrow:!1,autoClearSearchValue:!0,optionLabelProp:"label"},A),W=(0,l.useContext)(_.Z);return l.createElement(p.Z,(0,t.Z)({mode:"edit",valueEnum:(0,c.h)(I),request:f,params:T,valueType:"select",filedConfig:{customLightMode:!0},fieldProps:(0,m.Z)({getPopupContainer:W.getPopupContainer},B),ref:P,proFieldProps:s},j),u)}),o=D,i=d,a=o;a.SearchSelect=i,a.displayName="ProFormComponent",C.Z=a},5966:function(y,C,r){"use strict";var t=r(22122),m=r(81253),O=r(67294),c=r(39178),l=["fieldProps","proFieldProps"],_=["fieldProps","proFieldProps"],p="text",b=function(o){var i=o.fieldProps,a=o.proFieldProps,n=(0,m.Z)(o,l);return O.createElement(c.Z,(0,t.Z)({mode:"edit",valueType:p,fieldProps:i,filedConfig:{valueType:p},proFieldProps:a},n))},v=function(o){var i=o.fieldProps,a=o.proFieldProps,n=(0,m.Z)(o,_);return O.createElement(c.Z,(0,t.Z)({mode:"edit",valueType:"password",fieldProps:i,proFieldProps:a,filedConfig:{valueType:p}},n))},D=b;D.Password=v,D.displayName="ProFormComponent",C.Z=D},25185:function(y,C,r){"use strict";r.d(C,{UN:function(){return b},lu:function(){return v},G1:function(){return D}});var t=r(22385),m=r(61580),O=r(95357),c=r(8212),l=r(73171),_=r(85893),p=function(o){var i=o.icon,a=o.title,n=o.onClick;return(0,_.jsx)("a",{onClick:n,children:(0,_.jsx)(m.Z,{title:a,children:i})})},b=function(o){var i=o.title,a=o.onClick;return(0,_.jsx)(p,{icon:(0,_.jsx)(O.Z,{}),title:i||"Detail",onClick:a})},v=function(o){var i=o.title,a=o.onClick;return(0,_.jsx)(p,{icon:(0,_.jsx)(c.Z,{}),title:i||"Edit",onClick:a})},D=function(o){var i=o.title,a=o.onClick;return(0,_.jsx)(p,{icon:(0,_.jsx)(l.Z,{}),title:i||"Delete",onClick:a})};C.ZP=p},77555:function(y,C,r){"use strict";r.r(C);var t=r(57663),m=r(71577),O=r(11849),c=r(34792),l=r(48086),_=r(3182),p=r(71194),b=r(50146),v=r(2824),D=r(94043),d=r.n(D),o=r(49101),i=r(37476),a=r(5966),n=r(64317),P=r(51885),A=r(27596),u=r(67294),T=r(76208),s=r(44743),e=r(25185),I=r(32611),f=r(85893),Z=function(){var B=(0,u.useState)(!1),W=(0,v.Z)(B,2),Y=W[0],x=W[1],k=(0,u.useState)(!0),H=(0,v.Z)(k,2),F=H[0],w=H[1],G=(0,u.useState)({}),V=(0,v.Z)(G,2),$=V[0],N=V[1],K=(0,u.useRef)(),z=function(h){x(h),h||(w(!0),N({}))},J=[{title:"Name",dataIndex:"name",width:"50%"},{title:"Asset type",dataIndex:"part",valueType:"select",valueEnum:{o:{text:I.go},a:{text:I.$U},h:{text:I.iN}},width:"20%"},{title:"Created at",dataIndex:"created_at",width:"10%",hideInForm:!0,hideInSearch:!0,render:function(h){return(0,s.gu)(h)}},{title:"Updated at",dataIndex:"updated_at",width:"10%",hideInForm:!0,hideInSearch:!0,render:function(h){return(0,s.gu)(h)}},{title:"Action",dataIndex:"option",valueType:"option",width:"10%",render:function(h,g){return[(0,f.jsx)(e.lu,{onClick:function(){x(!0),w(!1),N(g)}},"edit"),(0,f.jsx)(e.G1,{onClick:function(){b.Z.confirm({title:"Delete asset",content:"Are you sure\uFF1F",okText:"Ok",cancelText:"Cancel",onOk:function(){var S=(0,_.Z)(d().mark(function E(){return d().wrap(function(U){for(;;)switch(U.prev=U.next){case 0:return U.next=2,Q(g.id);case 2:return U.abrupt("return",U.sent);case 3:case"end":return U.stop()}},E)}));function M(){return S.apply(this,arguments)}return M}()})}},"delete")]}}],Q=function(){var L=(0,_.Z)(d().mark(function h(g){var R;return d().wrap(function(M){for(;;)switch(M.prev=M.next){case 0:return M.prev=0,M.next=3,(0,T.mo)(g);case 3:R=M.sent,R&&(l.default.success("Delete successful!"),K.current&&K.current.reload()),M.next=10;break;case 7:M.prev=7,M.t0=M.catch(0),l.default.error("Delete failed!");case 10:case"end":return M.stop()}},h,null,[[0,7]])}));return function(g){return L.apply(this,arguments)}}(),X=function(){var L=(0,_.Z)(d().mark(function h(g){var R,S;return d().wrap(function(E){for(;;)switch(E.prev=E.next){case 0:if(R=(0,O.Z)({},g),!F){E.next=7;break}return E.next=4,(0,T.kI)(R);case 4:E.t0=E.sent,E.next=10;break;case 7:return E.next=9,(0,T.dQ)($.id,R);case 9:E.t0=E.sent;case 10:if(S=E.t0,!S){E.next=17;break}return l.default.success("".concat(F?"Add":"Edit"," asset successful!")),K.current&&K.current.reload(),w(!0),N({}),E.abrupt("return",!0);case 17:return l.default.error("".concat(F?"Add":"Edit"," asset failed!")),E.abrupt("return",!1);case 19:case"end":return E.stop()}},h)}));return function(g){return L.apply(this,arguments)}}();return(0,f.jsxs)(P.ZP,{children:[(0,f.jsx)(A.ZP,{actionRef:K,rowKey:"id",search:{labelWidth:120},request:T.Vh,columns:J,pagination:{pageSize:10},toolbar:{settings:[]},toolBarRender:function(){return[(0,f.jsxs)(m.Z,{type:"primary",onClick:function(){x(!0)},children:[(0,f.jsx)(o.Z,{})," Add"]},"primary")]},bordered:!0}),(0,f.jsxs)(i.Y,{title:"".concat(F?"Add":"Edit"," asset"),width:"600px",visible:Y,onVisibleChange:z,modalProps:{destroyOnClose:!0},onFinish:X,initialValues:$,layout:"vertical",children:[(0,f.jsx)(a.Z,{label:"Name",rules:[{required:!0}],name:"name"}),(0,f.jsx)(n.Z,{name:"part",label:"Asset type",valueEnum:{o:"OS",a:"APPLICATION",h:"HARDWARE"},placeholder:"Please select a asset type",rules:[{required:!0}]})]})]})};C.default=Z},76208:function(y,C,r){"use strict";r.d(C,{Vh:function(){return _},kI:function(){return b},dQ:function(){return D},mo:function(){return o}});var t=r(11849),m=r(3182),O=r(94043),c=r.n(O),l=r(64172);function _(a,n){return p.apply(this,arguments)}function p(){return p=(0,m.Z)(c().mark(function a(n,P){return c().wrap(function(u){for(;;)switch(u.prev=u.next){case 0:return u.abrupt("return",(0,l.ZP)("/api/assets",(0,t.Z)({method:"GET",params:(0,t.Z)({},n)},P||{})));case 1:case"end":return u.stop()}},a)})),p.apply(this,arguments)}function b(a,n){return v.apply(this,arguments)}function v(){return v=(0,m.Z)(c().mark(function a(n,P){return c().wrap(function(u){for(;;)switch(u.prev=u.next){case 0:return u.abrupt("return",(0,l.ZP)("/api/assets",(0,t.Z)({data:n,method:"POST"},P||{})));case 1:case"end":return u.stop()}},a)})),v.apply(this,arguments)}function D(a,n,P){return d.apply(this,arguments)}function d(){return d=(0,m.Z)(c().mark(function a(n,P,A){return c().wrap(function(T){for(;;)switch(T.prev=T.next){case 0:return T.abrupt("return",(0,l.ZP)("/api/assets/".concat(n),(0,t.Z)({data:P,method:"PUT"},A||{})));case 1:case"end":return T.stop()}},a)})),d.apply(this,arguments)}function o(a,n){return i.apply(this,arguments)}function i(){return i=(0,m.Z)(c().mark(function a(n,P){return c().wrap(function(u){for(;;)switch(u.prev=u.next){case 0:return u.abrupt("return",(0,l.ZP)("/api/assets/".concat(n),(0,t.Z)({method:"DELETE"},P||{})));case 1:case"end":return u.stop()}},a)})),i.apply(this,arguments)}},44743:function(y,C,r){"use strict";r.d(C,{w7:function(){return m},JS:function(){return O},Zb:function(){return c},gu:function(){return l},$U:function(){return p},O3:function(){return b},vh:function(){return v},rJ:function(){return D},zd:function(){return d},Ou:function(){return o},Vd:function(){return i},eX:function(){return a},jv:function(){return n},lf:function(){return P},xe:function(){return A},AC:function(){return u},Mc:function(){return T}});var t=r(32611),m=function(e){switch(e){case"OS":return"o";case"APPLICATION":return"a";case"HARDWARE":return"h";default:return}},O=function(e){switch(e){case"o":return"OS";case"a":return"APPLICATION";case"h":return"HARDWARE";default:return}},c=function(e){switch(e){case"HIGH":return 3;case"MEDIUM":return 2;case"LOW":return 1;default:return}},l=function(e){return e.substring(0,10)},_=function(e){return e.replace(/\w\S*/g,function(I){return I.charAt(0).toUpperCase()+I.substr(1).toLowerCase()})},p=function(e){return e>=9?["Critical",t.jv]:e>=7?["High",t.U1]:e>=4?["Medium",t.WY]:["Low",t.q6]},b=function(e){return e==="Critical"?t.jv:e==="High"?t.U1:e==="Medium"?t.WY:t.q6},v=function(e){return e<=1.8?["Negligible",1]:e<=3.6?["Low",2]:e<=5.4?["Moderate",3]:e<=7.2?["Significant",4]:["Catastrophic",5]},D=function(e){return e<=.2?["Improbable",1]:e<=.4?["Remote",2]:e<=.6?["Occsional",3]:e<=.8?["Probale",4]:["Frequent",5]},d=function(e,I){var f=e*I;return f>12?["Critical",t.jv,4]:f>7?["High",t.U1,3]:f>3?["Medium",t.WY,2]:["Low",t.q6,1]},o=function(e){return e===4?"Critical":e===3?"High":e===2?"Medium":e===1?"Low":""},i=function(e){return e===5?"Catastrophic":e===4?"Significant":e===3?"Moderate":e===2?"Low":e===1?"Negligible":""},a=function(e){return e===5?"Frequent":e===4?"Probale":e===3?"Occsional":e===2?"Remote":e===1?"Improbable":""},n=function(e){return Math.round(e*100)/100},P=function(e){return e<=.25?["Low",t.q6]:e<=.5?["Medium",t.WY]:e<=.75?["High",t.U1]:["Critical",t.jv]},A=function(e){return e==="Negligible"?t.Fe:e==="Low"?t.q6:e==="Moderate"?t.WY:e==="Significant"?t.U1:t.jv},u=function(e){return e==="Improbable"?t.Fe:e==="Low"?t.q6:e==="Occsional"?t.WY:e==="Significant"?t.U1:t.jv},T=function(e){return e==="None"?t.Fe:e==="Low"?t.q6:e==="Medium"?t.WY:e==="High"?t.U1:t.jv}}}]);