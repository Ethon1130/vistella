<div align="center">

# 🌌 Vistella (星境)

**開源 AI 視覺創作中心 · 提示詞工程權威指南 · 精選藝術配方與輕量工具**

[![Web 創作平台](https://img.shields.io/badge/Web_工作區-vistella.xyz-7c3aed?style=for-the-badge&logo=googlechrome&logoColor=white)](https://www.vistella.xyz/zh/playground?utm_source=github&utm_medium=repo_banner_zh_tw)
[![提示詞工程手冊](https://img.shields.io/badge/權威指南-提示詞工程手冊-3b82f6?style=for-the-badge&logo=gitbook&logoColor=white)](guides/prompt_engineering_handbook.md)
[![互動式工具](https://img.shields.io/badge/本地工具-提示詞工作室-10b981?style=for-the-badge&logo=html5&logoColor=white)](tools/prompt_builder/index.html)
[![開源授權: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![X (Twitter)](https://img.shields.io/badge/X-@aixtool-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/aixtool)

🌐 **多語言 / Languages:** [English](README.md) • [简体中文](README.zh-CN.md) • **繁體中文**

[**🌐 立即打開 Web 創作台**](https://www.vistella.xyz/zh/playground?utm_source=github&utm_medium=repo_cta_zh_tw) • [**📚 提示詞工程手冊**](guides/prompt_engineering_handbook.md) • [**🎨 精選場景詞庫**](#-精選場景提示詞寶庫) • [**🛠️ 互動式工具**](#️-本地互動式提示詞工作室) • [**🤝 社群貢獻**](CONTRIBUTING.md)

</div>

---

## 💡 什麼是 Vistella (星境)？

[Vistella (星境)](https://www.vistella.xyz/zh?utm_source=github&utm_medium=repo_intro_zh_tw) 是專為創作者、設計師與視覺藝術家打造的現代化線上 AI 視覺創作平台。無需配置複雜的本地運行環境、無需高規格顯示卡驅動與龐大的模型檔案，打開瀏覽器即可直接創作頂級品質的視覺藝術作品。

本開源專案是 Vistella 的官方社群技術與資源中心，包含：
- 📚 **權威級提示詞手冊**：系統拆解佈光法則（林布蘭光、廷得耳光、側逆光）、光學鏡頭（35mm/50mm/85mm）、底片色調與構圖美學。
- 🎨 **細分場景提示詞寶庫**：人像寫真、商業靜物、空間建築、數位動漫插畫的高分實戰配方。
- 🛡️ **負向排除詞典**：專門解決人像假面假手、畫面雜質、產品刮痕與透視畸變。
- 🛠️ **本地互動式工作台**：單檔案 Web 版提示詞工作室（免安裝雙擊即用，支援中/英/繁切換）與 Python 互動式生成器，支援一鍵直達 Vistella 工作區生成。

---

## 🗂️ 倉庫目錄與快速導覽

```text
vistella/
├── guides/                             # 📚 深度視覺創作指南
│   ├── prompt_engineering_handbook.md   # 《提示詞工程權威手冊》：佈光、鏡頭、色彩、構圖
│   └── aspect_ratio_guide.md           # 《畫幅比例與構圖指南》：1:1、3:4、4:5、16:9、21:9
├── prompts/                            # 🎨 細分領域實戰提示詞寶庫
│   ├── portraits_and_people.md         # 👤 人像寫真：北歐高訂、復古底片、賽博行者、黑白電影
│   ├── commercial_and_products.md      # 🛍️ 商業靜物：輕奢香水、3D 機械手錶、植萃精華、概念跑鞋
│   ├── architecture_and_spaces.md      # 🏛️ 空間建築：野獸派清水模、枯山水庭院、北歐廚房
│   ├── digital_art_and_illustration.md # 🎨 數位插畫：新海誠夏日積雨雲、吉卜力田園、80s 霓虹合成波
│   ├── recipes.md                      # 🌟 精選通用高分配方
│   └── negative_prompts.md             # 🛡️ 負向排除詞典
├── tools/                              # 🛠️ 本地互動式工具
│   └── prompt_builder/
│       ├── index.html                  # 💻 單檔案 Web 提示詞工作室（支援中/英/繁三語切換）
│       └── prompt_builder.py           # 🐍 零依賴 Python 命令列互動式生成器
└── CONTRIBUTING.md                     # 🤝 社群共建與提示詞提交指南
```

---

## 🚀 線上即開即用體驗

無需任何本地環境配置，零門檻開始視覺創作：

| 平台特色 | 詳細說明 |
| :--- | :--- |
| **即開即用** | 支援任何桌機或行動裝置瀏覽器造訪 [vistella.xyz](https://www.vistella.xyz/zh/playground?utm_source=github&utm_medium=feature_table_zh_tw)。 |
| **每日免費額度** | 註冊即享日常創作額度，隨心探索與測試不同提示詞風格。 |
| **全畫幅比例支援** | 自由切換 `1:1`、`16:9`、`9:16`、`3:4`、`4:3`、`21:9` 等構圖尺寸。 |
| **精選審美預設** | 內建攝影級構圖、佈光與材質參數，大幅降低試錯成本。 |

👉 [**立即進入 Vistella 創作台開啟創作 →**](https://www.vistella.xyz/zh/playground?utm_source=github&utm_medium=start_now_cta_zh_tw)

---

## 🎨 精選場景提示詞寶庫

每條配方均標註推薦畫幅、佈光說明與材質細節，附帶一鍵運行直達連結：

| 場景分類 | 內容涵蓋 | 快速瀏覽 |
| :--- | :--- | :--- |
| **👤 人像寫真與角色** | 北歐高訂時尚、70 年代復古底片、雨夜賽博駭客、黑白電影偵探、美妝微距 | [瀏覽人像詞庫 →](prompts/portraits_and_people.md) |
| **🛍️ 商業靜物與產品** | 輕奢長笛香水、懸浮拆解機械錶、有機植物精華、概念透光跑鞋、手沖咖啡 | [瀏覽靜物詞庫 →](prompts/commercial_and_products.md) |
| **🏛️ 空間建築與室內** | 懸崖野獸派清水模別墅、雨季日式庭院、極簡斯堪地那維亞廚房、荒漠夯土避難所 | [瀏覽建築詞庫 →](prompts/architecture_and_spaces.md) |
| **🎨 數位藝術與動漫** | 新海誠夏日積雨雲、吉卜力溪邊水車、80 年代復古合成波公路、黏土微縮世界 | [瀏覽插畫詞庫 →](prompts/digital_art_and_illustration.md) |
| **🛡️ 負向排除詞典** | 針對人像肢體、皮膚塑料感、產品指紋反光、建築透視變形的專用屏蔽詞 | [查看負向詞庫 →](prompts/negative_prompts.md) |

---

## 🛠️ 本地互動式提示詞工作室

倉庫自帶兩款免配置的輕量小工具：

### 1. Web 提示詞工作室 (`tools/prompt_builder/index.html`)
無需啟動伺服器，直接在本地瀏覽器雙擊即可運行。
- **多語言介面**：支援**英文、簡體中文、繁體中文**一鍵切換。
- **視覺化選詞**：點擊佈光、鏡頭、色彩、畫幅標籤即時生成結構化提示詞。
- **一鍵直通**：配備「📋 複製提示詞」與「🚀 在 Vistella 中打開生成」功能。

### 2. Python 終端生成器 (`tools/prompt_builder/prompt_builder.py`)
適合在命令列使用，無任何第三方套件依賴：

```bash
python tools/prompt_builder/prompt_builder.py
```

根據終端指引逐步選擇主體、環境、光影、鏡頭及畫幅，即時拼裝專業級描述並生成直通連結。

---

## 📐 通用高分提示詞結構法則

告別盲目堆砌無意義標籤，遵循專業視覺生成「五步法則」：

$$\text{最終畫面} = \text{核心主體} + \text{環境空間} + \text{光影氛圍} + \text{光學鏡頭} + \text{色彩與質感}$$

1. **核心主體**：精準定義人物、物品或建築的具體特徵（年齡、服裝、姿態、材質）。
2. **環境空間**：交代主體所處的位置、背景元素、天氣或時間。
3. **光影氛圍**：明確光源方向與光質（如：「柔和早晨側光」、「穿透薄霧的廷得耳金光」）。
4. **光學鏡頭**：控制景深與透視視角（如：「85mm f/1.4 肖像鏡頭」、「虛化背景奶油感」）。
5. **色彩質感**：指定色彩傾向與表面細節（如：「柯達 Portra 400 暖調」、「微小毛孔與天然細膩肌理」）。

*(更多內容詳見 [《提示詞工程權威手冊》](guides/prompt_engineering_handbook.md))*

---

## 🤝 社群共建

我們熱烈歡迎所有創作者貢獻靈感！
- 提交在 Vistella 實測高分的新提示詞配方
- 補充特定藝術風格的負向排除詞
- 完善使用手冊與技術翻譯

詳情請參閱 [貢獻指南 (CONTRIBUTING.md)](CONTRIBUTING.md)。

---

## 📄 開源授權

本專案基於 [MIT 授權條款](LICENSE) 開源。

---

<div align="center">
  <sub>由 <a href="https://github.com/Ethon1130">Ethon1130</a> 與 <a href="https://www.vistella.xyz/zh?utm_source=github&utm_medium=footer_zh_tw">Vistella 星境社群</a> 用心打造。</sub>
</div>
