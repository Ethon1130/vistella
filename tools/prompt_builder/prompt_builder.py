#!/usr/bin/env python3
"""
Vistella Visual Prompt Builder (CLI)
===================================
A lightweight, zero-dependency interactive tool to compose production-grade
prompts for AI visual creation on Vistella (https://www.vistella.xyz/en/playground).
Supports English, 简体中文, and 繁體中文.
"""

import sys
import urllib.parse

TEXTS = {
    "1": {
        "title": "🌌 Vistella Visual Prompt Builder (CLI)",
        "subtitle": "Craft production-ready prompts for https://www.vistella.xyz",
        "step1": "1. Enter your core subject / idea (in English or Chinese):\n> ",
        "default_subject": "An architectural pavilion in a serene bamboo grove",
        "step2": "2. Enter environment / background (press Enter to skip):\n> ",
        "step3": "3. Select Lighting",
        "step4": "4. Select Camera Optics",
        "step5": "5. Select Color & Film Grade",
        "step6": "6. Select Aspect Ratio",
        "select": "Select option (1-{n}) [default: 1]: ",
        "compiled": "✨ COMPILED PROMPT:",
        "negative": "🛡️ RECOMMENDED NEGATIVE PROMPT:",
        "ratio_rec": "📐 RECOMMENDED RATIO: {ratio} ({label})",
        "launch": "👉 OPEN DIRECTLY IN VISTELLA PLAYGROUND:",
        "prefix": "https://www.vistella.xyz/en/playground",
    },
    "2": {
        "title": "🌌 Vistella 提示词命令行拼装工具 (CLI)",
        "subtitle": "为 https://www.vistella.xyz 快速构建高质感提示词",
        "step1": "1. 请输入核心主体 / 画面创意 (支持中英文):\n> ",
        "default_subject": "A female fashion model in an oversized charcoal coat",
        "step2": "2. 请输入环境空间 / 背景元素 (按回车可跳过):\n> ",
        "step3": "3. 选择光影布光",
        "step4": "4. 选择镜头光学",
        "step5": "5. 选择色彩调色与胶片",
        "step6": "6. 选择画幅比例",
        "select": "请输入选项序号 (1-{n}) [默认: 1]: ",
        "compiled": "✨ 拼装完成的提示词 (Prompt):",
        "negative": "🛡️ 推荐负向排除词 (Negative Prompt):",
        "ratio_rec": "📐 推荐画幅比例: {ratio} ({label})",
        "launch": "👉 一键直达 Vistella 工作区生成:",
        "prefix": "https://www.vistella.xyz/zh/playground",
    },
    "3": {
        "title": "🌌 Vistella 提示詞命令列拼裝工具 (CLI)",
        "subtitle": "為 https://www.vistella.xyz 快速構建高質感提示詞",
        "step1": "1. 請輸入核心主體 / 畫面創意 (支援中英文):\n> ",
        "default_subject": "A female fashion model in an oversized charcoal coat",
        "step2": "2. 請輸入環境空間 / 背景元素 (按 Enter 可略過):\n> ",
        "step3": "3. 選擇光影佈光",
        "step4": "4. 選擇鏡頭光學",
        "step5": "5. 選擇色彩調色與底片",
        "step6": "6. 選擇畫幅比例",
        "select": "請輸入選項序號 (1-{n}) [預設: 1]: ",
        "compiled": "✨ 拼裝完成的提示詞 (Prompt):",
        "negative": "🛡️ 推薦負向排除詞 (Negative Prompt):",
        "ratio_rec": "📐 推薦畫幅比例: {ratio} ({label})",
        "launch": "👉 一鍵直達 Vistella 工作區生成:",
        "prefix": "https://www.vistella.xyz/zh/playground",
    },
}

LIGHTING_PRESETS = {
    "1": ("Golden Hour / 黄金暖光 / 黃金暖光", "soft warm low-angle golden hour sunlight with elongated gentle shadows"),
    "2": ("Studio Softbox / 摄影棚柔光 / 攝影棚柔光", "large octabox soft diffused studio lighting, balanced and neutral exposure"),
    "3": ("Volumetric Rays / 穿雾丁达尔光 / 穿霧廷得耳光", "dramatic volumetric god rays streaming through morning mist, Tyndall effect"),
    "4": ("Cinematic Neon / 赛博雨夜霓虹 / 賽博雨夜霓虹", "vibrant cyan and magenta neon ambient backlighting with wet glossy reflections"),
    "5": ("Overcast Soft / 阴天漫射光 / 陰天漫射光", "diffused soft overcast daylight, shadowless, true natural color fidelity"),
    "6": ("Chiaroscuro Noir / 伦勃朗明暗对比 / 林布蘭明暗對比", "chiaroscuro high-contrast lighting with deep velvety shadows and dramatic key light"),
}

OPTICS_PRESETS = {
    "1": ("85mm Portrait (f/1.4) / 肖像虚化定焦 / 肖像虛化定焦", "shot on 85mm f/1.4 prime lens, creamy shallow depth of field, sharp subject focus"),
    "2": ("50mm Natural Eye / 自然人眼视角 / 自然人眼視角", "shot on 50mm prime lens, natural human perspective, authentic organic field of view"),
    "3": ("35mm Street / Narrative / 人文环境街拍 / 人文環境街拍", "shot on 35mm f/1.8 lens, cinematic environmental perspective, subtle filmic depth"),
    "4": ("24mm Wide Architecture / 建筑移轴透视 / 建築移軸透視", "shot on 24mm tilt-shift wide-angle lens, straight vertical lines, expansive composition"),
    "5": ("100mm Macro Detail / 极致微距细节 / 極致微距細節", "extreme macro close-up photography, razor-thin focal plane, visible microscopic textures"),
}

COLOR_PRESETS = {
    "1": ("Kodak Portra 400 / 柯达暖调肤色 / 柯達暖調膚色", "warm Kodak Portra 400 color science, natural flattering skin tones, soft pastel highlights"),
    "2": ("Cinestill 800T / 卤化光晕夜景 / 鹵化光暈夜景", "Cinestill 800T tungsten film aesthetic, subtle red halation around specular highlights"),
    "3": ("Muted Minimalist / 极简米灰大地色 / 極簡米灰大地色", "monochromatic earthy palette of warm beige, travertine stone, and neutral gray tones"),
    "4": ("High-Contrast Monochrome / 经典银盐黑白 / 經典銀鹽黑白", "dramatic silver gelatin black and white photography, deep blacks, rich tonal graduation"),
    "5": ("Vibrant Anime / 新海诚动漫天空 / 新海誠動漫天空", "vibrant saturated anime color palette, lush sky gradients, Makoto Shinkai visual harmony"),
}

RATIO_PRESETS = {
    "1": ("1:1 (Square / 方形)", "1:1"),
    "2": ("3:4 (Portrait / 人像写真 / 人像寫真)", "3:4"),
    "3": ("4:5 (Vertical Feed / 社交信息流 / 社群資訊流)", "4:5"),
    "4": ("16:9 (Cinematic Widescreen / 电影宽屏 / 電影寬螢幕)", "16:9"),
    "5": ("9:16 (Vertical Story / 竖屏海报 / 豎屏海報)", "9:16"),
    "6": ("21:9 (Ultrawide Cinema / 超宽宽幅 / 超寬寬幅)", "21:9"),
}

DEFAULT_NEGATIVE = "deformed fingers, extra limbs, bad hands, plastic skin, unnatural face asymmetry, watermark, signature, blurry, low quality"


def prompt_menu(title, options, select_text):
    print(f"\n--- {title} ---")
    for key, (label, _) in options.items():
        print(f"  [{key}] {label}")
    choice = input(select_text.replace("{n}", str(len(options)))).strip()
    return options.get(choice, options["1"])


def main():
    print("=" * 60)
    print("  🌐 Language / 语言选择 / 語言選擇:")
    print("  [1] English (default)")
    print("  [2] 简体中文")
    print("  [3] 繁體中文")
    lang_choice = input("Select language (1-3) [default: 1]: ").strip()
    if lang_choice not in ("1", "2", "3"):
        lang_choice = "1"

    t = TEXTS[lang_choice]

    print("\n" + "=" * 60)
    print(f"  {t['title']}")
    print(f"  {t['subtitle']}")
    print("=" * 60)

    try:
        subject = input(f"\n{t['step1']}").strip()
        if not subject:
            subject = t["default_subject"]
            print(f"  (Default: '{subject}')")

        env = input(f"\n{t['step2']}").strip()

        light_label, light_text = prompt_menu(t["step3"], LIGHTING_PRESETS, t["select"])
        optics_label, optics_text = prompt_menu(t["step4"], OPTICS_PRESETS, t["select"])
        color_label, color_text = prompt_menu(t["step5"], COLOR_PRESETS, t["select"])
        ratio_label, ratio_val = prompt_menu(t["step6"], RATIO_PRESETS, t["select"])

        # Assemble prompt components
        components = [subject]
        if env:
            components.append(f"set in {env}")
        components.extend([light_text, optics_text, color_text, "masterpiece quality"])
        final_prompt = ", ".join(components) + "."

        print("\n" + "=" * 60)
        print(f"  {t['compiled']}")
        print("=" * 60)
        print(f"\n{final_prompt}\n")

        print("-" * 60)
        print(f"  {t['negative']}")
        print("-" * 60)
        print(f"\n{DEFAULT_NEGATIVE}\n")

        print("-" * 60)
        print("  " + t["ratio_rec"].format(ratio=ratio_val, label=ratio_label))
        print("-" * 60)

        # Web link
        encoded_prompt = urllib.parse.quote(final_prompt)
        web_link = f"{t['prefix']}?utm_source=cli_builder_{lang_choice}&prompt={encoded_prompt}"
        print(f"\n{t['launch']}")
        print(f"{web_link}\n")

    except KeyboardInterrupt:
        print("\nAborted.")
        sys.exit(0)


if __name__ == "__main__":
    main()
