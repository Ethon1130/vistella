<div align="center">

# 🌌 Vistella (星境)

**The Open-Source Toolkit, Prompt Recipes & Agent Skills for Next-Gen AI Visual Creation.**

[![Website](https://img.shields.io/badge/Web_App-vistella.xyz-7c3aed?style=for-the-badge&logo=googlechrome&logoColor=white)](https://www.vistella.xyz?utm_source=github&utm_medium=repo_banner&utm_campaign=vistella_oss)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![X (Twitter)](https://img.shields.io/badge/X-@aixtool-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/aixtool)
[![Capabilities](https://img.shields.io/badge/Capabilities-Text_to_Image_|_Editing_|_Styles-success?style=for-the-badge)](https://www.vistella.xyz/playground?utm_source=github&utm_medium=repo_badge)

[**🌐 Launch Web Playground**](https://www.vistella.xyz/playground?utm_source=github&utm_medium=repo_cta) • [**📖 Prompt Recipes**](#-curated-prompt-recipes) • [**🎨 Creative Capabilities**](#-creative-capabilities--visual-styles) • [**🤖 Agent Skills**](#-ai-agent-skills-integration) • [**⚡ API & SDK**](#-quick-start-api--sdk) • [**中文说明**](#-中文介绍)

</div>

---

## 💡 What is Vistella?

[Vistella (星境)](https://www.vistella.xyz?utm_source=github&utm_medium=repo_intro) is a modern AI visual workspace and unified cloud API designed for creators, designers, and developers. Instead of wrestling with complex local setups, GPU drivers, and massive checkpoint files, Vistella empowers you to create high-quality artwork directly in your browser or through a developer-friendly API.

This open-source repository provides:
- 🎨 **Curated Prompt Recipes**: Production-grade prompt engineering formulas tested for consistent aesthetic output.
- 🤖 **AI Agent Skills**: Drop-in skills for Claude Code, Cursor, OpenClaw, and autonomous agent frameworks.
- ⚡ **Lightweight SDKs & Examples**: Clean Python, Node.js, and cURL snippets for programmatic image synthesis.
- 📐 **Composition & Parameter Presets**: Pre-tuned aspect ratios, lighting parameters, and prompt structures.

---

## 🚀 Fast Track: Online Creation vs. Open Source

| Mode | Who it's for | Setup Time | GPU Required? | Link |
| :--- | :--- | :--- | :--- | :--- |
| **Online Playground** | Creators, Designers, Marketers | **0 seconds** | ❌ No | [👉 Launch Vistella Web App](https://www.vistella.xyz/playground?utm_source=github&utm_medium=table) |
| **Agent Skill / CLI** | AI Engineers & Agent Builders | ~1 minute | ❌ Cloud-powered | [Jump to Agent Skills](#-ai-agent-skills-integration) |
| **REST / Python API** | Developers integrating into apps | ~2 minutes | ❌ Cloud-powered | [Jump to API Examples](#-quick-start-api--sdk) |

---

## 🎨 Creative Capabilities & Visual Styles

Vistella covers diverse creative scenarios with purpose-built aesthetic tuning:

| Style & Domain | Best For | Typical Characteristics | Output Formats |
| :--- | :--- | :--- | :--- |
| **Photorealistic Studio** | Editorial portraits, fashion, candid street photography | Authentic skin texture, natural aperture bokeh, realistic optics | `3:4`, `4:5`, `16:9` |
| **Commercial & Product** | E-commerce visuals, packaging, industrial design | Clean studio lighting, physical material reflections, negative space | `1:1`, `4:3` |
| **Architecture & Spaces** | Exterior pavilions, interior design, spatial concepts | Volumetric sunlight, material authenticity, precise perspective | `16:9`, `21:9` |
| **Digital Art & Anime** | Concept art, fantasy worldbuilding, character illustration | Vibrant color harmony, cinematic atmosphere, artistic flair | `16:9`, `21:9` |
| **Brand & Graphic Assets** | Logos, app icons, vector illustrations, typography | Sharp edges, minimalist compositions, solid background contrast | `1:1`, `16:9` |

---

## 📖 Curated Prompt Recipes

Here are production-ready prompt formulas designed to produce consistent, stunning results. You can test them directly in the [Vistella Playground](https://www.vistella.xyz/playground?utm_source=github&utm_medium=recipe_section).

### 1. Cinematic Hyper-Realistic Portrait
> **Style:** Photorealistic Studio Photography  
> **Recommended Aspect Ratio:** `3:4` or `4:5`

```text
Cinematic 35mm photograph of an East Asian female architect in an ultra-modern concrete studio, 
soft natural morning sidelight, depth of field, dust motes in sunbeam, shot on Hasselblad H6D-100c, 
subtle film grain, hyper-detailed skin texture, neutral color grading, editorial masterpiece.
```
👉 [Run this prompt on Vistella →](https://www.vistella.xyz/playground?utm_source=github&utm_medium=prompt_recipe1)

---

### 2. Conceptual Minimalist 3D Product
> **Style:** Commercial Product Visualization  
> **Recommended Aspect Ratio:** `1:1`

```text
A luxury matte ceramic perfume bottle standing on smooth damp limestone, 
single ray of volumetric light from above, delicate water droplets, 
frosted glass accents, architectural minimalism, award-winning commercial photography, 8k render.
```
👉 [Run this prompt on Vistella →](https://www.vistella.xyz/playground?utm_source=github&utm_medium=prompt_recipe2)

---

### 3. Cyberpunk Streetscape
> **Style:** Digital Art & Worldbuilding  
> **Recommended Aspect Ratio:** `21:9`

```text
Rain-slicked alleyway in Neo-Tokyo at midnight, holographic kanji neon signage reflecting on wet asphalt, 
lone figure with glowing cybernetic visor under a transparent umbrella, moody volumetric fog, 
teal and magenta color contrast, Unreal Engine 5 aesthetic, photorealistic octane render.
```
👉 [Run this prompt on Vistella →](https://www.vistella.xyz/playground?utm_source=github&utm_medium=prompt_recipe3)

*(More recipes available in [`prompts/recipes.md`](prompts/recipes.md))*

---

## 🤖 AI Agent Skills Integration

Use Vistella directly inside autonomous AI agent workflows (Claude Code, OpenClaw, Cursor, AutoGen).

### Specification
The skill specification is located at [`skills/SKILL.md`](skills/SKILL.md).

### Quick Install (OpenClaw / Claude Skills)
```bash
# Add the Vistella image generation skill
openclaw skills add https://github.com/Ethon1130/vistella
```

Once installed, your agent can trigger visual creation naturally:
> *"Generate a minimalist hero illustration for our new landing page using Vistella."*

---

## ⚡ Quick Start: API & SDK

### Python Example
Submit an asynchronous task and poll for completion:

```python
import os
import time
import requests

API_KEY = os.getenv("VISTELLA_API_KEY", "your_api_key_here")
BASE_URL = "https://www.vistella.xyz/api/v1"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# 1. Create task
task_payload = {
    "prompt": "An ethereal glowing jellyfish floating above a serene mirror-like mountain lake at twilight, 8k",
    "aspect_ratio": "16:9"
}

res = requests.post(f"{BASE_URL}/tasks", json=task_payload, headers=headers)
task_id = res.json()["data"]["task_id"]
print(f"Task submitted! ID: {task_id}")

# 2. Wait for result
while True:
    status_res = requests.get(f"{BASE_URL}/tasks/{task_id}", headers=headers).json()
    status = status_res["data"]["status"]
    if status == "succeeded":
        image_url = status_res["data"]["output"]["url"]
        print(f"Image created successfully: {image_url}")
        break
    elif status == "failed":
        print("Task failed:", status_res["data"].get("error"))
        break
    time.sleep(2)
```

*(Full examples with error handling and Webhook callbacks in [`examples/`](examples/))*

---

## 🇨🇳 中文介绍

**Vistella (星境)** 是专为创作者与开发者打造的高质量 AI 视觉创作平台与统一接口服务。无需配置本地显卡环境，通过网页端工作区与标准化 API 即可一键生成高品质视觉作品。

- 🌐 **在线即用**：直接访问 [Vistella 官方工作区 (vistella.xyz)](https://www.vistella.xyz?utm_source=github&utm_medium=zh_intro) 即可开始创作，每日提供免费额度。
- 📦 **开源资源**：
  - 精选高分提示词配方（包含景深、布光、材质增强技巧）：详见 [`prompts/recipes.md`](prompts/recipes.md)。
  - 智能体 Agent Skill 规范：为 Claude、Cursor 等 AI 助手赋能生图能力：详见 [`skills/SKILL.md`](skills/SKILL.md)。
  - 开发者快速集成代码：详见 [`examples/`](examples/) 目录。

---

## 🤝 Contributing

We welcome contributions of all kinds!
- Submit new prompt recipes tested on Vistella
- Add agent adapters and framework integrations
- Enhance documentation or report feedback

Please feel free to open a [Pull Request](https://github.com/Ethon1130/vistella/pulls) or start a discussion in [Issues](https://github.com/Ethon1130/vistella/issues).

---

## 📄 License

This project is open-sourced under the [MIT License](LICENSE).

---

<div align="center">
  <sub>Built with ❤️ by <a href="https://github.com/Ethon1130">Ethon1130</a> & the <a href="https://www.vistella.xyz?utm_source=github&utm_medium=footer">Vistella Community</a>.</sub>
</div>
