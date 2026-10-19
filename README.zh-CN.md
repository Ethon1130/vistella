<div align="center">

# 🌌 Vistella (星境)

**开源 AI 视觉创作中心 · 提示词工程权威指南 · 精选艺术配方与轻量工具**

[![Web 创作平台](https://img.shields.io/badge/Web_工作区-vistella.xyz-7c3aed?style=for-the-badge&logo=googlechrome&logoColor=white)](https://www.vistella.xyz/zh/playground?utm_source=github&utm_medium=repo_banner_zh)
[![提示词工程手册](https://img.shields.io/badge/权威指南-提示词工程手册-3b82f6?style=for-the-badge&logo=gitbook&logoColor=white)](guides/prompt_engineering_handbook.md)
[![交互式工具](https://img.shields.io/badge/本地工具-提示词工作室-10b981?style=for-the-badge&logo=html5&logoColor=white)](tools/prompt_builder/index.html)
[![开源协议: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![X (Twitter)](https://img.shields.io/badge/X-@aixtool-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/aixtool)

🌐 **多语言 / Languages:** [English](README.md) • **简体中文** • [繁體中文](README.zh-TW.md)

[**🌐 立即打开 Web 创作台**](https://www.vistella.xyz/zh/playground?utm_source=github&utm_medium=repo_cta_zh) • [**📚 提示词工程手册**](guides/prompt_engineering_handbook.md) • [**🎨 精选场景词库**](#-精选场景提示词宝库) • [**🛠️ 交互式工具**](#️-本地交互式提示词工作室) • [**🤝 社区贡献**](CONTRIBUTING.md)

</div>

---

## 💡 什么是 Vistella (星境)？

[Vistella (星境)](https://www.vistella.xyz/zh?utm_source=github&utm_medium=repo_intro_zh) 是专为创作者、设计师与视觉艺术家打造的现代化在线 AI 视觉创作平台。无需配置复杂的本地运行环境、无需显卡驱动与庞大的模型文件，打开浏览器即可直接创作超高质量视觉艺术作品。

本开源项目是 Vistella 的官方社区技术与资源中心，包含：
- 📚 **权威级提示词手册**：系统拆解布光法则（伦勃朗光、丁达尔光、侧逆光）、光学镜头（35mm/50mm/85mm）、胶片色调与构图美学。
- 🎨 **细分场景提示词宝库**：人像写真、商业静物、空间建筑、数字动漫插画的高分实战配方。
- 🛡️ **负向排除词典**：专治人像假面假手、画面杂质、产品划痕与透视畸变。
- 🛠️ **本地交互式工作台**：单文件 Web 版提示词工作室（免安装双击即用）与 Python 交互式生成器，支持一键直达 Vistella 工作区生成。

---

## 🗂️ 仓库目录与快速导航

```text
vistella/
├── guides/                             # 📚 深度视觉创作指南
│   ├── prompt_engineering_handbook.md   # 《提示词工程权威手册》：布光、镜头、色彩、构图
│   └── aspect_ratio_guide.md           # 《画幅比例与构图指南》：1:1、3:4、4:5、16:9、21:9
├── prompts/                            # 🎨 细分领域实战提示词宝库
│   ├── portraits_and_people.md         # 👤 人像写真：北欧高定、复古胶片、赛博行者、黑白电影
│   ├── commercial_and_products.md      # 🛍️ 商业静物：轻奢香水、3D 机械手表、植萃精华、概念跑鞋
│   ├── architecture_and_spaces.md      # 🏛️ 空间建筑：野兽派混凝土、枯山水庭院、北欧厨房
│   ├── digital_art_and_illustration.md # 🎨 数字插画：新海诚夏日天空、吉卜力田园、80s 霓虹赛博
│   ├── recipes.md                      # 🌟 精选通用高分配方
│   └── negative_prompts.md             # 🛡️ 负向排除词典
├── tools/                              # 🛠️ 本地交互式工具
│   └── prompt_builder/
│       ├── index.html                  # 💻 单文件 Web 提示词工作室（支持中/英/繁三语切换）
│       └── prompt_builder.py           # 🐍 零依赖 Python 命令行交互式生成器
└── CONTRIBUTING.md                     # 🤝 社区共建与提示词提交指南
```

---

## 🚀 在线即开即用体验

无需任何本地环境配置，零门槛开始视觉创作：

| 平台特色 | 详细说明 |
| :--- | :--- |
| **即开即用** | 支持任何桌面或移动端浏览器访问 [vistella.xyz](https://www.vistella.xyz/zh/playground?utm_source=github&utm_medium=feature_table_zh)。 |
| **每日免费额度** | 注册即享日常创作额度，随心探索与测试不同提示词风格。 |
| **全画幅比例支持** | 自由切换 `1:1`、`16:9`、`9:16`、`3:4`、`4:3`、`21:9` 等构图尺寸。 |
| **精选审美预设** | 预置摄影级构图、布光与材质参数，降低“盲目抽卡”成本。 |

👉 [**立即进入 Vistella 创作台开启创作 →**](https://www.vistella.xyz/zh/playground?utm_source=github&utm_medium=start_now_cta_zh)

---

## 🎨 精选场景提示词宝库

每条配方均标注推荐画幅、布光说明与材质细节，附带一键运行直达链接：

| 场景分类 | 内容涵盖 | 快速浏览 |
| :--- | :--- | :--- |
| **👤 人像写真与角色** | 北欧高定时尚、70 年代复古胶片、雨夜赛博黑客、黑白电影侦探、美妆微距 | [浏览人像词库 →](prompts/portraits_and_people.md) |
| **🛍️ 商业静物与产品** | 轻奢长笛香水、悬浮拆解机械表、有机植物精华、概念透光跑鞋、手冲咖啡 | [浏览静物词库 →](prompts/commercial_and_products.md) |
| **🏛️ 空间建筑与室内** | 悬崖野兽派混凝土别墅、雨季日式庭院、极简斯堪的纳维亚厨房、荒漠夯土庇护所 | [浏览建筑词库 →](prompts/architecture_and_spaces.md) |
| **🎨 数字艺术与动漫** | 新海诚夏日积雨云、吉卜力溪边水车、80 年代复古合成波公路、黏土微缩世界 | [浏览插画词库 →](prompts/digital_art_and_illustration.md) |
| **🛡️ 负向排除词典** | 针对人像肢体、皮肤塑料感、产品指纹反光、建筑透视变形的专用屏蔽词 | [查看负向词库 →](prompts/negative_prompts.md) |

---

## 🛠️ 本地交互式提示词工作室

仓库自带两款免配置的轻量小工具：

### 1. Web 提示词工作室 (`tools/prompt_builder/index.html`)
无需启动服务器，直接在本地浏览器双击即可运行。
- **多语言界面**：支持**英文、简体中文、繁體中文**一键无缝切换。
- **可视化选词**：点击布光、镜头、色彩、画幅标签实时生成结构化提示词。
- **一键直通**：配备“📋 复制提示词”与“🚀 在 Vistella 中打开生成”功能。

### 2. Python 终端生成器 (`tools/prompt_builder/prompt_builder.py`)
适合极客在终端使用，无任何第三方包依赖：

```bash
python tools/prompt_builder/prompt_builder.py
```

根据终端指引逐步选择主体、环境、光影、镜头及画幅，即时拼装专业级描述并生成直通链接。

---

## 📐 通用高分提示词结构法则

告别盲目拼凑无意义标签，遵循专业视觉生成“五步法则”：

$$\text{最终画面} = \text{核心主体} + \text{环境空间} + \text{光影氛围} + \text{光学镜头} + \text{色彩与质感}$$

1. **核心主体**：精准定义人物、物品或建筑的具体特征（年龄、服装、姿态、材质）。
2. **环境空间**：交代主体所处的位置、背景元素、天气或时间。
3. **光影氛围**：明确光源方向与光质（如：“柔和早晨侧光”、“穿透薄雾的丁达尔金光”）。
4. **光学镜头**：控制景深与透视视角（如：“85mm f/1.4 肖像镜头”、“虚化背景奶油感”）。
5. **色彩质感**：指定色彩倾向与表面细节（如：“柯达 Portra 400 暖调”、“微小毛孔与天然细腻肌理”）。

*(更多干货详见 [《提示词工程权威手册》](guides/prompt_engineering_handbook.md))*

---

## 🤝 社区共建

我们热烈欢迎所有创作者贡献灵感！
- 提交在 Vistella 实测高分的新提示词配方
- 补充特定艺术风格的负向排除词
- 完善使用手册与技术翻译

详情请查阅 [贡献指南 (CONTRIBUTING.md)](CONTRIBUTING.md)。

---

## 📄 开源协议

本项目基于 [MIT 协议](LICENSE) 开源。

---

<div align="center">
  <sub>由 <a href="https://github.com/Ethon1130">Ethon1130</a> 与 <a href="https://www.vistella.xyz/zh?utm_source=github&utm_medium=footer_zh">Vistella 星境社区</a> 用心打造。</sub>
</div>
