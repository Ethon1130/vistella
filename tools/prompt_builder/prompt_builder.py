#!/usr/bin/env python3
"""
Vistella Visual Prompt Builder (CLI)
===================================
A lightweight, zero-dependency interactive tool to compose production-grade
prompts for AI visual creation on Vistella (https://www.vistella.xyz/playground).
"""

import sys
import urllib.parse

LIGHTING_PRESETS = {
    "1": ("Golden Hour", "soft warm low-angle golden hour sunlight with elongated gentle shadows"),
    "2": ("Studio Softbox", "large octabox soft diffused studio lighting, balanced and neutral exposure"),
    "3": ("Volumetric Rays", "dramatic volumetric god rays streaming through morning mist, Tyndall effect"),
    "4": ("Cinematic Neon", "vibrant cyan and magenta neon ambient backlighting with wet glossy reflections"),
    "5": ("Overcast Soft", "diffused soft overcast daylight, shadowless, true natural color fidelity"),
    "6": ("Chiaroscuro Noir", "chiaroscuro high-contrast lighting with deep velvety shadows and dramatic key light"),
}

OPTICS_PRESETS = {
    "1": ("85mm Portrait (f/1.4)", "shot on 85mm f/1.4 prime lens, creamy shallow depth of field, sharp subject focus"),
    "2": ("50mm Natural Eye", "shot on 50mm prime lens, natural human perspective, authentic organic field of view"),
    "3": ("35mm Street / Narrative", "shot on 35mm f/1.8 lens, cinematic environmental perspective, subtle filmic depth"),
    "4": ("24mm Wide Architecture", "shot on 24mm tilt-shift wide-angle lens, straight vertical lines, expansive composition"),
    "5": ("100mm Macro Detail", "extreme macro close-up photography, razor-thin focal plane, visible microscopic textures"),
}

COLOR_PRESETS = {
    "1": ("Kodak Portra 400", "warm Kodak Portra 400 color science, natural flattering skin tones, soft pastel highlights"),
    "2": ("Cinestill 800T", "Cinestill 800T tungsten film aesthetic, subtle red halation around specular highlights"),
    "3": ("Muted Minimalist", "monochromatic earthy palette of warm beige, travertine stone, and neutral gray tones"),
    "4": ("High-Contrast Monochrome", "dramatic silver gelatin black and white photography, deep blacks, rich tonal graduation"),
    "5": ("Vibrant Anime", "vibrant saturated anime color palette, lush sky gradients, Makoto Shinkai visual harmony"),
}

RATIO_PRESETS = {
    "1": ("1:1 (Square)", "1:1"),
    "2": ("3:4 (Portrait)", "3:4"),
    "3": ("4:5 (Vertical Feed)", "4:5"),
    "4": ("16:9 (Cinematic Widescreen)", "16:9"),
    "5": ("9:16 (Vertical Story)", "9:16"),
    "6": ("21:9 (Ultrawide Cinema)", "21:9"),
}

DEFAULT_NEGATIVE = "deformed fingers, extra limbs, bad hands, plastic skin, unnatural face asymmetry, watermark, signature, blurry, low quality"


def prompt_menu(title, options):
    print(f"\n--- {title} ---")
    for key, (label, _) in options.items():
        print(f"  [{key}] {label}")
    choice = input(f"Select option (1-{len(options)}) [default: 1]: ").strip()
    return options.get(choice, options["1"])


def main():
    print("=" * 60)
    print("  🌌 Vistella Visual Prompt Builder (CLI)")
    print("  Craft production-ready prompts for https://www.vistella.xyz")
    print("=" * 60)

    try:
        subject = input("\n1. Enter your core subject / idea:\n> ").strip()
        if not subject:
            subject = "An architectural pavilion in a serene bamboo grove"
            print(f"  (Using default: '{subject}')")

        env = input("\n2. Enter environment / background (press Enter to skip):\n> ").strip()

        light_label, light_text = prompt_menu("3. Select Lighting", LIGHTING_PRESETS)
        optics_label, optics_text = prompt_menu("4. Select Camera Optics", OPTICS_PRESETS)
        color_label, color_text = prompt_menu("5. Select Color & Film Grade", COLOR_PRESETS)
        ratio_label, ratio_val = prompt_menu("6. Select Aspect Ratio", RATIO_PRESETS)

        # Assemble prompt components
        components = [subject]
        if env:
            components.append(f"set in {env}")
        components.extend([light_text, optics_text, color_text, "masterpiece quality"])
        final_prompt = ", ".join(components) + "."

        print("\n" + "=" * 60)
        print("  ✨ COMPILED PROMPT:")
        print("=" * 60)
        print(f"\n{final_prompt}\n")

        print("-" * 60)
        print("  🛡️ RECOMMENDED NEGATIVE PROMPT:")
        print("-" * 60)
        print(f"\n{DEFAULT_NEGATIVE}\n")

        print("-" * 60)
        print(f"  📐 RECOMMENDED RATIO: {ratio_val} ({ratio_label})")
        print("-" * 60)

        # Web link
        encoded_prompt = urllib.parse.quote(final_prompt)
        web_link = f"https://www.vistella.xyz/playground?utm_source=cli_builder&prompt={encoded_prompt}"
        print("\n👉 OPEN DIRECTLY IN VISTELLA PLAYGROUND:")
        print(f"{web_link}\n")

    except KeyboardInterrupt:
        print("\nAborted.")
        sys.exit(0)


if __name__ == "__main__":
    main()
