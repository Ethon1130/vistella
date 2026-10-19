<div align="center">

# 🌌 Vistella (星境)

**The Open-Source Prompt Engineering Hub, Aesthetic Recipes & Creative Studio for AI Visual Art.**

[![Website](https://img.shields.io/badge/Web_App-vistella.xyz-7c3aed?style=for-the-badge&logo=googlechrome&logoColor=white)](https://www.vistella.xyz/en/playground?utm_source=github&utm_medium=repo_banner&utm_campaign=vistella_oss)
[![Prompt Handbook](https://img.shields.io/badge/Handbook-Prompt_Engineering-3b82f6?style=for-the-badge&logo=gitbook&logoColor=white)](guides/prompt_engineering_handbook.md)
[![Interactive Tool](https://img.shields.io/badge/Tools-Prompt_Studio-10b981?style=for-the-badge&logo=html5&logoColor=white)](tools/prompt_builder/index.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![X (Twitter)](https://img.shields.io/badge/X-@aixtool-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/aixtool)

🌐 **Languages / 語言:** **English** • [简体中文](README.zh-CN.md) • [繁體中文](README.zh-TW.md)

[**🌐 Launch Web Playground**](https://www.vistella.xyz/en/playground?utm_source=github&utm_medium=repo_cta) • [**🖼️ Visual Gallery**](prompts/README.md) • [**📚 Engineering Handbook**](guides/prompt_engineering_handbook.md) • [**🎨 Prompt Collections**](#-curated-prompt-collections) • [**🛠️ Interactive Tools**](#️-interactive-prompt-studio) • [**中文说明**](README.zh-CN.md)

</div>

![Moss-covered floating citadel with waterfalls above sunset clouds, a reference image for a fantasy prompt recipe](prompts/assets/floating-citadel-concept.webp)

*Browse the [visual prompt gallery](prompts/README.md). This reference artwork was made with imagegen for the repository; it is not a Vistella Playground result.*

---

## 💡 What is Vistella?

[Vistella (星境)](https://www.vistella.xyz?utm_source=github&utm_medium=repo_intro) is a modern, intuitive AI visual creation platform designed for creators, designers, and visual artists. Instead of wrestling with complex local software installations, GPU requirements, or terminal environments, Vistella empowers you to generate and edit high-quality visual art directly in your web browser with zero setup.

This open-source repository serves as the official community resource center:
- 📚 **Comprehensive Handbook**: Deep dive into lighting masterclasses, camera lenses, color science, and composition rules.
- 🎨 **Domain-Specific Prompt Libraries**: Production-grade prompt formulas for portraits, commercial products, architecture, and digital art.
- 🛡️ **Negative Prompt Dictionary**: Curated guardrails to eliminate plastic skin, anatomical errors, and geometric distortions.
- 🛠️ **Local Prompt Studio Tools**: Zero-dependency Python CLI tool and standalone offline HTML prompt builder with direct one-click launch to Vistella.
- ✨ **Visual Prompt Gallery**: Reference artwork paired with [copyable recipes](prompts/README.md) and a [sharing kit](prompts/distribution-kit.md).

---

## 🗂️ Repository Directory & Quick Navigation

```text
vistella/
├── guides/                             # 📚 In-depth Visual Guides
│   ├── prompt_engineering_handbook.md   # Lighting, optics, color science, and framing
│   └── aspect_ratio_guide.md           # Optimal ratios (1:1, 3:4, 16:9, 21:9) & layout
├── prompts/                            # 🎨 Battle-Tested Prompt Collections
│   ├── README.md                        # Visual gallery and copyable recipe links
│   ├── assets/                          # Reference artwork and social sharing files
│   ├── portraits_and_people.md         # Fashion editorials, cyberpunk wanderers, cinema noir
│   ├── commercial_and_products.md      # Perfumes, smartwatches, sneakers, cosmetics
│   ├── architecture_and_spaces.md      # Brutalist concrete, zen pavilions, desert retreats
│   ├── digital_art_and_illustration.md # Shinkai skies, Ghibli meadows, 80s synthwave
│   ├── recipes.md                      # Curated cross-category highlights
│   └── negative_prompts.md             # Curated artifact elimination tokens
├── tools/                              # 🛠️ Interactive Tools
│   └── prompt_builder/
│       ├── index.html                  # Standalone Web Prompt Studio (Open in browser)
│       └── prompt_builder.py           # Zero-dependency interactive Python CLI generator
└── CONTRIBUTING.md                     # 🤝 How to submit prompt recipes and improvements
```

---

## 🚀 Experience Vistella Online

No local setup, no heavy installations, and no powerful GPU required:

| Feature | Details |
| :--- | :--- |
| **Instant Access** | Open [vistella.xyz](https://www.vistella.xyz/en/playground?utm_source=github&utm_medium=feature_table) in any desktop or mobile browser. |
| **Daily Free Credits** | Create visual studies and explore styles with complimentary credits. |
| **Flexible Ratios** | Seamlessly toggle between `1:1`, `16:9`, `9:16`, `3:4`, `4:3`, and `21:9`. |
| **Curated Presets** | Fast-track your creativity with built-in aesthetics and parameters. |

👉 [**Start Creating on Vistella Playground Now →**](https://www.vistella.xyz/en/playground?utm_source=github&utm_medium=start_now_cta)

---

## 🎨 Curated Prompt Collections

Explore our categorized recipes with lighting, ratio, and aesthetic breakdowns:

| Category | Description | Recommended Link |
| :--- | :--- | :--- |
| **👤 Portraits & People** | Editorial fashion, vintage 1970s warmth, cyberpunk wanderers, studio beauty close-ups | [Browse Portraits →](prompts/portraits_and_people.md) |
| **🛍️ Commercial & Products** | Luxury frosted perfumes, exploded 3D smartwatches, skincare serums, sneakers | [Browse Products →](prompts/commercial_and_products.md) |
| **🏛️ Architecture & Spaces** | Brutalist concrete residences, Japanese zen pavilions, Scandinavian kitchens | [Browse Architecture →](prompts/architecture_and_spaces.md) |
| **🎨 Digital Art & Anime** | Makoto Shinkai skies, Studio Ghibli countryside, retro 80s synthwave, 3D dioramas | [Browse Digital Art →](prompts/digital_art_and_illustration.md) |
| **🛡️ Negative Prompts** | Specialized exclusions for hands, skin texture, product clarity, and architectural lines | [View Negative Prompts →](prompts/negative_prompts.md) |
| **🖼️ Visual Gallery** | Four reference scenes, exact imagegen prompts, and reusable social artwork | [Browse Gallery →](prompts/README.md) |

---

## 🛠️ Interactive Prompt Studio

We provide two lightweight tools to help you craft structured prompts in seconds:

### 1. Web Prompt Studio (`tools/prompt_builder/index.html`)
A standalone single-file visual tool that runs completely offline in any web browser.
- Interactive chips for Lighting, Optics, Film Stocks, and Aspect Ratios.
- Live real-time prompt compilation.
- One-click button: **"🚀 Launch in Vistella Playground"**.

### 2. CLI Prompt Builder (`tools/prompt_builder/prompt_builder.py`)
Run directly from your terminal with zero external dependencies:

```bash
python tools/prompt_builder/prompt_builder.py
```

Follow the interactive prompts to generate production-ready descriptions and get a direct web link to test them.

---

## 📐 The Universal Prompt Formula

To get the most consistent visual quality from modern image generation, structure your text prompts using this 5-part formula:

$$\text{Final Artwork} = \text{Subject} + \text{Environment} + \text{Lighting \& Atmosphere} + \text{Camera Optics} + \text{Color \& Material Details}$$

### Formula Breakdown:
1. **Core Subject**: Define the main character, object, or architecture with specific descriptors (age, clothing, pose, materials).
2. **Environment & Context**: Describe the surrounding space, background elements, weather, or time of day.
3. **Lighting & Mood**: Specify light direction and quality (e.g., *"soft diffused morning sidelight"*, *"volumetric golden hour glow"*).
4. **Camera & Optics**: Guide depth and perspective (e.g., *"shot on 85mm f/1.4 lens, shallow depth of field"*).
5. **Color & Texture**: State the color grade and surface finishes (e.g., *"warm earth tones, tactile brushed aluminum texture"*).

*(Read the complete breakdown in the [Prompt Engineering Handbook](guides/prompt_engineering_handbook.md))*

---

## 🇨🇳 中文介绍

**Vistella (星境)** 是专为创作者与设计师打造的在线 AI 视觉创作平台。无需配置本地复杂的显卡环境与运行库，打开网页即可开始创作。

- 🌐 **在线即用**：直接访问 [Vistella 官方工作区 (vistella.xyz)](https://www.vistella.xyz/zh/playground?utm_source=github&utm_medium=zh_intro) 即可开始创作，每日提供免费额度。
- 📦 **开源资源**：
  - 📚 **提示词工程权威指南**：系统化讲解布光方案（伦勃朗光、丁达尔光、侧光）、光学镜头（35mm/50mm/85mm）、胶片色调与构图法则：详见 [`guides/prompt_engineering_handbook.md`](guides/prompt_engineering_handbook.md)。
  - 📐 **画幅比例指南**：详见 [`guides/aspect_ratio_guide.md`](guides/aspect_ratio_guide.md)。
  - 🎨 **四大细分场景词库**：人像写真、商业静物、建筑空间、数字动漫插画，开箱即用。
  - 🛡️ **负向排除词典**：详见 [`prompts/negative_prompts.md`](prompts/negative_prompts.md)。
  - 🛠️ **本地交互式提示词生成器**：单文件 Web 版（[`tools/prompt_builder/index.html`](tools/prompt_builder/index.html)）与 Python 终端交互版。
  - 🖼️ **配图提示词画廊**：[查看参考图、配方和发布素材](prompts/README.zh-CN.md)。参考图由 imagegen 为本仓库制作，不代表 Vistella 站内实测输出。

---

## 🤝 Contributing

We welcome community contributions!
- Submit new prompt recipes tested on Vistella
- Share negative prompt refinements for specific art styles
- Enhance documentation or report feedback

Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for details on how to open a Pull Request.

---

## 📄 License

This project is open-sourced under the [MIT License](LICENSE).

---

<div align="center">
  <sub>Built with ❤️ by <a href="https://github.com/Ethon1130">Ethon1130</a> & the <a href="https://www.vistella.xyz/en/playground?utm_source=github&utm_medium=footer">Vistella Community</a>.</sub>
</div>
