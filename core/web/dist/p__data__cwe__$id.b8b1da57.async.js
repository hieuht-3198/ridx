(self.webpackChunkant_design_pro=self.webpackChunkant_design_pro||[]).push([[894],{52953:function(){},28579:function(ne,W,t){"use strict";t.r(W),t.d(W,{default:function(){return M}});var E=t(58024),F=t(91894),R=t(98858),x=t(4914),b=t(3182),G=t(2824),l=t(402),X=t(97272),Y=t(94043),Z=t.n(Y),k=t(51885),L=t(67294),u=t(11849),$=t(64172);function q(I,g,S){return D.apply(this,arguments)}function D(){return D=(0,b.Z)(Z().mark(function I(g,S,O){return Z().wrap(function(P){for(;;)switch(P.prev=P.next){case 0:return P.abrupt("return",(0,$.ZP)("/api/cwes/".concat(g),(0,u.Z)({method:"GET",params:(0,u.Z)({},S)},O||{})));case 1:case"end":return P.stop()}},I)})),D.apply(this,arguments)}var m=t(85893),_=X.Z.Paragraph,ee=function(g){var S,O=g==null||(S=g.match)===null||S===void 0?void 0:S.params,j=O.id,P=(0,L.useState)({}),n=(0,G.Z)(P,2),e=n[0],a=n[1],r=(0,L.useState)(!0),c=(0,G.Z)(r,2),o=c[0],s=c[1],v=function(){var p=(0,b.Z)(Z().mark(function f(){var i;return Z().wrap(function(C){for(;;)switch(C.prev=C.next){case 0:return C.next=2,q(j);case 2:i=C.sent,i&&a(i.data);case 4:case"end":return C.stop()}},f)}));return function(){return p.apply(this,arguments)}}();return(0,L.useEffect)(function(){v()},[]),(0,m.jsx)(k.ZP,{header:{title:"CWE Detail"},content:(0,m.jsx)(x.Z,{column:1,style:{marginBottom:-16},children:(0,m.jsx)(x.Z.Item,{label:"CWE ID",children:(0,m.jsx)("a",{children:j})})}),children:(0,m.jsx)(F.Z,{children:(0,m.jsxs)(x.Z,{title:"CWE info",column:1,children:[(0,m.jsx)(x.Z.Item,{label:"CWE ID",children:e==null?void 0:e.cwe_id}),(0,m.jsx)(x.Z.Item,{label:"CWE Name",children:e==null?void 0:e.cwe_name}),(0,m.jsx)(x.Z.Item,{label:"Description",children:(0,m.jsx)(_,{ellipsis:o?{rows:3,expandable:!0,symbol:"more"}:!1,children:e==null?void 0:e.description})})]})})})},M=ee},4914:function(ne,W,t){"use strict";t.d(W,{K:function(){return M},Z:function(){return P}});var E=t(96156),F=t(28481),R=t(90484),x=t(94184),b=t.n(x),G=t(50344),l=t(67294),X=t(53124),Y=t(96159),Z=t(24308),k=function(e){var a=e.children;return a},L=k,u=t(22122);function $(n){return n!=null}var q=function(e){var a=e.itemPrefixCls,r=e.component,c=e.span,o=e.className,s=e.style,v=e.labelStyle,p=e.contentStyle,f=e.bordered,i=e.label,h=e.content,C=e.colon,N=r;if(f){var d;return l.createElement(N,{className:b()((d={},(0,E.Z)(d,"".concat(a,"-item-label"),$(i)),(0,E.Z)(d,"".concat(a,"-item-content"),$(h)),d),o),style:s,colSpan:c},$(i)&&l.createElement("span",{style:v},i),$(h)&&l.createElement("span",{style:p},h))}return l.createElement(N,{className:b()("".concat(a,"-item"),o),style:s,colSpan:c},l.createElement("div",{className:"".concat(a,"-item-container")},(i||i===0)&&l.createElement("span",{className:b()("".concat(a,"-item-label"),(0,E.Z)({},"".concat(a,"-item-no-colon"),!C)),style:v},i),(h||h===0)&&l.createElement("span",{className:b()("".concat(a,"-item-content")),style:p},h)))},D=q;function m(n,e,a){var r=e.colon,c=e.prefixCls,o=e.bordered,s=a.component,v=a.type,p=a.showLabel,f=a.showContent,i=a.labelStyle,h=a.contentStyle;return n.map(function(C,N){var d=C.props,T=d.label,w=d.children,A=d.prefixCls,U=A===void 0?c:A,B=d.className,y=d.style,V=d.labelStyle,K=d.contentStyle,H=d.span,J=H===void 0?1:H,z=C.key;return typeof s=="string"?l.createElement(D,{key:"".concat(v,"-").concat(z||N),className:B,style:y,labelStyle:(0,u.Z)((0,u.Z)({},i),V),contentStyle:(0,u.Z)((0,u.Z)({},h),K),span:J,colon:r,component:s,itemPrefixCls:U,bordered:o,label:p?T:null,content:f?w:null}):[l.createElement(D,{key:"label-".concat(z||N),className:B,style:(0,u.Z)((0,u.Z)((0,u.Z)({},i),y),V),span:1,colon:r,component:s[0],itemPrefixCls:U,bordered:o,label:T}),l.createElement(D,{key:"content-".concat(z||N),className:B,style:(0,u.Z)((0,u.Z)((0,u.Z)({},h),y),K),span:J*2-1,component:s[1],itemPrefixCls:U,bordered:o,content:w})]})}var _=function(e){var a=l.useContext(M),r=e.prefixCls,c=e.vertical,o=e.row,s=e.index,v=e.bordered;return c?l.createElement(l.Fragment,null,l.createElement("tr",{key:"label-".concat(s),className:"".concat(r,"-row")},m(o,e,(0,u.Z)({component:"th",type:"label",showLabel:!0},a))),l.createElement("tr",{key:"content-".concat(s),className:"".concat(r,"-row")},m(o,e,(0,u.Z)({component:"td",type:"content",showContent:!0},a)))):l.createElement("tr",{key:s,className:"".concat(r,"-row")},m(o,e,(0,u.Z)({component:v?["th","td"]:"td",type:"item",showLabel:!0,showContent:!0},a)))},ee=_,M=l.createContext({}),I={xxl:3,xl:3,lg:3,md:3,sm:2,xs:1};function g(n,e){if(typeof n=="number")return n;if((0,R.Z)(n)==="object")for(var a=0;a<Z.c4.length;a++){var r=Z.c4[a];if(e[r]&&n[r]!==void 0)return n[r]||I[r]}return 3}function S(n,e,a){var r=n;return(e===void 0||e>a)&&(r=(0,Y.Tm)(n,{span:a})),r}function O(n,e){var a=(0,G.Z)(n).filter(function(s){return s}),r=[],c=[],o=e;return a.forEach(function(s,v){var p,f=(p=s.props)===null||p===void 0?void 0:p.span,i=f||1;if(v===a.length-1){c.push(S(s,f,o)),r.push(c);return}i<o?(o-=i,c.push(s)):(c.push(S(s,i,o)),r.push(c),o=e,c=[])}),r}function j(n){var e,a=n.prefixCls,r=n.title,c=n.extra,o=n.column,s=o===void 0?I:o,v=n.colon,p=v===void 0?!0:v,f=n.bordered,i=n.layout,h=n.children,C=n.className,N=n.style,d=n.size,T=n.labelStyle,w=n.contentStyle,A=l.useContext(X.E_),U=A.getPrefixCls,B=A.direction,y=U("descriptions",a),V=l.useState({}),K=(0,F.Z)(V,2),H=K[0],J=K[1],z=g(s,H);l.useEffect(function(){var te=Z.ZP.subscribe(function(Q){(0,R.Z)(s)==="object"&&J(Q)});return function(){Z.ZP.unsubscribe(te)}},[]);var ae=O(h,z),le=l.useMemo(function(){return{labelStyle:T,contentStyle:w}},[T,w]);return l.createElement(M.Provider,{value:le},l.createElement("div",{className:b()(y,(e={},(0,E.Z)(e,"".concat(y,"-").concat(d),d&&d!=="default"),(0,E.Z)(e,"".concat(y,"-bordered"),!!f),(0,E.Z)(e,"".concat(y,"-rtl"),B==="rtl"),e),C),style:N},(r||c)&&l.createElement("div",{className:"".concat(y,"-header")},r&&l.createElement("div",{className:"".concat(y,"-title")},r),c&&l.createElement("div",{className:"".concat(y,"-extra")},c)),l.createElement("div",{className:"".concat(y,"-view")},l.createElement("table",null,l.createElement("tbody",null,ae.map(function(te,Q){return l.createElement(ee,{key:Q,index:Q,colon:p,prefixCls:y,vertical:i==="vertical",bordered:f,row:te})}))))))}j.Item=L;var P=j},98858:function(ne,W,t){"use strict";var E=t(38663),F=t.n(E),R=t(52953),x=t.n(R)}}]);
