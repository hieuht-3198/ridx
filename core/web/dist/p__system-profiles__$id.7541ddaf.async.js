(self.webpackChunkant_design_pro=self.webpackChunkant_design_pro||[]).push([[969],{95309:function(F){F.exports={chartCard:"chartCard___3qknk",chartTop:"chartTop___2R1BK",chartTopMargin:"chartTopMargin___AyG2m",chartTopHasMargin:"chartTopHasMargin___1fvNn",metaWrap:"metaWrap___1CCfp",avatar:"avatar___2Fipb",meta:"meta___1hBzK",action:"action___1UvpU",total:"total___2r-XK",content:"content___3mTXa",contentFixed:"contentFixed___15Zmm",footer:"footer___2tHDy",footerMargin:"footerMargin___dYkOa"}},17594:function(F){F.exports={field:"field___17sfV",label:"label___pbsUN",number:"number___1z44s"}},25506:function(F){F.exports={iconGroup:"iconGroup___1v3pt",anticon:"anticon___3Xk68",rankingList:"rankingList___3RwuR",rankingItemNumber:"rankingItemNumber___2sm0Q",active:"active___104Mq",rankingItemTitle:"rankingItemTitle___1oOJZ",salesExtra:"salesExtra___2wuAO",currentDate:"currentDate___15bkb",salesCard:"salesCard___3AuAu",salesBar:"salesBar___1ZbKX",salesRank:"salesRank___AIPd0",salesCardExtra:"salesCardExtra___2dwYx",salesTypeRadio:"salesTypeRadio___17KwQ",offlineCard:"offlineCard___1AO4t",trendText:"trendText___1CnnA",rankingTitle:"rankingTitle___2fDAt",salesExtraWrap:"salesExtraWrap___3ldm6"}},52953:function(){},40182:function(F,R,t){"use strict";t.d(R,{th:function(){return m}});var a=t(92077),I=t.n(a),M=t(11849),S=t(58024),A=t(91894),L=t(93224),n=t(32059),T=t(69610),Z=t(54941),N=t(81306),C=t(19809),k=t(67294),j=t(94184),B=t.n(j),K=t(95309),g=t.n(K),v=t(85893),et=function(r){if(!r&&r!==0)return null;var s;switch(typeof r){case"undefined":s=null;break;case"function":s=(0,v.jsx)("div",{className:g().total,children:r()});break;default:s=(0,v.jsx)("div",{className:g().total,children:r})}return s},w=function(o){(0,N.Z)(s,o);var r=(0,C.Z)(s);function s(){var c;(0,T.Z)(this,s);for(var d=arguments.length,f=new Array(d),u=0;u<d;u++)f[u]=arguments[u];return c=r.call.apply(r,[this].concat(f)),c.renderContent=function(){var i=c.props,b=i.contentHeight,U=i.title,x=i.avatar,E=i.action,Y=i.total,O=i.footer,p=i.children,X=i.loading;return X?!1:(0,v.jsxs)("div",{className:g().chartCard,children:[(0,v.jsxs)("div",{className:B()(g().chartTop,(0,n.Z)({},g().chartTopMargin,!p&&!O)),children:[(0,v.jsx)("div",{className:g().avatar,children:x}),(0,v.jsxs)("div",{className:g().metaWrap,children:[(0,v.jsxs)("div",{className:g().meta,children:[(0,v.jsx)("span",{className:g().title,children:U}),(0,v.jsx)("span",{className:g().action,children:E})]}),et(Y)]})]}),p&&(0,v.jsx)("div",{className:g().content,style:{height:b||"auto"},children:(0,v.jsx)("div",{className:b&&g().contentFixed,children:p})}),O&&(0,v.jsx)("div",{className:B()(g().footer,(0,n.Z)({},g().footerMargin,!p)),children:O})]})},c}return(0,Z.Z)(s,[{key:"render",value:function(){var d=this.props,f=d.loading,u=f===void 0?!1:f,i=d.contentHeight,b=d.title,U=d.avatar,x=d.action,E=d.total,Y=d.footer,O=d.children,p=(0,L.Z)(d,["loading","contentHeight","title","avatar","action","total","footer","children"]);return(0,v.jsx)(A.Z,(0,M.Z)((0,M.Z)({loading:u,bodyStyle:{padding:"20px 24px 8px 24px"}},p),{},{children:this.renderContent()}))}}]),s}(k.Component),m=w,e=t(17594),D=t.n(e),V=function(r){var s=r.label,c=r.value,d=(0,L.Z)(r,["label","value"]);return(0,v.jsxs)("div",(0,M.Z)((0,M.Z)({className:D().field},d),{},{children:[(0,v.jsx)("span",{className:D().label,children:s}),(0,v.jsx)("span",{className:D().number,children:c})]}))},nt=V,l=function(r){return"\xA5 ".concat(I()(r).format("0,0"))},at={yuan:l,ChartCard:m,Field:nt}},64129:function(F,R,t){"use strict";var a=t(13062),I=t(71230),M=t(89032),S=t(15746),A=t(58024),L=t(91894),n=t(85893),T=function(N){var C=N.data;return(0,n.jsxs)(n.Fragment,{children:[(0,n.jsxs)(I.Z,{children:[(0,n.jsx)(S.Z,{span:12,children:(0,n.jsxs)(L.Z,{bordered:!0,style:{backgroundColor:"#FF4536"},bodyStyle:{padding:"8px"},children:[(0,n.jsx)("div",{children:"Critical"}),(0,n.jsx)("div",{className:"metric-value",children:C.critical||"-"})]})}),(0,n.jsx)(S.Z,{span:12,children:(0,n.jsxs)(L.Z,{bordered:!0,style:{backgroundColor:"#FEC44B"},bodyStyle:{padding:"8px"},children:[(0,n.jsx)("div",{children:"High"}),(0,n.jsx)("div",{className:"metric-value",children:C.high||"-"})]})})]}),(0,n.jsxs)(I.Z,{children:[(0,n.jsx)(S.Z,{span:12,children:(0,n.jsxs)(L.Z,{bordered:!0,style:{backgroundColor:"#FBE452"},bodyStyle:{padding:"8px"},children:[(0,n.jsx)("div",{children:"Medium"}),(0,n.jsx)("div",{className:"metric-value",children:C.medium||"-"})]})}),(0,n.jsx)(S.Z,{span:12,children:(0,n.jsxs)(L.Z,{bordered:!0,style:{backgroundColor:"#93D150"},bodyStyle:{padding:"8px"},children:[(0,n.jsx)("div",{children:"Low"}),(0,n.jsx)("div",{className:"metric-value",children:C.low||"-"})]})})]})]})};R.Z=T},32701:function(F,R,t){"use strict";t.r(R),t.d(R,{default:function(){return tt}});for(var a=t(58024),I=t(91894),M=t(98858),S=t(4914),A=t(3182),L=t(2824),n=t(94043),T=t.n(n),Z=t(44743),N=t(51885),C=t(21349),k=t(67294),j=t(13062),B=t(71230),K=t(11849),g=t(89032),v=t(15746),et=t(22385),w=t(61580),m=t(68628),e=t(92077),D=t.n(e),V=t(64129),nt=t(40182),l=t(85893),at={xs:24,sm:12,md:12,lg:12,xl:6,style:{marginBottom:24}},o=function(){return(0,l.jsxs)(B.Z,{gutter:24,children:[(0,l.jsx)(v.Z,(0,K.Z)((0,K.Z)({},at),{},{children:(0,l.jsx)(nt.th,{bordered:!1,title:"Total assets",action:(0,l.jsx)(w.Z,{title:"\u6307\u6807\u8BF4\u660E",children:(0,l.jsx)(m.Z,{})}),total:D()(12).format("0,0"),contentHeight:150,children:(0,l.jsx)(V.Z,{data:{critical:2,high:3,medium:5,low:6}})})})),(0,l.jsx)(v.Z,(0,K.Z)((0,K.Z)({},at),{},{children:(0,l.jsx)(nt.th,{bordered:!1,title:"Total deployment scenarios",action:(0,l.jsx)(w.Z,{title:"\u6307\u6807\u8BF4\u660E",children:(0,l.jsx)(m.Z,{})}),total:D()(300).format("0,0"),contentHeight:150,children:(0,l.jsx)(V.Z,{data:{critical:20,high:30,medium:50,low:60}})})}))]})},r=o,s=t(18106),c=t(51752),d=t(14965),f=t(68588),u=t(25506),i=t.n(u),b=f.Z.RangePicker,U=c.Z.TabPane,x=[],E=0;E<5;E+=1)x.push({title:"CVE-2020-".concat(Math.floor(Math.random()*1e4)),total:10});var Y=function(h){var H=h.rangePickerValue,z=h.salesData,q=h.isActive,$=h.handleRangePickerChange,Q=h.loading,y=h.selectDate;return(0,l.jsx)(I.Z,{children:(0,l.jsx)("div",{className:i().salesCard,children:(0,l.jsxs)(B.Z,{children:[(0,l.jsx)(v.Z,{span:12,children:(0,l.jsxs)("div",{className:i().salesRank,children:[(0,l.jsx)("h4",{className:i().rankingTitle,children:"Vulnerabily rank"}),(0,l.jsx)("ul",{className:i().rankingList,children:x.map(function(W,P){return(0,l.jsxs)("li",{children:[(0,l.jsx)("span",{className:"".concat(i().rankingItemNumber," ").concat(P<3?i().active:""),children:P+1}),(0,l.jsx)("span",{className:i().rankingItemTitle,title:W.title,children:W.title}),(0,l.jsx)("span",{className:i().rankingItemValue,children:D()(W.total).format("0,0")})]},W.title)})})]})}),(0,l.jsx)(v.Z,{span:12,children:(0,l.jsxs)("div",{className:i().salesRank,children:[(0,l.jsx)("h4",{className:i().rankingTitle,children:"Vulnerabily rank"}),(0,l.jsx)("ul",{className:i().rankingList,children:x.map(function(W,P){return(0,l.jsxs)("li",{children:[(0,l.jsx)("span",{className:"".concat(i().rankingItemNumber," ").concat(P<3?i().active:""),children:P+1}),(0,l.jsx)("span",{className:i().rankingItemTitle,title:W.title,children:W.title}),(0,l.jsx)("span",{className:i().rankingItemValue,children:D()(W.total).format("0,0")})]},W.title)})})]})})]})})})},O=Y,p=t(64172);function X(G,h,H){return J.apply(this,arguments)}function J(){return J=(0,A.Z)(T().mark(function G(h,H,z){return T().wrap(function($){for(;;)switch($.prev=$.next){case 0:return $.abrupt("return",(0,p.ZP)("/api/system_profiles/".concat(h),(0,K.Z)({method:"GET",params:(0,K.Z)({},H)},z||{})));case 1:case"end":return $.stop()}},G)})),J.apply(this,arguments)}var _=function(h){var H,z=h==null||(H=h.match)===null||H===void 0?void 0:H.params,q=z.id,$=(0,k.useState)({}),Q=(0,L.Z)($,2),y=Q[0],W=Q[1];return(0,k.useEffect)(function(){var P=function(){var rt=(0,A.Z)(T().mark(function ot(){var st;return T().wrap(function(lt){for(;;)switch(lt.prev=lt.next){case 0:return lt.next=2,X(q);case 2:st=lt.sent,console.log("Res",st),W(st.data);case 5:case"end":return lt.stop()}},ot)}));return function(){return rt.apply(this,arguments)}}();P()},[]),(0,l.jsx)(N.ZP,{header:{title:"System profile detail"},content:(0,l.jsx)(S.Z,{column:2,style:{marginBottom:-16},children:(0,l.jsx)(S.Z.Item,{label:"System profile",children:(0,l.jsx)("a",{onClick:function(){},children:y.name})})}),children:(0,l.jsxs)(C.Z,{children:[(0,l.jsx)(r,{}),(0,l.jsx)(I.Z,{title:"System profile detail",style:{marginBottom:24},children:(y==null?void 0:y.name)&&(0,l.jsxs)("ul",{children:[(0,l.jsx)("li",{children:"Name: ".concat(y==null?void 0:y.name)}),(0,l.jsx)("li",{children:"Description: ".concat(y==null?void 0:y.description)}),Object.keys(y==null?void 0:y.custom_fields).map(function(P){return(0,l.jsx)("li",{children:"".concat(P,": ").concat(y==null?void 0:y.custom_fields[P])},P)}),(0,l.jsx)("li",{children:"Created at: ".concat((0,Z.gu)(y==null?void 0:y.created_at))}),(0,l.jsx)("li",{children:"Updated at: ".concat((0,Z.gu)(y==null?void 0:y.updated_at))})]})}),(0,l.jsx)(O,{})]})})},tt=_},44743:function(F,R,t){"use strict";t.d(R,{w7:function(){return I},JS:function(){return M},Zb:function(){return S},gu:function(){return A},$U:function(){return n},O3:function(){return T},vh:function(){return Z},rJ:function(){return N},zd:function(){return C},Ou:function(){return k},Vd:function(){return j},eX:function(){return B},jv:function(){return K},lf:function(){return g},xe:function(){return v},AC:function(){return et},Mc:function(){return w}});var a=t(32611),I=function(e){switch(e){case"OS":return"o";case"APPLICATION":return"a";case"HARDWARE":return"h";default:return}},M=function(e){switch(e){case"o":return"OS";case"a":return"APPLICATION";case"h":return"HARDWARE";default:return}},S=function(e){switch(e){case"HIGH":return 3;case"MEDIUM":return 2;case"LOW":return 1;default:return}},A=function(e){return e.substring(0,10)},L=function(e){return e.replace(/\w\S*/g,function(D){return D.charAt(0).toUpperCase()+D.substr(1).toLowerCase()})},n=function(e){return e>=9?["Critical",a.jv]:e>=7?["High",a.U1]:e>=4?["Medium",a.WY]:["Low",a.q6]},T=function(e){return e==="Critical"?a.jv:e==="High"?a.U1:e==="Medium"?a.WY:a.q6},Z=function(e){return e<=1.8?["Negligible",1]:e<=3.6?["Low",2]:e<=5.4?["Moderate",3]:e<=7.2?["Significant",4]:["Catastrophic",5]},N=function(e){return e<=.2?["Improbable",1]:e<=.4?["Remote",2]:e<=.6?["Occsional",3]:e<=.8?["Probale",4]:["Frequent",5]},C=function(e,D){var V=e*D;return V>12?["Critical",a.jv,4]:V>7?["High",a.U1,3]:V>3?["Medium",a.WY,2]:["Low",a.q6,1]},k=function(e){return e===4?"Critical":e===3?"High":e===2?"Medium":e===1?"Low":""},j=function(e){return e===5?"Catastrophic":e===4?"Significant":e===3?"Moderate":e===2?"Low":e===1?"Negligible":""},B=function(e){return e===5?"Frequent":e===4?"Probale":e===3?"Occsional":e===2?"Remote":e===1?"Improbable":""},K=function(e){return Math.round(e*100)/100},g=function(e){return e<=.25?["Low",a.q6]:e<=.5?["Medium",a.WY]:e<=.75?["High",a.U1]:["Critical",a.jv]},v=function(e){return e==="Negligible"?a.Fe:e==="Low"?a.q6:e==="Moderate"?a.WY:e==="Significant"?a.U1:a.jv},et=function(e){return e==="Improbable"?a.Fe:e==="Low"?a.q6:e==="Occsional"?a.WY:e==="Significant"?a.U1:a.jv},w=function(e){return e==="None"?a.Fe:e==="Low"?a.q6:e==="Medium"?a.WY:e==="High"?a.U1:a.jv}},9708:function(F,R,t){"use strict";t.d(R,{Z:function(){return L},F:function(){return n}});var a=t(96156),I=t(94184),M=t.n(I),S=t(93355),A=(0,S.b)("warning","error","");function L(T,Z,N){var C;return M()((C={},(0,a.Z)(C,"".concat(T,"-status-success"),Z==="success"),(0,a.Z)(C,"".concat(T,"-status-warning"),Z==="warning"),(0,a.Z)(C,"".concat(T,"-status-error"),Z==="error"),(0,a.Z)(C,"".concat(T,"-status-validating"),Z==="validating"),(0,a.Z)(C,"".concat(T,"-has-feedback"),N),C))}var n=function(Z,N){return N||Z}},4914:function(F,R,t){"use strict";t.d(R,{K:function(){return m},Z:function(){return at}});var a=t(96156),I=t(28481),M=t(90484),S=t(94184),A=t.n(S),L=t(50344),n=t(67294),T=t(53124),Z=t(96159),N=t(24308),C=function(r){var s=r.children;return s},k=C,j=t(22122);function B(o){return o!=null}var K=function(r){var s=r.itemPrefixCls,c=r.component,d=r.span,f=r.className,u=r.style,i=r.labelStyle,b=r.contentStyle,U=r.bordered,x=r.label,E=r.content,Y=r.colon,O=c;if(U){var p;return n.createElement(O,{className:A()((p={},(0,a.Z)(p,"".concat(s,"-item-label"),B(x)),(0,a.Z)(p,"".concat(s,"-item-content"),B(E)),p),f),style:u,colSpan:d},B(x)&&n.createElement("span",{style:i},x),B(E)&&n.createElement("span",{style:b},E))}return n.createElement(O,{className:A()("".concat(s,"-item"),f),style:u,colSpan:d},n.createElement("div",{className:"".concat(s,"-item-container")},(x||x===0)&&n.createElement("span",{className:A()("".concat(s,"-item-label"),(0,a.Z)({},"".concat(s,"-item-no-colon"),!Y)),style:i},x),(E||E===0)&&n.createElement("span",{className:A()("".concat(s,"-item-content")),style:b},E)))},g=K;function v(o,r,s){var c=r.colon,d=r.prefixCls,f=r.bordered,u=s.component,i=s.type,b=s.showLabel,U=s.showContent,x=s.labelStyle,E=s.contentStyle;return o.map(function(Y,O){var p=Y.props,X=p.label,J=p.children,_=p.prefixCls,tt=_===void 0?d:_,G=p.className,h=p.style,H=p.labelStyle,z=p.contentStyle,q=p.span,$=q===void 0?1:q,Q=Y.key;return typeof u=="string"?n.createElement(g,{key:"".concat(i,"-").concat(Q||O),className:G,style:h,labelStyle:(0,j.Z)((0,j.Z)({},x),H),contentStyle:(0,j.Z)((0,j.Z)({},E),z),span:$,colon:c,component:u,itemPrefixCls:tt,bordered:f,label:b?X:null,content:U?J:null}):[n.createElement(g,{key:"label-".concat(Q||O),className:G,style:(0,j.Z)((0,j.Z)((0,j.Z)({},x),h),H),span:1,colon:c,component:u[0],itemPrefixCls:tt,bordered:f,label:X}),n.createElement(g,{key:"content-".concat(Q||O),className:G,style:(0,j.Z)((0,j.Z)((0,j.Z)({},E),h),z),span:$*2-1,component:u[1],itemPrefixCls:tt,bordered:f,content:J})]})}var et=function(r){var s=n.useContext(m),c=r.prefixCls,d=r.vertical,f=r.row,u=r.index,i=r.bordered;return d?n.createElement(n.Fragment,null,n.createElement("tr",{key:"label-".concat(u),className:"".concat(c,"-row")},v(f,r,(0,j.Z)({component:"th",type:"label",showLabel:!0},s))),n.createElement("tr",{key:"content-".concat(u),className:"".concat(c,"-row")},v(f,r,(0,j.Z)({component:"td",type:"content",showContent:!0},s)))):n.createElement("tr",{key:u,className:"".concat(c,"-row")},v(f,r,(0,j.Z)({component:i?["th","td"]:"td",type:"item",showLabel:!0,showContent:!0},s)))},w=et,m=n.createContext({}),e={xxl:3,xl:3,lg:3,md:3,sm:2,xs:1};function D(o,r){if(typeof o=="number")return o;if((0,M.Z)(o)==="object")for(var s=0;s<N.c4.length;s++){var c=N.c4[s];if(r[c]&&o[c]!==void 0)return o[c]||e[c]}return 3}function V(o,r,s){var c=o;return(r===void 0||r>s)&&(c=(0,Z.Tm)(o,{span:s})),c}function nt(o,r){var s=(0,L.Z)(o).filter(function(u){return u}),c=[],d=[],f=r;return s.forEach(function(u,i){var b,U=(b=u.props)===null||b===void 0?void 0:b.span,x=U||1;if(i===s.length-1){d.push(V(u,U,f)),c.push(d);return}x<f?(f-=x,d.push(u)):(d.push(V(u,x,f)),c.push(d),f=r,d=[])}),c}function l(o){var r,s=o.prefixCls,c=o.title,d=o.extra,f=o.column,u=f===void 0?e:f,i=o.colon,b=i===void 0?!0:i,U=o.bordered,x=o.layout,E=o.children,Y=o.className,O=o.style,p=o.size,X=o.labelStyle,J=o.contentStyle,_=n.useContext(T.E_),tt=_.getPrefixCls,G=_.direction,h=tt("descriptions",s),H=n.useState({}),z=(0,I.Z)(H,2),q=z[0],$=z[1],Q=D(u,q);n.useEffect(function(){var P=N.ZP.subscribe(function(rt){(0,M.Z)(u)==="object"&&$(rt)});return function(){N.ZP.unsubscribe(P)}},[]);var y=nt(E,Q),W=n.useMemo(function(){return{labelStyle:X,contentStyle:J}},[X,J]);return n.createElement(m.Provider,{value:W},n.createElement("div",{className:A()(h,(r={},(0,a.Z)(r,"".concat(h,"-").concat(p),p&&p!=="default"),(0,a.Z)(r,"".concat(h,"-bordered"),!!U),(0,a.Z)(r,"".concat(h,"-rtl"),G==="rtl"),r),Y),style:O},(c||d)&&n.createElement("div",{className:"".concat(h,"-header")},c&&n.createElement("div",{className:"".concat(h,"-title")},c),d&&n.createElement("div",{className:"".concat(h,"-extra")},d)),n.createElement("div",{className:"".concat(h,"-view")},n.createElement("table",null,n.createElement("tbody",null,y.map(function(P,rt){return n.createElement(w,{key:rt,index:rt,colon:b,prefixCls:h,vertical:x==="vertical",bordered:U,row:P})}))))))}l.Item=k;var at=l},98858:function(F,R,t){"use strict";var a=t(38663),I=t.n(a),M=t(52953),S=t.n(M)}}]);
