(self.webpackChunkant_design_pro=self.webpackChunkant_design_pro||[]).push([[459],{52953:function(){},13277:function(){},76731:function(re,j,t){"use strict";var r=t(71153),I=t(60331),D=t(44743),T=t(85893),N=function(s){var h=s.cvss;if(h){var R=(0,D.$U)(h);return(0,T.jsx)(I.Z,{color:R[1],children:(0,T.jsx)("b",{style:{color:"black"},children:"".concat(h," ").concat(R[0])})})}return"(not available)"};j.Z=N},73041:function(re,j,t){"use strict";t.r(j),t.d(j,{default:function(){return e}});var r=t(58024),I=t(91894),D=t(98858),T=t(4914),N=t(3182),Y=t(2824),s=t(402),h=t(97272),R=t(94043),$=t.n(R),X=t(76731),_=t(51885),g=t(67294),A=t(11849),ee=t(64172);function k(u,d,c){return V.apply(this,arguments)}function V(){return V=(0,N.Z)($().mark(function u(d,c,C){return $().wrap(function(a){for(;;)switch(a.prev=a.next){case 0:return a.abrupt("return",(0,ee.ZP)("/api/cves/".concat(d),(0,A.Z)({method:"GET",params:(0,A.Z)({},c)},C||{})));case 1:case"end":return a.stop()}},u)})),V.apply(this,arguments)}var m=t(85893),Q=h.Z.Paragraph,y=function(d){var c,C,U,a,n,l,i,p,f,v,S,E,P,x,Z,L,O,b,B=d==null||(c=d.match)===null||c===void 0?void 0:c.params,W=B.id,z=(0,g.useState)({}),w=(0,Y.Z)(z,2),o=w[0],M=w[1],G=(0,g.useState)(!0),K=(0,Y.Z)(G,2),q=K[0],te=K[1],F=function(){var ae=(0,N.Z)($().mark(function ne(){var H;return $().wrap(function(oe){for(;;)switch(oe.prev=oe.next){case 0:return oe.next=2,k(W);case 2:H=oe.sent,H&&M(H.data);case 4:case"end":return oe.stop()}},ne)}));return function(){return ae.apply(this,arguments)}}();return(0,g.useEffect)(function(){F()},[]),(0,m.jsx)(_.ZP,{header:{title:"CVE Detail"},content:(0,m.jsx)(T.Z,{column:1,style:{marginBottom:-16},children:(0,m.jsx)(T.Z.Item,{label:"CVE ID",children:(0,m.jsx)("a",{children:W})})}),children:(0,m.jsx)(I.Z,{children:(0,m.jsxs)(T.Z,{title:"CVE info",column:1,children:[(0,m.jsx)(T.Z.Item,{label:"CVE ID",children:o==null?void 0:o.cve_id}),(0,m.jsx)(T.Z.Item,{label:"CWE ID",children:(0,m.jsx)("a",{onClick:function(){window.open("/data/cwe/".concat(o==null?void 0:o.cwe_id),"_blank")},children:o==null?void 0:o.cwe_id})}),(0,m.jsx)(T.Z.Item,{label:"Description",children:(0,m.jsx)(Q,{ellipsis:q?{rows:3,expandable:!0,symbol:"more"}:!1,children:o==null?void 0:o.description})}),(0,m.jsx)(T.Z.Item,{label:"CVSS V2",children:o!=null&&(C=o.impact)!==null&&C!==void 0&&(U=C.baseMetricV2)!==null&&U!==void 0&&(a=U.cvssV2)!==null&&a!==void 0&&a.vectorString?(0,m.jsxs)(m.Fragment,{children:[(0,m.jsx)(X.Z,{cvss:o==null||(n=o.impact)===null||n===void 0||(l=n.baseMetricV2)===null||l===void 0?void 0:l.exploitabilityScore}),o==null||(i=o.impact)===null||i===void 0||(p=i.baseMetricV2)===null||p===void 0||(f=p.cvssV2)===null||f===void 0?void 0:f.vectorString]}):(0,m.jsx)("i",{children:"(not available)"})}),(0,m.jsx)(T.Z.Item,{label:"CVSS V3",children:o!=null&&(v=o.impact)!==null&&v!==void 0&&(S=v.baseMetricV3)!==null&&S!==void 0&&(E=S.cvssV3)!==null&&E!==void 0&&E.vectorString?(0,m.jsxs)(m.Fragment,{children:[(0,m.jsx)(X.Z,{cvss:o==null||(P=o.impact)===null||P===void 0||(x=P.baseMetricV3)===null||x===void 0?void 0:x.exploitabilityScore}),o==null||(Z=o.impact)===null||Z===void 0||(L=Z.baseMetricV3)===null||L===void 0||(O=L.cvssV3)===null||O===void 0||(b=O.vectorString)===null||b===void 0?void 0:b.replace("CVSS:3.1/","")]}):(0,m.jsx)("i",{children:"(not available)"})})]})})})},e=y},44743:function(re,j,t){"use strict";t.d(j,{w7:function(){return I},JS:function(){return D},Zb:function(){return T},gu:function(){return N},$U:function(){return s},O3:function(){return h},vh:function(){return R},rJ:function(){return $},zd:function(){return X},Ou:function(){return _},Vd:function(){return g},eX:function(){return A},jv:function(){return ee},lf:function(){return k},xe:function(){return V},AC:function(){return m},Mc:function(){return Q}});var r=t(32611),I=function(e){switch(e){case"OS":return"o";case"APPLICATION":return"a";case"HARDWARE":return"h";default:return}},D=function(e){switch(e){case"o":return"OS";case"a":return"APPLICATION";case"h":return"HARDWARE";default:return}},T=function(e){switch(e){case"HIGH":return 3;case"MEDIUM":return 2;case"LOW":return 1;default:return}},N=function(e){return e.substring(0,10)},Y=function(e){return e.replace(/\w\S*/g,function(u){return u.charAt(0).toUpperCase()+u.substr(1).toLowerCase()})},s=function(e){return e>=9?["Critical",r.jv]:e>=7?["High",r.U1]:e>=4?["Medium",r.WY]:["Low",r.q6]},h=function(e){return e==="Critical"?r.jv:e==="High"?r.U1:e==="Medium"?r.WY:r.q6},R=function(e){return e<=1.8?["Negligible",1]:e<=3.6?["Low",2]:e<=5.4?["Moderate",3]:e<=7.2?["Significant",4]:["Catastrophic",5]},$=function(e){return e<=.2?["Improbable",1]:e<=.4?["Remote",2]:e<=.6?["Occsional",3]:e<=.8?["Probale",4]:["Frequent",5]},X=function(e,u){var d=e*u;return d>12?["Critical",r.jv,4]:d>7?["High",r.U1,3]:d>3?["Medium",r.WY,2]:["Low",r.q6,1]},_=function(e){return e===4?"Critical":e===3?"High":e===2?"Medium":e===1?"Low":""},g=function(e){return e===5?"Catastrophic":e===4?"Significant":e===3?"Moderate":e===2?"Low":e===1?"Negligible":""},A=function(e){return e===5?"Frequent":e===4?"Probale":e===3?"Occsional":e===2?"Remote":e===1?"Improbable":""},ee=function(e){return Math.round(e*100)/100},k=function(e){return e<=.25?["Low",r.q6]:e<=.5?["Medium",r.WY]:e<=.75?["High",r.U1]:["Critical",r.jv]},V=function(e){return e==="Negligible"?r.Fe:e==="Low"?r.q6:e==="Moderate"?r.WY:e==="Significant"?r.U1:r.jv},m=function(e){return e==="Improbable"?r.Fe:e==="Low"?r.q6:e==="Occsional"?r.WY:e==="Significant"?r.U1:r.jv},Q=function(e){return e==="None"?r.Fe:e==="Low"?r.q6:e==="Medium"?r.WY:e==="High"?r.U1:r.jv}},4914:function(re,j,t){"use strict";t.d(j,{K:function(){return y},Z:function(){return U}});var r=t(96156),I=t(28481),D=t(90484),T=t(94184),N=t.n(T),Y=t(50344),s=t(67294),h=t(53124),R=t(96159),$=t(24308),X=function(n){var l=n.children;return l},_=X,g=t(22122);function A(a){return a!=null}var ee=function(n){var l=n.itemPrefixCls,i=n.component,p=n.span,f=n.className,v=n.style,S=n.labelStyle,E=n.contentStyle,P=n.bordered,x=n.label,Z=n.content,L=n.colon,O=i;if(P){var b;return s.createElement(O,{className:N()((b={},(0,r.Z)(b,"".concat(l,"-item-label"),A(x)),(0,r.Z)(b,"".concat(l,"-item-content"),A(Z)),b),f),style:v,colSpan:p},A(x)&&s.createElement("span",{style:S},x),A(Z)&&s.createElement("span",{style:E},Z))}return s.createElement(O,{className:N()("".concat(l,"-item"),f),style:v,colSpan:p},s.createElement("div",{className:"".concat(l,"-item-container")},(x||x===0)&&s.createElement("span",{className:N()("".concat(l,"-item-label"),(0,r.Z)({},"".concat(l,"-item-no-colon"),!L)),style:S},x),(Z||Z===0)&&s.createElement("span",{className:N()("".concat(l,"-item-content")),style:E},Z)))},k=ee;function V(a,n,l){var i=n.colon,p=n.prefixCls,f=n.bordered,v=l.component,S=l.type,E=l.showLabel,P=l.showContent,x=l.labelStyle,Z=l.contentStyle;return a.map(function(L,O){var b=L.props,B=b.label,W=b.children,z=b.prefixCls,w=z===void 0?p:z,o=b.className,M=b.style,G=b.labelStyle,K=b.contentStyle,q=b.span,te=q===void 0?1:q,F=L.key;return typeof v=="string"?s.createElement(k,{key:"".concat(S,"-").concat(F||O),className:o,style:M,labelStyle:(0,g.Z)((0,g.Z)({},x),G),contentStyle:(0,g.Z)((0,g.Z)({},Z),K),span:te,colon:i,component:v,itemPrefixCls:w,bordered:f,label:E?B:null,content:P?W:null}):[s.createElement(k,{key:"label-".concat(F||O),className:o,style:(0,g.Z)((0,g.Z)((0,g.Z)({},x),M),G),span:1,colon:i,component:v[0],itemPrefixCls:w,bordered:f,label:B}),s.createElement(k,{key:"content-".concat(F||O),className:o,style:(0,g.Z)((0,g.Z)((0,g.Z)({},Z),M),K),span:te*2-1,component:v[1],itemPrefixCls:w,bordered:f,content:W})]})}var m=function(n){var l=s.useContext(y),i=n.prefixCls,p=n.vertical,f=n.row,v=n.index,S=n.bordered;return p?s.createElement(s.Fragment,null,s.createElement("tr",{key:"label-".concat(v),className:"".concat(i,"-row")},V(f,n,(0,g.Z)({component:"th",type:"label",showLabel:!0},l))),s.createElement("tr",{key:"content-".concat(v),className:"".concat(i,"-row")},V(f,n,(0,g.Z)({component:"td",type:"content",showContent:!0},l)))):s.createElement("tr",{key:v,className:"".concat(i,"-row")},V(f,n,(0,g.Z)({component:S?["th","td"]:"td",type:"item",showLabel:!0,showContent:!0},l)))},Q=m,y=s.createContext({}),e={xxl:3,xl:3,lg:3,md:3,sm:2,xs:1};function u(a,n){if(typeof a=="number")return a;if((0,D.Z)(a)==="object")for(var l=0;l<$.c4.length;l++){var i=$.c4[l];if(n[i]&&a[i]!==void 0)return a[i]||e[i]}return 3}function d(a,n,l){var i=a;return(n===void 0||n>l)&&(i=(0,R.Tm)(a,{span:l})),i}function c(a,n){var l=(0,Y.Z)(a).filter(function(v){return v}),i=[],p=[],f=n;return l.forEach(function(v,S){var E,P=(E=v.props)===null||E===void 0?void 0:E.span,x=P||1;if(S===l.length-1){p.push(d(v,P,f)),i.push(p);return}x<f?(f-=x,p.push(v)):(p.push(d(v,x,f)),i.push(p),f=n,p=[])}),i}function C(a){var n,l=a.prefixCls,i=a.title,p=a.extra,f=a.column,v=f===void 0?e:f,S=a.colon,E=S===void 0?!0:S,P=a.bordered,x=a.layout,Z=a.children,L=a.className,O=a.style,b=a.size,B=a.labelStyle,W=a.contentStyle,z=s.useContext(h.E_),w=z.getPrefixCls,o=z.direction,M=w("descriptions",l),G=s.useState({}),K=(0,I.Z)(G,2),q=K[0],te=K[1],F=u(v,q);s.useEffect(function(){var H=$.ZP.subscribe(function(J){(0,D.Z)(v)==="object"&&te(J)});return function(){$.ZP.unsubscribe(H)}},[]);var ae=c(Z,F),ne=s.useMemo(function(){return{labelStyle:B,contentStyle:W}},[B,W]);return s.createElement(y.Provider,{value:ne},s.createElement("div",{className:N()(M,(n={},(0,r.Z)(n,"".concat(M,"-").concat(b),b&&b!=="default"),(0,r.Z)(n,"".concat(M,"-bordered"),!!P),(0,r.Z)(n,"".concat(M,"-rtl"),o==="rtl"),n),L),style:O},(i||p)&&s.createElement("div",{className:"".concat(M,"-header")},i&&s.createElement("div",{className:"".concat(M,"-title")},i),p&&s.createElement("div",{className:"".concat(M,"-extra")},p)),s.createElement("div",{className:"".concat(M,"-view")},s.createElement("table",null,s.createElement("tbody",null,ae.map(function(H,J){return s.createElement(Q,{key:J,index:J,colon:E,prefixCls:M,vertical:x==="vertical",bordered:P,row:H})}))))))}C.Item=_;var U=C},98858:function(re,j,t){"use strict";var r=t(38663),I=t.n(r),D=t(52953),T=t.n(D)},60331:function(re,j,t){"use strict";t.d(j,{Z:function(){return y}});var r=t(96156),I=t(22122),D=t(28481),T=t(54549),N=t(94184),Y=t.n(N),s=t(98423),h=t(67294),R=t(53124),$=t(98787),X=t(21790),_=function(e,u){var d={};for(var c in e)Object.prototype.hasOwnProperty.call(e,c)&&u.indexOf(c)<0&&(d[c]=e[c]);if(e!=null&&typeof Object.getOwnPropertySymbols=="function")for(var C=0,c=Object.getOwnPropertySymbols(e);C<c.length;C++)u.indexOf(c[C])<0&&Object.prototype.propertyIsEnumerable.call(e,c[C])&&(d[c[C]]=e[c[C]]);return d},g=function(u){var d,c=u.prefixCls,C=u.className,U=u.checked,a=u.onChange,n=u.onClick,l=_(u,["prefixCls","className","checked","onChange","onClick"]),i=h.useContext(R.E_),p=i.getPrefixCls,f=function(P){a==null||a(!U),n==null||n(P)},v=p("tag",c),S=Y()(v,(d={},(0,r.Z)(d,"".concat(v,"-checkable"),!0),(0,r.Z)(d,"".concat(v,"-checkable-checked"),U),d),C);return h.createElement("span",(0,I.Z)({},l,{className:S,onClick:f}))},A=g,ee=function(e,u){var d={};for(var c in e)Object.prototype.hasOwnProperty.call(e,c)&&u.indexOf(c)<0&&(d[c]=e[c]);if(e!=null&&typeof Object.getOwnPropertySymbols=="function")for(var C=0,c=Object.getOwnPropertySymbols(e);C<c.length;C++)u.indexOf(c[C])<0&&Object.prototype.propertyIsEnumerable.call(e,c[C])&&(d[c[C]]=e[c[C]]);return d},k=new RegExp("^(".concat($.Y.join("|"),")(-inverse)?$")),V=new RegExp("^(".concat($.E.join("|"),")$")),m=function(u,d){var c,C=u.prefixCls,U=u.className,a=u.style,n=u.children,l=u.icon,i=u.color,p=u.onClose,f=u.closeIcon,v=u.closable,S=v===void 0?!1:v,E=ee(u,["prefixCls","className","style","children","icon","color","onClose","closeIcon","closable"]),P=h.useContext(R.E_),x=P.getPrefixCls,Z=P.direction,L=h.useState(!0),O=(0,D.Z)(L,2),b=O[0],B=O[1];h.useEffect(function(){"visible"in E&&B(E.visible)},[E.visible]);var W=function(){return i?k.test(i)||V.test(i):!1},z=(0,I.Z)({backgroundColor:i&&!W()?i:void 0},a),w=W(),o=x("tag",C),M=Y()(o,(c={},(0,r.Z)(c,"".concat(o,"-").concat(i),w),(0,r.Z)(c,"".concat(o,"-has-color"),i&&!w),(0,r.Z)(c,"".concat(o,"-hidden"),!b),(0,r.Z)(c,"".concat(o,"-rtl"),Z==="rtl"),c),U),G=function(J){J.stopPropagation(),p==null||p(J),!J.defaultPrevented&&("visible"in E||B(!1))},K=function(){return S?f?h.createElement("span",{className:"".concat(o,"-close-icon"),onClick:G},f):h.createElement(T.Z,{className:"".concat(o,"-close-icon"),onClick:G}):null},q="onClick"in E||n&&n.type==="a",te=(0,s.Z)(E,["visible"]),F=l||null,ae=F?h.createElement(h.Fragment,null,F,h.createElement("span",null,n)):n,ne=h.createElement("span",(0,I.Z)({},te,{ref:d,className:M,style:z}),ae,K());return q?h.createElement(X.Z,null,ne):ne},Q=h.forwardRef(m);Q.CheckableTag=A;var y=Q},71153:function(re,j,t){"use strict";var r=t(38663),I=t.n(r),D=t(13277),T=t.n(D)}}]);
