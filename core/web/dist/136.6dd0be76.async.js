(self.webpackChunkant_design_pro=self.webpackChunkant_design_pro||[]).push([[136],{99165:function(_,x,i){"use strict";i.d(x,{Z:function(){return p}});var d=i(28991),e=i(67294),C={icon:{tag:"svg",attrs:{viewBox:"64 64 896 896",focusable:"false"},children:[{tag:"path",attrs:{d:"M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"}}]},name:"copy",theme:"outlined"},A=C,c=i(27029),f=function(K,B){return e.createElement(c.Z,(0,d.Z)((0,d.Z)({},K),{},{ref:B,icon:A}))};f.displayName="CopyOutlined";var p=e.forwardRef(f)},8212:function(_,x,i){"use strict";i.d(x,{Z:function(){return p}});var d=i(28991),e=i(67294),C={icon:{tag:"svg",attrs:{viewBox:"64 64 896 896",focusable:"false"},children:[{tag:"path",attrs:{d:"M257.7 752c2 0 4-.2 6-.5L431.9 722c2-.4 3.9-1.3 5.3-2.8l423.9-423.9a9.96 9.96 0 000-14.1L694.9 114.9c-1.9-1.9-4.4-2.9-7.1-2.9s-5.2 1-7.1 2.9L256.8 538.8c-1.5 1.5-2.4 3.3-2.8 5.3l-29.5 168.2a33.5 33.5 0 009.4 29.8c6.6 6.4 14.9 9.9 23.8 9.9zm67.4-174.4L687.8 215l73.3 73.3-362.7 362.6-88.9 15.7 15.6-89zM880 836H144c-17.7 0-32 14.3-32 32v36c0 4.4 3.6 8 8 8h784c4.4 0 8-3.6 8-8v-36c0-17.7-14.3-32-32-32z"}}]},name:"edit",theme:"outlined"},A=C,c=i(27029),f=function(K,B){return e.createElement(c.Z,(0,d.Z)((0,d.Z)({},K),{},{ref:B,icon:A}))};f.displayName="EditOutlined";var p=e.forwardRef(f)},47828:function(){},97272:function(_,x,i){"use strict";i.d(x,{Z:function(){return Wt}});var d=i(22122),e=i(67294),C=i(96156),A=i(90484),c=i(28481),f=i(79508),p=i(99165),R=i(8212),K=i(94184),B=i.n(K),le=i(20640),q=i.n(le),O=i(48717),se=i(50344),ce=i(8410),U=i(21770),ue=i(98423),we=i(42550),Le=i(53124),lt=i(42051),Re=i(61580),Me=i(79370),Ie=i(34952),De=i(28991),st={icon:{tag:"svg",attrs:{viewBox:"64 64 896 896",focusable:"false"},children:[{tag:"path",attrs:{d:"M864 170h-60c-4.4 0-8 3.6-8 8v518H310v-73c0-6.7-7.8-10.5-13-6.3l-141.9 112a8 8 0 000 12.6l141.9 112c5.3 4.2 13 .4 13-6.3v-75h498c35.3 0 64-28.7 64-64V178c0-4.4-3.6-8-8-8z"}}]},name:"enter",theme:"outlined"},ct=st,ut=i(27029),Ne=function(r,a){return e.createElement(ut.Z,(0,De.Z)((0,De.Z)({},r),{},{ref:a,icon:ct}))};Ne.displayName="EnterOutlined";var dt=e.forwardRef(Ne),Ae=i(15105),ft=i(94418),vt=i(96159),pt=function(r){var a=r.prefixCls,n=r["aria-label"],o=r.className,v=r.style,m=r.direction,y=r.maxLength,L=r.autoSize,M=L===void 0?!0:L,Z=r.value,j=r.onSave,z=r.onCancel,F=r.onEnd,b=r.component,H=r.enterIcon,k=H===void 0?e.createElement(dt,null):H,h=e.useRef(),I=e.useRef(!1),G=e.useRef(),T=e.useState(Z),oe=(0,c.Z)(T,2),J=oe[0],ie=oe[1];e.useEffect(function(){ie(Z)},[Z]),e.useEffect(function(){if(h.current&&h.current.resizableTextArea){var E=h.current.resizableTextArea.textArea;E.focus();var S=E.value.length;E.setSelectionRange(S,S)}},[]);var ee=function(S){var w=S.target;ie(w.value.replace(/[\n\r]/g,""))},g=function(){I.current=!0},W=function(){I.current=!1},V=function(S){var w=S.keyCode;I.current||(G.current=w)},te=function(){j(J.trim())},de=function(S){var w=S.keyCode,me=S.ctrlKey,ve=S.altKey,Q=S.metaKey,D=S.shiftKey;G.current===w&&!I.current&&!me&&!ve&&!Q&&!D&&(w===Ae.Z.ENTER?(te(),F==null||F()):w===Ae.Z.ESC&&z())},ne=function(){te()},fe=b?"".concat(a,"-").concat(b):"",P=B()(a,"".concat(a,"-edit-content"),(0,C.Z)({},"".concat(a,"-rtl"),m==="rtl"),o,fe);return e.createElement("div",{className:P,style:v},e.createElement(ft.Z,{ref:h,maxLength:y,value:J,onChange:ee,onKeyDown:V,onKeyUp:de,onCompositionStart:g,onCompositionEnd:W,onBlur:ne,"aria-label":n,rows:1,autoSize:M}),k!==null?(0,vt.Tm)(k,{className:"".concat(a,"-edit-content-confirm")}):null)},yt=pt;function Ze(t,r){return e.useMemo(function(){var a=!!t;return[a,(0,d.Z)((0,d.Z)({},r),a&&(0,A.Z)(t)==="object"?t:null)]},[t])}var mt=function(t,r){var a=e.useRef(!1);e.useEffect(function(){a.current?t():a.current=!0},r)},gt=function(t,r){var a={};for(var n in t)Object.prototype.hasOwnProperty.call(t,n)&&r.indexOf(n)<0&&(a[n]=t[n]);if(t!=null&&typeof Object.getOwnPropertySymbols=="function")for(var o=0,n=Object.getOwnPropertySymbols(t);o<n.length;o++)r.indexOf(n[o])<0&&Object.prototype.propertyIsEnumerable.call(t,n[o])&&(a[n[o]]=t[n[o]]);return a},Et=function(r,a){var n=r.prefixCls,o=r.component,v=o===void 0?"article":o,m=r.className,y=r["aria-label"],L=r.setContentRef,M=r.children,Z=gt(r,["prefixCls","component","className","aria-label","setContentRef","children"]),j=e.useContext(Le.E_),z=j.getPrefixCls,F=j.direction,b=a;L&&(b=(0,we.sQ)(a,L));var H=v,k=z("typography",n),h=B()(k,(0,C.Z)({},"".concat(k,"-rtl"),F==="rtl"),m);return e.createElement(H,(0,d.Z)({className:h,"aria-label":y,ref:b},Z),M)},Ct=e.forwardRef(Et),ht=Ct,$e=ht;function Ke(t){var r=(0,A.Z)(t);return r==="string"||r==="number"}function St(t){var r=0;return t.forEach(function(a){Ke(a)?r+=String(a).length:r+=1}),r}function je(t,r){for(var a=0,n=[],o=0;o<t.length;o+=1){if(a===r)return n;var v=t[o],m=Ke(v),y=m?String(v).length:1,L=a+y;if(L>r){var M=r-a;return n.push(String(v).slice(0,M)),n}n.push(v),a=L}return t}var bt=0,Ee=1,ze=2,Te=3,ke=4,xt=function(r){var a=r.enabledMeasure,n=r.children,o=r.text,v=r.width,m=r.rows,y=r.onEllipsis,L=e.useState([0,0,0]),M=(0,c.Z)(L,2),Z=M[0],j=M[1],z=e.useState(bt),F=(0,c.Z)(z,2),b=F[0],H=F[1],k=(0,c.Z)(Z,3),h=k[0],I=k[1],G=k[2],T=e.useState(0),oe=(0,c.Z)(T,2),J=oe[0],ie=oe[1],ee=e.useRef(null),g=e.useRef(null),W=e.useMemo(function(){return(0,se.Z)(o)},[o]),V=e.useMemo(function(){return St(W)},[W]),te=e.useMemo(function(){return!a||b!==Te?n(W,!1):n(je(W,I),I<V)},[a,b,n,W,I,V]);(0,ce.Z)(function(){a&&v&&V&&(H(Ee),j([0,Math.ceil(V/2),V]))},[a,v,o,V,m]),(0,ce.Z)(function(){var P;b===Ee&&ie(((P=ee.current)===null||P===void 0?void 0:P.offsetHeight)||0)},[b]),(0,ce.Z)(function(){var P,E;if(J){if(b===Ee){var S=((P=g.current)===null||P===void 0?void 0:P.offsetHeight)||0,w=m*J;S<=w?(H(ke),y(!1)):H(ze)}else if(b===ze)if(h!==G){var me=((E=g.current)===null||E===void 0?void 0:E.offsetHeight)||0,ve=m*J,Q=h,D=G;h===G-1?D=h:me<=ve?Q=I:D=I;var Pe=Math.ceil((Q+D)/2);j([Q,Pe,D])}else H(Te),y(!0)}},[b,h,G,m,J]);var de={width:v,whiteSpace:"normal",margin:0,padding:0},ne=function(E,S,w){return e.createElement("span",{"aria-hidden":!0,ref:S,style:(0,d.Z)({position:"fixed",display:"block",left:0,top:0,zIndex:-9999,visibility:"hidden",pointerEvents:"none"},w)},E)},fe=function(E,S){var w=je(W,E);return ne(n(w,!0),S,de)};return e.createElement(e.Fragment,null,te,a&&b!==Te&&b!==ke&&e.createElement(e.Fragment,null,ne("lg",ee,{wordBreak:"keep-all",whiteSpace:"nowrap"}),b===Ee?ne(n(W,!1),g,de):fe(I,g)))},Ot=xt,Rt=function(r){var a=r.title,n=r.enabledEllipsis,o=r.isEllipsis,v=r.children;return!a||!n?v:e.createElement(Re.Z,{title:a,visible:o?void 0:!1},v)},Zt=Rt,Tt=function(t,r){var a={};for(var n in t)Object.prototype.hasOwnProperty.call(t,n)&&r.indexOf(n)<0&&(a[n]=t[n]);if(t!=null&&typeof Object.getOwnPropertySymbols=="function")for(var o=0,n=Object.getOwnPropertySymbols(t);o<n.length;o++)r.indexOf(n[o])<0&&Object.prototype.propertyIsEnumerable.call(t,n[o])&&(a[n[o]]=t[n[o]]);return a};function Pt(t,r){var a=t.mark,n=t.code,o=t.underline,v=t.delete,m=t.strong,y=t.keyboard,L=t.italic,M=r;function Z(j,z){!j||(M=e.createElement(z,{},M))}return Z(m,"strong"),Z(o,"u"),Z(v,"del"),Z(n,"code"),Z(a,"mark"),Z(y,"kbd"),Z(L,"i"),M}function Ce(t,r,a){return t===!0||t===void 0?r:t||a&&r}function Be(t){return Array.isArray(t)?t:[t]}var wt="...",Lt=e.forwardRef(function(t,r){var a=t.prefixCls,n=t.className,o=t.style,v=t.type,m=t.disabled,y=t.children,L=t.ellipsis,M=t.editable,Z=t.copyable,j=t.component,z=t.title,F=Tt(t,["prefixCls","className","style","type","disabled","children","ellipsis","editable","copyable","component","title"]),b=e.useContext(Le.E_),H=b.getPrefixCls,k=b.direction,h=(0,lt.E)("Text")[0],I=e.useRef(null),G=e.useRef(null),T=H("typography",a),oe=(0,ue.Z)(F,["mark","code","delete","underline","strong","keyboard","italic"]),J=Ze(M),ie=(0,c.Z)(J,2),ee=ie[0],g=ie[1],W=(0,U.Z)(!1,{value:g.editing}),V=(0,c.Z)(W,2),te=V[0],de=V[1],ne=g.triggerType,fe=ne===void 0?["icon"]:ne,P=function(l){var s;l&&((s=g.onStart)===null||s===void 0||s.call(g)),de(l)};mt(function(){var u;te||(u=G.current)===null||u===void 0||u.focus()},[te]);var E=function(l){l==null||l.preventDefault(),P(!0)},S=function(l){var s;(s=g.onChange)===null||s===void 0||s.call(g,l),P(!1)},w=function(){var l;(l=g.onCancel)===null||l===void 0||l.call(g),P(!1)},me=Ze(Z),ve=(0,c.Z)(me,2),Q=ve[0],D=ve[1],Pe=e.useState(!1),Ue=(0,c.Z)(Pe,2),Se=Ue[0],He=Ue[1],We=e.useRef(),Ve={};D.format&&(Ve.format=D.format);var Fe=function(){clearTimeout(We.current)},Vt=function(l){var s;l==null||l.preventDefault(),l==null||l.stopPropagation(),q()(D.text||String(y)||"",Ve),He(!0),Fe(),We.current=setTimeout(function(){He(!1)},3e3),(s=D.onCopy)===null||s===void 0||s.call(D,l)};e.useEffect(function(){return Fe},[]);var Ft=e.useState(!1),Ge=(0,c.Z)(Ft,2),Je=Ge[0],Gt=Ge[1],Jt=e.useState(!1),Qe=(0,c.Z)(Jt,2),Xe=Qe[0],Qt=Qe[1],Xt=e.useState(!1),Ye=(0,c.Z)(Xt,2),Yt=Ye[0],_t=Ye[1],qt=e.useState(!1),_e=(0,c.Z)(qt,2),qe=_e[0],en=_e[1],tn=e.useState(!1),et=(0,c.Z)(tn,2),tt=et[0],nn=et[1],rn=Ze(L,{expandable:!1}),nt=(0,c.Z)(rn,2),re=nt[0],N=nt[1],X=re&&!Yt,rt=N.rows,pe=rt===void 0?1:rt,be=e.useMemo(function(){return!X||N.suffix!==void 0||N.onEllipsis||N.expandable||ee||Q},[X,N,ee,Q]);(0,ce.Z)(function(){re&&!be&&(Gt((0,Me.G)("webkitLineClamp")),Qt((0,Me.G)("textOverflow")))},[be,re]);var Y=e.useMemo(function(){return be?!1:pe===1?Xe:Je},[be,Xe,Je]),at=X&&(Y?tt:qe),an=X&&pe===1&&Y,xe=X&&pe>1&&Y,on=function(l){var s;_t(!0),(s=N.onExpand)===null||s===void 0||s.call(N,l)},ln=e.useState(0),ot=(0,c.Z)(ln,2),sn=ot[0],cn=ot[1],un=function(l){var s=l.offsetWidth;cn(s)},dn=function(l){var s;en(l),qe!==l&&((s=N.onEllipsis)===null||s===void 0||s.call(N,l))};e.useEffect(function(){var u=I.current;if(re&&Y&&u){var l=xe?u.offsetHeight<u.scrollHeight:u.offsetWidth<u.scrollWidth;tt!==l&&nn(l)}},[re,Y,y,xe]);var Oe=N.tooltip===!0?y:N.tooltip,it=e.useMemo(function(){var u=function(s){return["string","number"].includes((0,A.Z)(s))};if(!(!re||Y)){if(u(y))return y;if(u(z))return z;if(u(Oe))return Oe}},[re,Y,z,Oe,at]);if(te)return e.createElement(yt,{value:typeof y=="string"?y:"",onSave:S,onCancel:w,onEnd:g.onEnd,prefixCls:T,className:n,style:o,direction:k,component:j,maxLength:g.maxLength,autoSize:g.autoSize,enterIcon:g.enterIcon});var fn=function(){var l=N.expandable,s=N.symbol;if(!l)return null;var $;return s?$=s:$=h.expand,e.createElement("a",{key:"expand",className:"".concat(T,"-expand"),onClick:on,"aria-label":h.expand},$)},vn=function(){if(!!ee){var l=g.icon,s=g.tooltip,$=(0,se.Z)(s)[0]||h.edit,ae=typeof $=="string"?$:"";return fe.includes("icon")?e.createElement(Re.Z,{key:"edit",title:s===!1?"":$},e.createElement(Ie.Z,{ref:G,className:"".concat(T,"-edit"),onClick:E,"aria-label":ae},l||e.createElement(R.Z,{role:"button"}))):null}},pn=function(){if(!!Q){var l=D.tooltips,s=D.icon,$=Be(l),ae=Be(s),ge=Se?Ce($[1],h.copied):Ce($[0],h.copy),gn=Se?h.copied:h.copy,En=typeof ge=="string"?ge:gn;return e.createElement(Re.Z,{key:"copy",title:ge},e.createElement(Ie.Z,{className:B()("".concat(T,"-copy"),Se&&"".concat(T,"-copy-success")),onClick:Vt,"aria-label":En},Se?Ce(ae[1],e.createElement(f.Z,null),!0):Ce(ae[0],e.createElement(p.Z,null),!0)))}},yn=function(l){return[l&&fn(),vn(),pn()]},mn=function(l){return[l&&e.createElement("span",{"aria-hidden":!0,key:"ellipsis"},wt),N.suffix,yn(l)]};return e.createElement(O.Z,{onResize:un,disabled:!X||Y},function(u){var l;return e.createElement(Zt,{title:Oe,enabledEllipsis:X,isEllipsis:at},e.createElement($e,(0,d.Z)({className:B()((l={},(0,C.Z)(l,"".concat(T,"-").concat(v),v),(0,C.Z)(l,"".concat(T,"-disabled"),m),(0,C.Z)(l,"".concat(T,"-ellipsis"),re),(0,C.Z)(l,"".concat(T,"-single-line"),X&&pe===1),(0,C.Z)(l,"".concat(T,"-ellipsis-single-line"),an),(0,C.Z)(l,"".concat(T,"-ellipsis-multiple-line"),xe),l),n),style:(0,d.Z)((0,d.Z)({},o),{WebkitLineClamp:xe?pe:void 0}),component:j,ref:(0,we.sQ)(u,I,r),direction:k,onClick:fe.includes("text")?E:null,"aria-label":it,title:z},oe),e.createElement(Ot,{enabledMeasure:X&&!Y,text:y,rows:pe,width:sn,onEllipsis:dn},function(s,$){var ae=s;s.length&&$&&it&&(ae=e.createElement("span",{key:"show-content","aria-hidden":!0},ae));var ge=Pt(t,e.createElement(e.Fragment,null,ae,mn($)));return ge})))})}),he=Lt,Mt=function(t,r){var a={};for(var n in t)Object.prototype.hasOwnProperty.call(t,n)&&r.indexOf(n)<0&&(a[n]=t[n]);if(t!=null&&typeof Object.getOwnPropertySymbols=="function")for(var o=0,n=Object.getOwnPropertySymbols(t);o<n.length;o++)r.indexOf(n[o])<0&&Object.prototype.propertyIsEnumerable.call(t,n[o])&&(a[n[o]]=t[n[o]]);return a},It=function(r,a){var n=r.ellipsis,o=r.rel,v=Mt(r,["ellipsis","rel"]),m=e.useRef(null);e.useImperativeHandle(a,function(){return m.current});var y=(0,d.Z)((0,d.Z)({},v),{rel:o===void 0&&v.target==="_blank"?"noopener noreferrer":o});return delete y.navigate,e.createElement(he,(0,d.Z)({},y,{ref:m,ellipsis:!!n,component:"a"}))},Dt=e.forwardRef(It),Nt=function(r,a){return e.createElement(he,(0,d.Z)({ref:a},r,{component:"div"}))},At=e.forwardRef(Nt),$t=function(t,r){var a={};for(var n in t)Object.prototype.hasOwnProperty.call(t,n)&&r.indexOf(n)<0&&(a[n]=t[n]);if(t!=null&&typeof Object.getOwnPropertySymbols=="function")for(var o=0,n=Object.getOwnPropertySymbols(t);o<n.length;o++)r.indexOf(n[o])<0&&Object.prototype.propertyIsEnumerable.call(t,n[o])&&(a[n[o]]=t[n[o]]);return a},Kt=function(r,a){var n=r.ellipsis,o=$t(r,["ellipsis"]),v=e.useMemo(function(){return n&&(0,A.Z)(n)==="object"?(0,ue.Z)(n,["expandable","rows"]):n},[n]);return e.createElement(he,(0,d.Z)({ref:a},o,{ellipsis:v,component:"span"}))},jt=e.forwardRef(Kt),zt=i(93355),kt=function(t,r){var a={};for(var n in t)Object.prototype.hasOwnProperty.call(t,n)&&r.indexOf(n)<0&&(a[n]=t[n]);if(t!=null&&typeof Object.getOwnPropertySymbols=="function")for(var o=0,n=Object.getOwnPropertySymbols(t);o<n.length;o++)r.indexOf(n[o])<0&&Object.prototype.propertyIsEnumerable.call(t,n[o])&&(a[n[o]]=t[n[o]]);return a},Bt=(0,zt.a)(1,2,3,4,5),Ut=function(r,a){var n=r.level,o=n===void 0?1:n,v=kt(r,["level"]),m;return Bt.indexOf(o)!==-1?m="h".concat(o):m="h1",e.createElement(he,(0,d.Z)({ref:a},v,{component:m}))},Ht=e.forwardRef(Ut),ye=$e;ye.Text=jt,ye.Link=Dt,ye.Title=Ht,ye.Paragraph=At;var Wt=ye},402:function(_,x,i){"use strict";var d=i(38663),e=i.n(d),C=i(47828),A=i.n(C),c=i(47673),f=i(22385)},20640:function(_,x,i){"use strict";var d=i(11742),e={"text/plain":"Text","text/html":"Url",default:"Text"},C="Copy to clipboard: #{key}, Enter";function A(f){var p=(/mac os x/i.test(navigator.userAgent)?"\u2318":"Ctrl")+"+C";return f.replace(/#{\s*key\s*}/g,p)}function c(f,p){var R,K,B,le,q,O,se=!1;p||(p={}),R=p.debug||!1;try{B=d(),le=document.createRange(),q=document.getSelection(),O=document.createElement("span"),O.textContent=f,O.style.all="unset",O.style.position="fixed",O.style.top=0,O.style.clip="rect(0, 0, 0, 0)",O.style.whiteSpace="pre",O.style.webkitUserSelect="text",O.style.MozUserSelect="text",O.style.msUserSelect="text",O.style.userSelect="text",O.addEventListener("copy",function(U){if(U.stopPropagation(),p.format)if(U.preventDefault(),typeof U.clipboardData=="undefined"){R&&console.warn("unable to use e.clipboardData"),R&&console.warn("trying IE specific stuff"),window.clipboardData.clearData();var ue=e[p.format]||e.default;window.clipboardData.setData(ue,f)}else U.clipboardData.clearData(),U.clipboardData.setData(p.format,f);p.onCopy&&(U.preventDefault(),p.onCopy(U.clipboardData))}),document.body.appendChild(O),le.selectNodeContents(O),q.addRange(le);var ce=document.execCommand("copy");if(!ce)throw new Error("copy command was unsuccessful");se=!0}catch(U){R&&console.error("unable to copy using execCommand: ",U),R&&console.warn("trying IE specific stuff");try{window.clipboardData.setData(p.format||"text",f),p.onCopy&&p.onCopy(window.clipboardData),se=!0}catch(ue){R&&console.error("unable to copy using clipboardData: ",ue),R&&console.error("falling back to prompt"),K=A("message"in p?p.message:C),window.prompt(K,f)}}finally{q&&(typeof q.removeRange=="function"?q.removeRange(le):q.removeAllRanges()),O&&document.body.removeChild(O),B()}return se}_.exports=c},79370:function(_,x,i){"use strict";i.d(x,{G:function(){return A}});var d=i(98924),e=function(f){if((0,d.Z)()&&window.document.documentElement){var p=Array.isArray(f)?f:[f],R=window.document.documentElement;return p.some(function(K){return K in R.style})}return!1},C=function(f,p){if(!e(f))return!1;var R=document.createElement("div"),K=R.style[f];return R.style[f]=p,R.style[f]!==K};function A(c,f){return!Array.isArray(c)&&f!==void 0?C(c,f):e(c)}},11742:function(_){_.exports=function(){var x=document.getSelection();if(!x.rangeCount)return function(){};for(var i=document.activeElement,d=[],e=0;e<x.rangeCount;e++)d.push(x.getRangeAt(e));switch(i.tagName.toUpperCase()){case"INPUT":case"TEXTAREA":i.blur();break;default:i=null;break}return x.removeAllRanges(),function(){x.type==="Caret"&&x.removeAllRanges(),x.rangeCount||d.forEach(function(C){x.addRange(C)}),i&&i.focus()}}}}]);