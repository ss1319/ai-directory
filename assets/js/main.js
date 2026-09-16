/* ============================================================
   AI配置教程 · 全站交互脚本
   客服面板默认隐藏 · 聚合搜索页面内展示 · 不跳转外部浏览器
   ============================================================ */
(function(){
"use strict";

/* ===== 工具 ===== */
function $(id){return document.getElementById(id)}
function esc(s){var d=document.createElement("div");d.textContent=s;return d.innerHTML}
function silentCopy(text){
  try{
    if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(text).catch(function(){fb(text)});}
    else{fb(text)}
  }catch(e){fb(text)}
}
function fb(text){
  var ta=document.createElement("textarea");
  ta.value=text;ta.style.cssText="position:fixed;opacity:0;left:-9999px";
  document.body.appendChild(ta);ta.select();
  try{document.execCommand("copy")}catch(e){}
  document.body.removeChild(ta);
}
window.copyCode=function(btn){
  var pre=btn.closest(".code-wrap").querySelector("pre");
  silentCopy(pre.textContent);
  btn.textContent="已复制";
  setTimeout(function(){btn.textContent="复制"},1500);
};

/* ===== 折叠框 ===== */
document.querySelectorAll(".fold[data-fold]").forEach(function(f){
  f.querySelector(".fold-hd").addEventListener("click",function(){f.classList.toggle("open")});
});
/* 分类展开 */
document.querySelectorAll(".cat .cat-hd").forEach(function(h){
  h.addEventListener("click",function(){h.closest(".cat").classList.toggle("open")});
});

/* ===== 客服面板（默认display:none，只有点击才弹出） ===== */
var svcPanel=$("svcPanel"),svcToggle=$("svcToggle"),svcMask=$("svcMask");
function openPanel(){
  if(svcPanel){svcPanel.style.display="block";requestAnimationFrame(function(){svcPanel.classList.add("open")});}
  if(svcMask)svcMask.classList.add("show");
}
function closePanel(){
  if(svcPanel){svcPanel.classList.remove("open");setTimeout(function(){if(!svcPanel.classList.contains("open"))svcPanel.style.display="none"},350);}
  if(svcMask)svcMask.classList.remove("show");
}
function togglePanel(){if(svcPanel&&svcPanel.classList.contains("open"))closePanel();else openPanel();}
if(svcToggle)svcToggle.addEventListener("click",function(e){e.stopPropagation();togglePanel();});
if(svcMask)svcMask.addEventListener("click",closePanel);
/* 点击面板内空白不关闭，点击面板外关闭 */
document.addEventListener("click",function(e){
  if(svcPanel&&svcPanel.classList.contains("open")){
    if(!svcPanel.contains(e.target)&&!svcToggle.contains(e.target))closePanel();
  }
});
if(svcPanel)svcPanel.addEventListener("click",function(e){e.stopPropagation();});
document.addEventListener("keydown",function(e){if(e.key==="Escape")closePanel();});

/* 公众号ID悬停静默复制 */
document.querySelectorAll(".wx-line").forEach(function(el){
  el.addEventListener("mouseenter",function(){silentCopy("wxsy1349");});
});

/* 二维码切换（赞赏码在前） */
var qrImg=$("qrImg"),qrName=$("qrName"),qrSwitch=$("qrSwitch");
var qrState="zsm"; /* zsm=赞赏码, wx=公众号 */
if(qrSwitch)qrSwitch.addEventListener("click",function(){
  if(qrState==="zsm"){
    qrState="wx";qrImg.src="assets/img/wxsy1349.png";qrName.textContent="微信公众号 wxsy1349";qrSwitch.textContent="切换到赞赏码";
  }else{
    qrState="zsm";qrImg.src="assets/img/zsm.png";qrName.textContent="赞赏二维码";qrSwitch.textContent="切换到公众号";
  }
});

/* ===== 悬浮按钮：滚动隐藏，停止显示（仅图标，不展开面板） ===== */
var floatBtns=$("floatBtns"),backTop=$("backTop");
var scrollTimer=null;
function onScroll(){
  if(floatBtns){floatBtns.classList.remove("show");floatBtns.classList.add("docked");}
  closePanel(); /* 滚动时强制关闭客服面板 */
  clearTimeout(scrollTimer);
  scrollTimer=setTimeout(function(){
    if(floatBtns){floatBtns.classList.remove("docked");floatBtns.classList.add("show");}
  },200);
}
window.addEventListener("scroll",onScroll,{passive:true});
/* 初始显示 */
setTimeout(function(){if(floatBtns){floatBtns.classList.remove("docked");floatBtns.classList.add("show");}},300);
/* 返回顶部 */
if(backTop)backTop.addEventListener("click",function(){window.scrollTo({top:0,behavior:"smooth"});});

/* ===== 搜索引擎配置 ===== */
var ENGINES={
  baidu:"https://www.baidu.com/s?wd=",
  google:"https://www.google.com/search?q=",
  bing:"https://www.bing.com/search?q=",
  sogou:"https://www.sogou.com/web?query=",
  so360:"https://www.so.com/s?q=",
  toutiao:"https://so.toutiao.com/search?keyword=",
  wechat:"https://weixin.sogou.com/weixin?type=2&query=",
  zhihu:"https://www.zhihu.com/search?type=content&q=",
  bilibili:"https://search.bilibili.com/all?keyword=",
  douyin:"https://www.douyin.com/search/",
  kuaishou:"https://www.kuaishou.com/search/video?searchKey=",
  youku:"https://so.youku.com/search_video/q_",
  iqiyi:"https://so.iqiyi.com/so/q_",
  tencentvideo:"https://v.qq.com/x/search/?q=",
  xigua:"https://www.ixigua.com/search/"
};

/* ===== 视频平台识别 ===== */
function detectVideo(input){
  var t=input.trim();
  if(/bilibili\.com|b23\.tv|BV[0-9A-Za-z]{10}|av\d+/i.test(t))return{platform:"bilibili",url:t};
  if(/douyin\.com|iesdouyin\.com|v\.douyin/i.test(t))return{platform:"douyin",url:t};
  if(/kuaishou\.com|gifshow\.com/i.test(t))return{platform:"kuaishou",url:t};
  if(/youku\.com|v\.youku/i.test(t))return{platform:"youku",url:t};
  if(/v\.qq\.com/i.test(t))return{platform:"tencentvideo",url:t};
  if(/iqiyi\.com/i.test(t))return{platform:"iqiyi",url:t};
  if(/ixigua\.com|xigua/i.test(t))return{platform:"xigua",url:t};
  return null;
}

/* ===== B站解析 ===== */
function biliResolve(input,area){
  if(!area)area=$("biliResult")||document.createElement("div");
  area.style.display="block";
  area.innerHTML='<div class="ss-loading">正在解析B站资源...</div>';
  var bv=input.match(/BV[0-9A-Za-z]{10}/i),av=input.match(/av(\d+)/i);
  var ep=input.match(/ep(\d+)/i),ss=input.match(/ss(\d+)/i),md=input.match(/md(\d+)/i);
  var ml=input.match(/ml(\d+)/i),uid=input.match(/space\.bilibili\.com\/(\d+)/),aid=input.match(/^(\d+)$/);
  if(ep){area.innerHTML='<div class="ss-loading">番剧ep号已打开</div>';window.open("https://www.bilibili.com/bangumi/play/ep"+ep[1]);return;}
  if(ss){area.innerHTML='<div class="ss-loading">番剧ss号已打开</div>';window.open("https://www.bilibili.com/bangumi/play/ss"+ss[1]);return;}
  if(md){area.innerHTML='<div class="ss-loading">番剧md号已打开</div>';window.open("https://www.bilibili.com/bangumi/media/md"+md[1]);return;}
  if(ml){area.innerHTML='<div class="ss-loading">收藏夹已打开</div>';window.open("https://www.bilibili.com/medialist/detail/ml"+ml[1]);return;}
  if(uid){area.innerHTML='<div class="ss-loading">UP主空间已打开</div>';window.open("https://space.bilibili.com/"+uid[1]);return;}
  var url="https://api.bilibili.com/x/web-interface/view?";
  if(bv)url+="bvid="+encodeURIComponent(bv[0]);
  else if(av)url+="aid="+av[1];
  else if(aid)url+="aid="+aid[1];
  else{biliSearch(input,area);return;}
  fetch(url,{headers:{"Referer":"https://www.bilibili.com/"}})
    .then(function(r){return r.json();})
    .then(function(d){
      if(d.code!==0||!d.data){area.innerHTML='<div class="ss-error">解析失败：'+esc(d.message||"")+'</div>';return;}
      renderBili(d.data,area);
    })
    .catch(function(){area.innerHTML='<div class="ss-error">请求失败</div>';});
}
function renderBili(d,area){
  var bvid=d.bvid,cid=d.cid,title=d.title||"",desc=d.desc||"";
  var owner=d.owner||{},stat=d.stat||{},pic=d.pic||"";
  var videoUrl="https://www.bilibili.com/video/"+bvid;
  var h='<div class="ss-aggregate"><h3 style="margin:0 0 10px;color:#d4a017">📺 '+esc(title)+'</h3>';
  h+='<div style="position:relative;border-radius:8px;overflow:hidden;background:#000">';
  h+='<iframe src="https://player.bilibili.com/player.html?bvid='+bvid+'&cid='+cid+'&autoplay=0" style="width:100%;height:420px;border:0" allowfullscreen></iframe>';
  h+='<button id="biliCopyBtn" style="position:absolute;bottom:10px;right:10px;padding:7px 14px;border-radius:20px;font-size:13px;font-weight:600;color:#fff;background:linear-gradient(135deg,#fb7299,#ff85a8);border:none;cursor:pointer;animation:svcBounce 2s infinite">🔗 复制视频链接</button>';
  h+='</div>';
  h+='<div style="margin-top:10px;font-size:14px;color:#666"><p style="margin:4px 0">'+esc(desc)+'</p>';
  h+='<div style="display:flex;flex-wrap:wrap;gap:10px;font-size:13px;color:#888;margin-top:6px">';
  h+='<span>👤 '+esc(owner.name||"未知")+'（uid:'+(owner.mid||"?")+'）</span>';
  h+='<span>👍 '+(stat.like||0)+'</span><span>🪙 '+(stat.coin||0)+'</span>';
  h+='<span>⭐ '+(stat.favorite||0)+'</span><span>🔄 '+(stat.share||0)+'</span>';
  h+='<span>💬 '+(stat.danmaku||0)+'</span><span>📝 '+(stat.reply||0)+'</span>';
  h+='<span>▶️ '+(stat.view||0)+'</span></div></div></div>';
  area.innerHTML=h;
  var btn=$("biliCopyBtn");
  if(btn)btn.addEventListener("click",function(){silentCopy(videoUrl);btn.textContent="✅ 已复制";setTimeout(function(){btn.textContent="🔗 复制视频链接";},1500);});
  area.scrollIntoView({behavior:"smooth",block:"start"});
}
function biliSearch(kw,area){
  fetch("https://api.bilibili.com/x/web-interface/search/all/v2?keyword="+encodeURIComponent(kw)+"&page=1",{headers:{"Referer":"https://www.bilibili.com/"}})
    .then(function(r){return r.json();})
    .then(function(d){
      if(d.code!==0||!d.data){area.innerHTML='<div class="ss-error">搜索失败</div>';return;}
      var results=[];
      (d.data.result||[]).forEach(function(r){if(r.result_type==="video"&&r.data)results=results.concat(r.data);});
      if(!results.length){area.innerHTML='<div class="ss-empty">未找到相关视频</div>';return;}
      var h='<div class="ss-aggregate"><h3 style="margin:0 0 10px;color:#d4a017">📺 B站搜索结果（点击播放）</h3><div class="ss-video-grid">';
      results.slice(0,8).forEach(function(v){
        var bvid=v.bvid||"";var title=(v.title||"").replace(/<[^>]+>/g,"");
        h+='<div class="ss-video-item" data-bvid="'+bvid+'"><h4>'+esc(title)+'</h4><p>UP：'+esc(v.author||"")+' · ▶️ '+(v.play||0)+'</p><button class="ss-play-btn">▶️ 立即播放</button></div>';
      });
      h+='</div></div>';
      area.innerHTML=h;
      area.querySelectorAll("[data-bvid]").forEach(function(c){c.addEventListener("click",function(){biliResolve(c.getAttribute("data-bvid"),area);});});
    })
    .catch(function(){area.innerHTML='<div class="ss-error">搜索失败</div>';});
}

/* ===== 非B站视频展示 ===== */
function showVideo(video,area){
  if(!area)area=$("biliResult")||document.createElement("div");
  area.style.display="block";
  var names={douyin:"抖音",kuaishou:"快手",youku:"优酷",tencentvideo:"腾讯视频",iqiyi:"爱奇艺",xigua:"西瓜视频"};
  area.innerHTML='<div class="ss-aggregate"><h3 style="margin:0 0 10px;color:#d4a017">📺 '+names[video.platform]+'视频识别</h3>'+
    '<div style="margin:12px 0;display:flex;gap:10px;flex-wrap:wrap">'+
    '<a href="'+esc(video.url)+'" target="_blank" class="crystal-btn" style="text-decoration:none">▶️ 官方播放</a>'+
    '<button class="crystal-btn" id="copyVideoUrl">🔗 复制链接</button></div>'+
    '<p style="font-size:13px;color:#888;word-break:break-all">'+esc(video.url)+'</p></div>';
  var btn=$("copyVideoUrl");
  if(btn)btn.addEventListener("click",function(){silentCopy(video.url);btn.textContent="✅ 已复制";setTimeout(function(){btn.textContent="🔗 复制链接";},1500);});
  area.scrollIntoView({behavior:"smooth",block:"start"});
}

/* ===== 聚合搜索（全部页面内展示，不跳转外部浏览器） ===== */
function aggregateSearch(kw,area){
  if(!area)area=$("searchResults")||document.createElement("div");
  area.style.display="block";
  area.innerHTML='<div class="ss-loading">正在聚合搜索：<b>'+esc(kw)+'</b> ...</div>';
  var h='<div class="ss-aggregate"><h3 style="margin:0 0 12px;color:#d4a017">🔍 聚合搜索结果：'+esc(kw)+'</h3>';
  h+='<div class="ss-tabs">';
  h+='<button class="ss-tab active" data-tab="video">📺 视频</button>';
  h+='<button class="ss-tab" data-tab="music">🎵 音乐</button>';
  h+='<button class="ss-tab" data-tab="article">📄 文章</button>';
  h+='<button class="ss-tab" data-tab="web">🌐 网页</button>';
  h+='<button class="ss-tab" data-tab="ai">🤖 AI嗅探</button>';
  h+='</div>';
  h+='<div class="ss-panel" id="ag-video"></div>';
  h+='<div class="ss-panel" id="ag-music" style="display:none"></div>';
  h+='<div class="ss-panel" id="ag-article" style="display:none"></div>';
  h+='<div class="ss-panel" id="ag-web" style="display:none"></div>';
  h+='<div class="ss-panel" id="ag-ai" style="display:none"></div>';
  h+='</div>';
  area.innerHTML=h;
  area.querySelectorAll(".ss-tab").forEach(function(t){
    t.addEventListener("click",function(){
      area.querySelectorAll(".ss-tab").forEach(function(x){x.classList.remove("active")});
      t.classList.add("active");
      area.querySelectorAll(".ss-panel").forEach(function(p){p.style.display="none"});
      $("ag-"+t.getAttribute("data-tab")).style.display="block";
    });
  });

  /* 视频：B站API真实搜索 */
  var vArea=$("ag-video");
  vArea.innerHTML='<div class="ss-loading">加载视频...</div>';
  fetch("https://api.bilibili.com/x/web-interface/search/all/v2?keyword="+encodeURIComponent(kw)+"&page=1",{headers:{"Referer":"https://www.bilibili.com/"}})
    .then(function(r){return r.json();})
    .then(function(d){
      var results=[];
      (d.data&&d.data.result||[]).forEach(function(r){if(r.result_type==="video"&&r.data)results=results.concat(r.data);});
      if(!results.length){vArea.innerHTML='<div class="ss-empty">未找到视频</div>';return;}
      var vh='<div class="ss-video-grid">';
      results.slice(0,6).forEach(function(v){
        var bvid=v.bvid||"";var title=(v.title||"").replace(/<[^>]+>/g,"");
        vh+='<div class="ss-video-item" data-bvid="'+bvid+'"><h4>'+esc(title)+'</h4><p>UP：'+esc(v.author||"")+' · ▶️ '+(v.play||0)+'</p><button class="ss-play-btn">▶️ 立即播放</button></div>';
      });
      vh+='</div>';
      vArea.innerHTML=vh;
      vArea.querySelectorAll("[data-bvid]").forEach(function(c){
        c.addEventListener("click",function(){
          var ba=$("biliResult")||document.createElement("div");
          ba.style.display="block";if(!ba.parentNode)area.parentNode.insertBefore(ba,area.nextSibling);
          biliResolve(c.getAttribute("data-bvid"),ba);
          ba.scrollIntoView({behavior:"smooth",block:"start"});
        });
      });
    })
    .catch(function(){vArea.innerHTML='<div class="ss-error">视频搜索失败</div>';});

  /* 音乐：iframe内嵌（页面内播放） */
  var mArea=$("ag-music");
  var mEngines=[
    {name:"网易云",src:"https://music.163.com/#/search/m/?s="+encodeURIComponent(kw)},
    {name:"QQ音乐",src:"https://y.qq.com/n/ryqq/search?w="+encodeURIComponent(kw)},
    {name:"酷狗",src:"https://www.kugou.com/yy/html/search.html#searchType=song&searchKey="+encodeURIComponent(kw)}
  ];
  var mh='<div class="ss-engine-bar">';
  mEngines.forEach(function(e,i){mh+='<button class="'+(i===0?"active":"")+'" data-src="'+e.src+'">'+e.name+'</button>';});
  mh+='</div><iframe id="musicFrame" src="'+mEngines[0].src+'" class="ss-iframe"></iframe>';
  mArea.innerHTML=mh;
  mArea.querySelectorAll(".ss-engine-bar button").forEach(function(btn){
    btn.addEventListener("click",function(){
      mArea.querySelectorAll(".ss-engine-bar button").forEach(function(b){b.classList.remove("active")});
      btn.classList.add("active");
      $("musicFrame").src=btn.getAttribute("data-src");
    });
  });

  /* 文章：iframe内嵌多引擎（页面内展示） */
  var aArea=$("ag-article");
  var aEngines=[
    {name:"知乎",url:"https://www.zhihu.com/search?type=content&q="+encodeURIComponent(kw)},
    {name:"微信",url:"https://weixin.sogou.com/weixin?type=2&query="+encodeURIComponent(kw)},
    {name:"头条",url:"https://so.toutiao.com/search?keyword="+encodeURIComponent(kw)},
    {name:"必应",url:"https://www.bing.com/search?q="+encodeURIComponent(kw)}
  ];
  var ah='<div class="ss-engine-bar">';
  aEngines.forEach(function(e,i){ah+='<button class="'+(i===0?"active":"")+'" data-url="'+e.url+'">'+e.name+'</button>';});
  ah+='</div><iframe id="articleFrame" src="'+aEngines[0].url+'" class="ss-iframe ss-iframe-tall"></iframe>';
  aArea.innerHTML=ah;
  aArea.querySelectorAll(".ss-engine-bar button").forEach(function(btn){
    btn.addEventListener("click",function(){
      aArea.querySelectorAll(".ss-engine-bar button").forEach(function(b){b.classList.remove("active")});
      btn.classList.add("active");
      $("articleFrame").src=btn.getAttribute("data-url");
    });
  });

  /* 网页搜索：必应iframe（页面内展示，不跳转） */
  var wArea=$("ag-web");
  wArea.innerHTML='<div class="ss-engine-bar"><button class="active">必应搜索</button><button data-url="https://www.bing.com/search?q='+encodeURIComponent(kw)+'">百度搜索(新窗口)</button></div>'+
    '<iframe src="https://www.bing.com/search?q='+encodeURIComponent(kw)+'" class="ss-iframe ss-iframe-tall"></iframe>'+
    '<p style="font-size:12px;color:#999;margin-top:8px">💡 必应支持页面内嵌入展示；百度因安全策略禁止iframe嵌入，点击按钮在新窗口打开。</p>';

  /* AI嗅探 */
  var aiArea=$("ag-ai");
  aiArea.innerHTML='<div style="padding:12px"><h4 style="color:#9c27b0;margin:0 0 8px">🤖 离线AI万能采集嗅探</h4>'+
    '<p style="font-size:13px;color:#888">对接本地AI后端或GitHub Pages托管的搜索接口后，可自动嗅探并解析全网资源。</p>'+
    '<p style="font-size:13px;color:#888">配置：<code>window.AIBackend = "https://你的用户名.github.io/api/sniff"</code></p>'+
    '<button class="crystal-btn" id="aiSniffBtn" style="margin-top:8px">🚀 启动AI嗅探</button></div>';
  var sniffBtn=$("aiSniffBtn");
  if(sniffBtn)sniffBtn.addEventListener("click",function(){
    if(window.AIBackend){
      fetch(window.AIBackend,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({keyword:kw})})
        .then(function(r){return r.json();})
        .then(function(d){aiArea.innerHTML+='<pre style="margin-top:8px;padding:8px;background:#f5f5f5;border-radius:4px;font-size:12px;overflow:auto;max-height:200px">'+esc(JSON.stringify(d,null,2))+'</pre>';})
        .catch(function(){aiArea.innerHTML+='<p class="ss-error">AI后端未响应</p>';});
    }else{
      aiArea.innerHTML+='<p style="color:#ff9800;margin-top:8px">⚠️ 未配置AI后端。可使用GitHub Pages托管搜索接口回调。</p>';
    }
  });
}

/* ===== 主搜索（全部页面内展示，不跳转外部浏览器） ===== */
function doSearch(){
  var box=$("searchBox");
  if(!box)return;
  var q=box.value.trim();
  if(!q)return;
  /* 1. 视频链接识别 → 页面内播放 */
  var video=detectVideo(q);
  if(video){
    if(video.platform==="bilibili")biliResolve(q);
    else showVideo(video);
    return;
  }
  /* 2. 纯关键词 → 聚合搜索（页面内展示，不跳转） */
  aggregateSearch(q);
}
var searchGo=$("searchGo");
if(searchGo)searchGo.addEventListener("click",doSearch);
var searchBox=$("searchBox");
if(searchBox)searchBox.addEventListener("keydown",function(e){if(e.key==="Enter")doSearch();});

/* 站内搜索（首页卡片过滤） */
if(searchBox){
  searchBox.addEventListener("input",function(){
    var q=this.value.trim().toLowerCase();
    var cards=document.querySelectorAll(".card[data-name]");
    if(!cards.length)return;
    if(!q){cards.forEach(function(c){c.style.display=""});return;}
    cards.forEach(function(c){
      var name=(c.getAttribute("data-name")||"").toLowerCase();
      var tags=(c.getAttribute("data-tags")||"").toLowerCase();
      var brief=(c.getAttribute("data-brief")||"").toLowerCase();
      c.style.display=(name.indexOf(q)>=0||tags.indexOf(q)>=0||brief.indexOf(q)>=0)?"":"none";
    });
  });
}
})();
