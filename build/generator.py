# -*- coding: utf-8 -*-
"""AI配置教程全站生成器 - 金色玻璃水晶质感"""
import os

BASE = r"E:\000000已设计好的完整HTML源码\AI配置教程"

# 客服面板HTML（8个彩色按钮 + 公众号wxsy1349 + 赞赏码在前 + 1px滚动条）
SVC_PANEL = '''
<div class="svc-mask" id="svcMask"></div>
<div class="svc-panel glass-strong" id="svcPanel">
  <div class="panel-inner">
    <div class="panel-title">💬 联系客服 · 资源导航</div>
    <!-- 赞赏码在前 -->
    <div class="qr-box">
      <div class="qr-frame"><img id="qrImg" src="assets/img/zsm.png" alt="赞赏码" onerror="this.src='assets/img/wxsy1349.png'"></div>
      <div class="qr-name" id="qrName">赞赏二维码</div>
      <button class="qr-switch" id="qrSwitch" type="button">切换到公众号</button>
    </div>
    <p class="qr-tip">欢迎自愿赞赏支持作者</p>
    <!-- 公众号彩色动画立体大字 -->
    <div class="wx-id" title="鼠标移过自动复制">
      <span class="wx-label">微信公众号</span>
      <span class="wx-line">wxsy1349</span>
    </div>
    <!-- 8个彩色超链接按钮 -->
    <div class="svc-links">
      <a class="svc-link c1" href="https://app.kwaixiaodian.com/page/kwaishop-store-c-frame-h5/frame?layoutType=4&hyId=kwaishop-store-c-frame-h5&sellerId=1865090819&authorId=1865090819&carrierType=29&carrierId=fva0b4kfnGw&entrance=xdhtlj" target="_blank">🛒 快手小店</a>
      <a class="svc-link c2" href="https://pd.qq.com/s/24yp7y38f" target="_blank">💬 腾讯频道</a>
      <a class="svc-link c3" href="https://www.zhihu.com/people/z6391" target="_blank">💡 知乎</a>
      <a class="svc-link c4" href="https://qm.qq.com/q/VHeRTTdQcu" target="_blank">👥 QQ群</a>
      <a class="svc-link c5" href="https://bolt.cello.so/lsypink3QTR" target="_blank">💻 在线AI编程</a>
      <a class="svc-link c6" href="https://api.u-claw.org/register?aff=9OLG" target="_blank">🐙 OpenClaw</a>
      <a class="svc-link c7" href="https://weibo.com/zdzqxt" target="_blank">📢 微博</a>
      <a class="svc-link c8" href="https://txc.qq.com/embed/367382/new-post/" target="_blank">✉️ 欢迎留言</a>
    </div>
    <div class="svc-bottom">AI配置教程 · 全国AI智能体大全 · 持续更新中</div>
  </div>
</div>
<!-- 悬浮按钮：客服在上（彩色跳动），返回顶部在下（🚀），32x32贴右侧边缘 -->
<div class="float-btns docked" id="floatBtns">
  <button class="fab" id="svcToggle" type="button" title="点击打开客服面板">💬</button>
  <button class="fab" id="backTop" type="button" title="返回顶部">🚀</button>
</div>
'''

FLOAT_BTNS_SINGLE = '''
<div class="svc-mask" id="svcMask"></div>
<div class="svc-panel glass-strong" id="svcPanel">
  <div class="panel-inner">
    <div class="panel-title">💬 联系客服 · 资源导航</div>
    <div class="qr-box">
      <div class="qr-frame"><img id="qrImg" src="../assets/img/zsm.png" alt="赞赏码" onerror="this.src='../assets/img/wxsy1349.png'"></div>
      <div class="qr-name" id="qrName">赞赏二维码</div>
      <button class="qr-switch" id="qrSwitch" type="button">切换到公众号</button>
    </div>
    <p class="qr-tip">欢迎自愿赞赏支持作者</p>
    <div class="wx-id" title="鼠标移过自动复制">
      <span class="wx-label">微信公众号</span>
      <span class="wx-line">wxsy1349</span>
    </div>
    <div class="svc-links">
      <a class="svc-link c1" href="https://app.kwaixiaodian.com/page/kwaishop-store-c-frame-h5/frame?layoutType=4&hyId=kwaishop-store-c-frame-h5&sellerId=1865090819&authorId=1865090819&carrierType=29&carrierId=fva0b4kfnGw&entrance=xdhtlj" target="_blank">🛒 快手小店</a>
      <a class="svc-link c2" href="https://pd.qq.com/s/24yp7y38f" target="_blank">💬 腾讯频道</a>
      <a class="svc-link c3" href="https://www.zhihu.com/people/z6391" target="_blank">💡 知乎</a>
      <a class="svc-link c4" href="https://qm.qq.com/q/VHeRTTdQcu" target="_blank">👥 QQ群</a>
      <a class="svc-link c5" href="https://bolt.cello.so/lsypink3QTR" target="_blank">💻 在线AI编程</a>
      <a class="svc-link c6" href="https://api.u-claw.org/register?aff=9OLG" target="_blank">🐙 OpenClaw</a>
      <a class="svc-link c7" href="https://weibo.com/zdzqxt" target="_blank">📢 微博</a>
      <a class="svc-link c8" href="https://txc.qq.com/embed/367382/new-post/" target="_blank">✉️ 欢迎留言</a>
    </div>
    <div class="svc-bottom">AI配置教程 · 全国AI智能体大全 · 持续更新中</div>
  </div>
</div>
<div class="float-btns docked" id="floatBtns">
  <button class="fab" id="svcToggle" type="button" title="点击打开客服面板">💬</button>
  <button class="fab" id="backTop" type="button" title="返回顶部">🚀</button>
</div>
'''

def page_head(title, desc, crumb, css_path="../assets/css/main.css"):
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · AI智能体搭建与exe/apk后端Key配置教程</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="{css_path}">
</head>
<body class="ai-page">
<div class="bg-layer" aria-hidden="true"><i class="blob b1"></i><i class="blob b2"></i><i class="blob b3"></i><i class="blob b4"></i></div>
<header class="topbar glass">
  <a class="logo" href="../index.html">🏠 AI配置教程 · 智能索引</a>
  <span class="crumb">{crumb}</span>
</header>
<main class="ai-main">
'''

def page_tail(js_path="../assets/js/main.js"):
    return f'''</main>
{FLOAT_BTNS_SINGLE}
<script src="{js_path}"></script>
</body>
</html>'''

def code_block(title, lang, code, cid):
    return f'''<div class="code-wrap">
<div class="code-bar"><span class="code-t">{title}</span><span class="code-lang">{lang}</span><button class="copy-btn" type="button" onclick="copyCode(this)">复制</button></div>
<pre><code id="{cid}">{code}</code></pre>
</div>'''

def link_table(rows):
    h = '<table class="link-table">'
    for k, v in rows:
        h += f'<tr><th>{k}</th><td>{v}</td></tr>'
    h += '</table>'
    return h

def render_steps(steps):
    h = '<div class="steps">'
    for i, (title, txt) in enumerate(steps, 1):
        h += f'<div class="step"><div class="step-no">{i}</div><div class="step-body"><h4>{title}</h4><div class="step-txt">{txt}</div></div></div>'
    h += '</div>'
    return h

# AI数据（72个）
AIS = [
    # 离线部署型 (8)
    {"cat":"offline","slug":"ollama","name":"Ollama","ico":"🦙","tags":["离线","本地大模型","开源","免费","exe/apk内嵌"],
     "brief":"一键在本地运行Llama3、Qwen、DeepSeek等大模型，支持Windows/Mac/Linux，完全离线免费。",
     "links":[("官网地址",'<a href="https://ollama.com" target="_blank">https://ollama.com</a>'),("下载地址",'<a href="https://ollama.com/download" target="_blank">https://ollama.com/download</a>'),("开源仓库",'<a href="https://github.com/ollama/ollama" target="_blank">GitHub</a>'),("社群",'<a href="https://discord.gg/ollama" target="_blank">Discord</a>'),("微信公众号","Ollama"),("微信小程序","暂无")],
     "feat":["支持Llama3、Qwen2、DeepSeek等数十种开源模型","一条命令拉取并运行模型","提供REST API可被exe/apk内嵌调用","4GB内存即可跑7B模型","完全离线数据不出本机"],
     "intro":"Ollama是目前最流行的本地大模型运行工具，把模型下载、量化、运行封装成一条命令。安装后执行ollama run qwen2即可对话。提供http://localhost:11434的REST API，任何程序都能通过HTTP调用。",
     "steps":[("下载安装","访问ollama.com/download，选择对应系统版本下载安装。Windows版双击安装即可，安装后自动后台运行。"),("拉取模型","打开命令行执行 ollama pull qwen2 拉取通义千问2模型（约4.7GB）。"),("运行对话","执行 ollama run qwen2 即可在终端对话，输入/bye退出。"),("验证API","浏览器打开http://localhost:11434显示Ollama is running即正常。"),("开机自启","Windows版默认开机自启，Linux执行systemctl enable ollama。")],
     "cb_code":'''import requests

def on_ai_reply(text):
    """回调函数：AI回答后调用此函数"""
    print("AI回答:", text)

def ask(prompt, model="qwen2"):
    r = requests.post("http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": False}, timeout=120)
    reply = r.json()["response"]
    on_ai_reply(reply)
    return reply

ask("写一首关于秋天的诗")'''},
    {"cat":"offline","slug":"lmstudio","name":"LM Studio","ico":"🏠","tags":["离线","图形界面","本地模型","免费"],
     "brief":"图形化界面运行本地大模型，支持GGUF格式模型，内置模型市场和API服务。",
     "links":[("官网地址",'<a href="https://lmstudio.ai" target="_blank">https://lmstudio.ai</a>'),("下载地址",'<a href="https://lmstudio.ai/download" target="_blank">下载</a>'),("开源仓库","闭源免费"),("社群","Discord社区"),("微信公众号","LM Studio"),("微信小程序","暂无")],
     "feat":["图形化界面，无需命令行","内置模型市场，一键下载","支持OpenAI兼容API","可同时加载多个模型","完全离线运行"],
     "intro":"LM Studio是一款图形化本地大模型运行工具，适合不熟悉命令行的用户。内置模型搜索和下载功能，支持加载GGUF格式模型，一键启动OpenAI兼容的API服务器。",
     "steps":[("下载安装","访问lmstudio.ai下载安装包，双击安装。"),("搜索模型","打开软件，在左侧搜索栏输入模型名称（如qwen2）。"),("下载模型","点击模型卡片的Download按钮下载。"),("加载对话","切换到Chat页面，选择已下载的模型开始对话。"),("启动API","在Developer页面启动本地服务器，端口默认1234。")],
     "cb_code":'''import requests

# LM Studio默认端口1234，兼容OpenAI格式
def ask_lmstudio(prompt):
    r = requests.post("http://localhost:1234/v1/chat/completions",
        json={"model": "local-model", "messages": [{"role": "user", "content": prompt}]})
    return r.json()["choices"][0]["message"]["content"]

print(ask_lmstudio("你好"))'''},
    # 更多AI省略，用循环生成精简版
]

# 批量生成剩余AI（精简版，确保72个）
MORE_AIS = [
    ("offline","llama-cpp","llama.cpp","⚡","离线推理引擎","C++实现的高性能本地推理引擎，支持CPU/GPU加速。"),
    ("offline","gpt4all","GPT4All","💬","离线对话","桌面端离线AI对话工具，支持多种模型。"),
    ("offline","koboldcpp","KoboldCpp","📖","离线小说","专为小说创作优化的本地推理工具。"),
    ("offline","text-generation-webui","Text Generation WebUI","🌐","离线WebUI","Gradio界面的本地模型运行平台。"),
    ("offline","vllm","vLLM","🚀","离线推理服务","高吞吐量推理服务，支持OpenAI API。"),
    ("offline","xinference","Xinference","🔧","离线模型平台","开源模型推理和部署平台。"),
    ("chat","deepseek","DeepSeek","🔮","对话型","深度求索推出的对话AI，支持代码和推理。"),
    ("chat","tongyi","通义千问","☁️","对话型","阿里云推出的大语言模型。"),
    ("chat","wenxin","文心一言","📝","对话型","百度推出的知识增强大模型。"),
    ("chat","doubao","豆包","🫘","对话型","字节跳动推出的AI助手。"),
    ("chat","kimi","Kimi","🌙","对话型","月之暗面推出的超长上下文AI。"),
    ("chat","zhipu","智谱清言","🧠","对话型","智谱AI推出的大模型助手。"),
    ("chat","hunyuan","混元","🎯","对话型","腾讯推出的大语言模型。"),
    ("chat","xinghuo","讯飞星火","🔥","对话型","科大讯飞推出的认知大模型。"),
    ("chat","chatglm","ChatGLM","💎","对话型","智谱开源的对话模型。"),
    ("chat","baichuan","百川","🌊","对话型","百川智能推出的大模型。"),
    ("chat","minimax","MiniMax","🎭","对话型","MiniMax推出的对话AI。"),
    ("chat","moonshot","月之暗面","🌙","对话型","Kimi背后的公司。"),
    ("chat","360gpt","360智脑","🛡️","对话型","360推出的大模型。"),
    ("chat","skylark","字节豆包","🫘","对话型","字节跳动的大模型。"),
    ("api","openai","OpenAI API","🤖","API自定义","全球最流行的AI API，支持GPT系列模型。"),
    ("api","anthropic","Anthropic Claude","🧩","API自定义","Claude系列模型API。"),
    ("api","azure","Azure OpenAI","☁️","API自定义","微软Azure托管的OpenAI服务。"),
    ("api","openrouter","OpenRouter","🔀","API自定义","聚合数百种模型的API路由。"),
    ("api","siliconflow","硅基流动","💎","API自定义","国内大模型API聚合平台。"),
    ("api","dashscope","阿里云百炼","🔮","API自定义","阿里云模型服务平台。"),
    ("api","zhipu-api","智谱API","🧠","API自定义","智谱AI开放平台。"),
    ("api","moonshot-api","Kimi API","🌙","API自定义","月之暗面开放平台。"),
    ("api","deepseek-api","DeepSeek API","🔮","API自定义","深度求索开放平台。"),
    ("api","stepfun","阶跃星辰","⭐","API自定义","阶跃星辰大模型API。"),
    ("api","baichuan-api","百川API","🌊","API自定义","百川智能开放平台。"),
    ("api","minimax-api","MiniMax API","🎭","API自定义","MiniMax开放平台。"),
    ("agent","coze","扣子Coze","🎯","Agent智能体","字节跳动推出的AI智能体搭建平台。"),
    ("agent","dify","Dify","🔧","Agent智能体","开源LLM应用开发平台。"),
    ("agent","langchain","LangChain","⛓️","Agent框架","最流行的LLM应用开发框架。"),
    ("agent","autogen","AutoGen","🤝","Agent框架","微软多智能体协作框架。"),
    ("agent","crewai","CrewAI","👥","Agent框架","角色化多智能体协作框架。"),
    ("agent","n8n","n8n","🔄","Agent自动化","开源工作流自动化平台。"),
    ("agent","zapier","Zapier","⚡","Agent自动化","无代码自动化平台。"),
    ("agent","make","Make","🔧","Agent自动化","可视化自动化平台。"),
    ("agent","ifttt","IFTTT","🔗","Agent自动化","简单的自动化连接平台。"),
    ("agent","openclaw","OpenClaw虾盘云","🐙","Agent智能体","云端AI聚合服务，支持MCP协议。"),
    ("agent","fastgpt","FastGPT","🚀","Agent智能体","开源知识库问答平台。"),
    ("agent","anything-llm","AnythingLLM","📚","Agent智能体","开源文档问答助手。"),
    ("rpa","yingdao","影刀RPA","🎭","RPA自动化","国内领先的RPA工具，支持AI能力。"),
    ("rpa","shizai","实在智能Agent","🤖","RPA+AI","AI驱动的RPA平台。"),
    ("rpa","uibot","UiBot","🔧","RPA自动化","来也科技RPA平台。"),
    ("rpa","powerautomate","Power Automate","⚡","RPA自动化","微软RPA平台。"),
    ("rpa","uipath","UiPath","🏢","RPA自动化","全球领先的RPA平台。"),
    ("rpa","automationanywhere","Automation Anywhere","🌐","RPA自动化","企业级RPA平台。"),
    ("production","pixverse","PixVerse","🎬","生产类-AI视频","AI视频生成工具。"),
    ("production","miaoda","秒哒剪辑","✂️","生产类-剪辑","AI全能剪辑助手。"),
    ("production","feitui","沸推AI","📈","生产类-营销","AI营销内容生成。"),
    ("production","feiying","飞影数字人","🎤","生产类-数字人","AI数字人视频生成。"),
    ("production","liblib","LiblibAI","🎨","生产类-生图","AI绘画创作平台。"),
    ("production","aipy","爱派Aipy","🖼️","生产类-设计","AI设计工具。"),
    ("production","typefun","TypeFun","⌨️","生产类-打字","AI助力打字学习。"),
    ("production","bianjie","边界AI","💻","生产类-桌面","AI电脑桌面助手。"),
    ("production","workbuddy","腾讯WorkBuddy","💼","生产类-办公","腾讯AI办公助手。"),
    ("production","wenxin-vegan","文心素食助手","🥗","生产类-垂直","素食领域AI助手。"),
    ("production","capcut","剪映","🎬","生产类-剪辑","字节跳动视频剪辑工具。"),
    ("production","canva","可画Canva","🎨","生产类-设计","在线设计平台。"),
    ("production","notionai","Notion AI","📝","生产类-笔记","AI笔记助手。"),
    ("production","gamma","Gamma","📊","生产类-PPT","AI演示文稿生成。"),
    ("production","runway","Runway","🎥","生产类-视频","专业AI视频编辑。"),
    ("code","bolt","Bolt","⚡","编程类","在线AI编程助手。"),
    ("code","githubcopilot","GitHub Copilot","🐙","编程类","GitHub AI编程助手。"),
    ("code","cursor","Cursor","🖱️","编程类","AI代码编辑器。"),
    ("code","trae","Trae","💻","编程类","字节AI编程IDE。"),
    ("code","codegeex","CodeGeeX","🧩","编程类","智谱AI编程助手。"),
    ("code","tongyi-lingma","通义灵码","🔮","编程类","阿里云AI编程助手。"),
    ("code","codeium","Codeium","✨","编程类","免费AI编程助手。"),
]

CAT_NAMES = {
    "offline":"免费离线·本地部署型AI",
    "chat":"一般普通对话型AI",
    "api":"可申请Tracking ID和Key的自定义模型类AI",
    "agent":"Agent全自动化工作型AI",
    "rpa":"RPA类AI",
    "production":"生产类AI",
    "code":"AI编程助手类"
}

def gen_ai_page(ai):
    """生成AI单页"""
    slug = ai["slug"]
    name = ai["name"]
    cat = ai["cat"]
    crumb = CAT_NAMES.get(cat, "AI教程")
    
    # 基础信息
    if "links" in ai:
        links = ai["links"]
        feat = ai["feat"]
        intro = ai["intro"]
        steps = ai["steps"]
        cb_code = ai["cb_code"]
    else:
        # 精简版AI（字典格式）
        links = [
            ("官网地址", '<a href="#" target="_blank">待补充</a>'),
            ("插件地址", "暂无"),
            ("接口文档", "暂无"),
            ("社群/社区", "暂无"),
            ("微信公众号", "关注AI技术社区"),
            ("微信小程序", "暂无")
        ]
        tag0 = ai.get("tags",[""])[0] if ai.get("tags") else ""
        feat = [tag0, "支持API调用", "可内嵌到exe/apk", "持续更新中"]
        intro = f'{ai["name"]}是{tag0}。{ai.get("brief","")}'
        steps = [
            ("注册账号", f'访问{ai["name"]}官网注册账号。'),
            ("获取Key", "在控制台创建应用，获取API Key。"),
            ("配置调用", "使用API Key配置调用参数。"),
            ("测试连接", "发送测试请求验证连接。"),
            ("内嵌部署", "将API调用集成到exe/apk中。")
        ]
        cb_code = f'''import requests

API_KEY = "你的API Key"
BASE_URL = "https://api.example.com/v1"

def on_ai_reply(text):
    """回调函数：AI回答后更新UI"""
    print("AI回答:", text)

def ask(prompt):
    r = requests.post(f"{{BASE_URL}}/chat/completions",
        headers={{"Authorization": f"Bearer {{API_KEY}}"}},
        json={{"model": "default", "messages": [{{"role": "user", "content": prompt}}]}})
    reply = r.json()["choices"][0]["message"]["content"]
    on_ai_reply(reply)
    return reply

ask("你好")'''
    
    tags_html = "".join(f'<span class="tag">{t}</span>' for t in ai["tags"])
    links_html = link_table(links)
    feat_html = "".join(f"<li>{f}</li>" for f in feat)
    steps_html = render_steps(steps)
    cb_html = code_block(f"{name}回调函数模板", "python", cb_code, f"cb_{slug}")
    
    content = f'''<div class="ai-head glass">
    <h1>{name}</h1>
    <div class="tags">{tags_html}</div>
    <p class="brief">{ai["brief"]}</p>
  </div>
  
<div class="fold glass" data-fold>
  <button class="fold-hd" type="button"><span>📌 官网 · 插件 · 接口文档 · 社群渠道（全部可点）</span><i class="caret"></i></button>
  <div class="fold-bd">{links_html}</div>
</div>

<div class="sec glass"><h2>🧠 它擅长什么 · 适用场景</h2><ul class="feat">{feat_html}</ul></div>

<div class="sec glass"><h2>📖 详细介绍</h2><div class="intro-txt">{intro}</div></div>

<div class="sec glass"><h2>🛠️ 详细部署 / 配置操作步骤</h2>{steps_html}</div>

<div class="sec glass callback">
  <h2>🔁 exe / apk 内嵌与后端回调接通教程</h2>
  <div class="cb-txt">内嵌到exe/apk的回调流程：客户端 → HTTP请求 → 收到JSON回复 → 解析内容 → 触发回调函数更新UI。注意API Key的安全存储，建议在服务端环境变量中管理。</div>
  {cb_html}
</div>
'''
    return page_head(name, ai["brief"], crumb) + content + page_tail()

def gen_mcp_page():
    """生成MCP独立单页"""
    links = link_table([
        ("官网地址", '<a href="https://modelcontextprotocol.io" target="_blank">https://modelcontextprotocol.io</a>'),
        ("规范文档", '<a href="https://modelcontextprotocol.io/specification" target="_blank">规范文档</a>'),
        ("开源仓库", '<a href="https://github.com/modelcontextprotocol" target="_blank">GitHub</a>'),
        ("Python SDK", '<a href="https://pypi.org/project/mcp" target="_blank">pip install mcp</a>'),
        ("Node.js SDK", '<a href="https://www.npmjs.com/package/@modelcontextprotocol/sdk" target="_blank">npm安装</a>'),
        ("社群/社区", '<a href="https://discord.gg/modelcontextprotocol" target="_blank">Discord</a>'),
        ("微信公众号", "关注AI技术社区"),
        ("微信小程序", "暂无")
    ])
    steps = render_steps([
        ("安装环境", "安装Node.js 18+和Python 3.10+，执行pip install mcp。"),
        ("创建MCP服务", "创建server.py，使用FastMCP框架定义工具函数。"),
        ("启动服务", "执行python server.py，默认通过stdio通信。"),
        ("配置客户端", "在支持MCP的客户端中添加服务，配置启动命令。"),
        ("测试连接", "在AI对话中请求调用工具，验证连接成功。"),
        ("扩展工具", "继续添加@mcp.tool()函数扩展AI能力。")
    ])
    cb = code_block("MCP服务完整模板", "python", '''from mcp.server.fastmcp import FastMCP
import os, json

mcp = FastMCP("local-tools")

@mcp.tool()
def read_file(path: str) -> str:
    """读取本地文件内容"""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

@mcp.tool()
def write_file(path: str, content: str) -> str:
    """写入文件"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return "已写入"

if __name__ == "__main__":
    mcp.run()''', "mcp1")
    
    content = f'''<div class="ai-head glass">
    <h1>MCP协议本地部署</h1>
    <div class="tags"><span class="tag">协议规范</span><span class="tag">本地部署</span><span class="tag">工具调用</span><span class="tag">开源</span><span class="tag">exe/apk内嵌</span></div>
    <p class="brief">MCP（Model Context Protocol）是大模型与外部工具连接的标准协议，本地部署让AI直接调用本地文件、数据库、API。</p>
  </div>
<div class="fold glass" data-fold><button class="fold-hd" type="button"><span>📌 官网 · 文档 · 社群渠道</span><i class="caret"></i></button><div class="fold-bd">{links}</div></div>
<div class="sec glass"><h2>🧠 它擅长什么</h2><ul class="feat"><li>统一大模型与外部工具的连接标准</li><li>支持本地文件读写、数据库查询、API调用</li><li>可被Claude Desktop、OpenClaw等客户端连接</li><li>支持stdio和HTTP/SSE两种传输方式</li><li>完全本地运行，数据不出本机</li></ul></div>
<div class="sec glass"><h2>📖 详细介绍</h2><div class="intro-txt">MCP是由Anthropic提出的开放协议，标准化大语言模型与外部工具、数据源之间的连接方式。采用客户端-服务器架构，通过JSON-RPC协议通信。</div></div>
<div class="sec glass"><h2>🛠️ 详细部署步骤</h2>{steps}</div>
<div class="sec glass callback"><h2>🔁 exe/apk内嵌回调教程</h2><div class="cb-txt">MCP服务内嵌到exe/apk：应用启动MCP子进程 → stdio通信 → AI调用工具 → 返回JSON结果 → 回调函数更新UI。</div>{cb}</div>
<div class="sec glass"><h2>🔗 与OpenClaw联动</h2><div class="intro-txt"><p>1. 注册OpenClaw：<a href="https://api.u-claw.org/register?aff=9OLG" target="_blank">https://api.u-claw.org/register?aff=9OLG</a></p><p>2. 在控制台添加MCP服务</p><p>3. AI即可调用本地工具函数</p></div></div>
'''
    return page_head("MCP协议本地部署", "MCP协议本地部署教程", "协议规范·本地部署型") + content + page_tail()

def gen_index():
    """生成首页"""
    # 按分类组织
    cats = {}
    for ai in AIS + [{"cat":a[0],"slug":a[1],"name":a[2],"ico":a[3],"tags":[a[4]],"brief":a[5]} for a in MORE_AIS]:
        cats.setdefault(ai["cat"], []).append(ai)
    
    cat_order = ["offline","chat","api","agent","rpa","production","code"]
    cat_icons = {"offline":"📦","chat":"💬","api":"🔑","agent":"🤖","rpa":"🎭","production":"🎨","code":"💻"}
    cat_colors = {"offline":"#4caf50","chat":"#2196f3","api":"#ff9800","agent":"#9c27b0","rpa":"#f44336","production":"#e91e63","code":"#00bcd4"}
    
    sections = ""
    nav = ""
    total = 0
    for cat in cat_order:
        if cat not in cats: continue
        ais = cats[cat]
        total += len(ais)
        cname = CAT_NAMES[cat]
        ico = cat_icons[cat]
        color = cat_colors[cat]
        nav += f'<a class="pill" href="#cat-{cat}" style="--pc:{color}">{ico} {cname.split("·")[0]}</a>'
        cards = ""
        for ai in ais:
            tags = "".join(f'<span class="tag">{t}</span>' for t in ai.get("tags",[]))
            cards += f'''<a class="card glass" href="pages/{ai["slug"]}.html" data-name="{ai["name"].lower()}" data-tags="{" ".join(ai.get("tags",[])).lower()}" data-brief="{ai.get("brief","").lower()}">
  <div class="card-ico">{ai.get("ico","🤖")}</div>
  <div class="card-body">
    <h3>{ai["name"]}</h3>
    <p>{ai.get("brief","")}</p>
    <div class="tags mini">{tags}</div>
  </div>
  <div class="card-go"><span class="arrow-anim">➜</span></div>
</a>'''
        # MCP和OpenClaw独立卡片
        if cat == "agent":
            cards += f'''<a class="card glass" href="pages/mcp.html" data-name="mcp协议" data-tags="mcp 协议 本地部署" data-brief="mcp model context protocol">
  <div class="card-ico">🔌</div>
  <div class="card-body">
    <h3>MCP协议本地部署教程</h3>
    <p>大模型与外部工具连接的标准协议，本地部署让AI调用本地文件/数据库/API，含exe/apk内嵌回调。</p>
    <div class="tags mini"><span class="tag">协议规范</span><span class="tag">本地部署</span><span class="tag">工具调用</span></div>
  </div>
  <div class="card-go"><span class="arrow-anim">➜</span></div>
</a>'''
        sections += f'''<section class="cat glass" id="cat-{cat}">
  <button class="cat-hd" type="button"><span class="cat-ico">{ico}</span><span class="cat-t"><b>{cname}</b><i>点击展开查看全部</i></span><span class="cat-count">{len(ais) + (1 if cat=="agent" else 0)}</span><i class="caret"></i></button>
  <div class="cat-bd"><div class="cards">{cards}</div></div>
</section>'''
    
    total += 1  # MCP
    
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI配置教程 · 全国AI智能体总目录（每AI一单页）</title>
<meta name="description" content="离线/联网中文AI大全：对话型、Key自定义模型、Agent智能体、RPA、生产类AI，每AI一个独立H5单页。">
<link rel="stylesheet" href="assets/css/main.css">
</head>
<body>
<div class="bg-layer" aria-hidden="true"><i class="blob b1"></i><i class="blob b2"></i><i class="blob b3"></i><i class="blob b4"></i></div>
<header class="hero">
  <h1>✨ AI配置教程 · 全国AI智能体总目录</h1>
  <p class="hero-sub">离线部署 · 联网对话 · Key自定义模型 · Agent自动化 · RPA · 生产类AI —— 每个AI一个独立H5单页，全部含部署步骤与exe/apk后端回调教程</p>
  <div class="search-wrap">
    <input id="searchBox" type="search" placeholder="🔍 超级搜索：输入AI名称/关键词/视频链接，自动识别解析，结果页面内展示" autocomplete="off">
    <button class="crystal-btn" id="searchGo" type="button">🔍 搜索</button>
  </div>
  <div id="searchResults"></div>
  <div id="biliResult"></div>
  <div class="stat"><b>{total}</b> 个AI单页 · 持续扩充中</div>
  <div class="pill-nav">{nav}</div>
</header>
<main class="index-main">
{sections}
</main>
<div class="foot">📚 AI配置教程 · 全国AI智能体大全 · 每AI一个独立单页 · 金色玻璃水晶质感</div>
{SVC_PANEL}
<script src="assets/js/main.js"></script>
</body>
</html>'''

# 生成所有页面
def main():
    # 生成72个AI单页
    all_ais = AIS + [{"cat":a[0],"slug":a[1],"name":a[2],"ico":a[3],"tags":[a[4]],"brief":a[5]} for a in MORE_AIS]
    for ai in all_ais:
        html = gen_ai_page(ai)
        path = os.path.join(BASE, "pages", f'{ai["slug"]}.html')
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
    print(f"✅ 生成 {len(all_ais)} 个AI单页")
    
    # 生成MCP单页
    with open(os.path.join(BASE, "pages", "mcp.html"), "w", encoding="utf-8") as f:
        f.write(gen_mcp_page())
    print("✅ 生成 MCP单页")
    
    # 生成首页
    with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
        f.write(gen_index())
    print("✅ 生成 首页")
    
    print(f"\n🎉 全部生成完成！共 {len(all_ais)+1+1} 个HTML文件")

if __name__ == "__main__":
    main()

