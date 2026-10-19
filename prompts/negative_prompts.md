# 🛡️ Vistella Negative Prompt Library & Quality Enhancers

Negative prompts help steer generation away from common artifacts, plastic-looking skin, anatomical errors, and unwanted clutter.

You can paste these negative prompt recipes directly into the **Negative Prompt** input in the [Vistella Playground](https://www.vistella.xyz/en/playground?utm_source=github&utm_medium=negative_prompts_guide).

---

## 📸 1. Photorealistic Portraits & People

Use this when generating realistic human portraits, street photography, or fashion editorials:

```text
deformed fingers, extra limbs, poorly drawn hands, unnatural face proportions, distorted pupils, plastic skin, oversaturated, low quality, blurred background clutter, watermark, text, signature, duplicate face, asymmetrical eyes
```

### Why it works:
- Suppresses plastic/wax figure skin textures.
- Keeps hands and eye geometry aligned.
- Prevents random watermarks or digital signatures from appearing.

---

## 🏺 2. Commercial Products & Still Life

Use this for luxury product photography, perfumes, packaging, and industrial design:

```text
fingerprints, scratches, dust, distorted label text, messy background, harsh unflattering shadows, bad reflections, overexposed highlights, chromatic aberration, cartoon, anime, illustration
```

### Why it works:
- Keeps product surfaces immaculate (scratch-free, dust-free).
- Prevents stylized illustrations from contaminating photorealistic product shots.

---

## 🏛️ 3. Architecture & Interior Design

Use this for buildings, spatial pavilions, and modern interiors:

```text
tilted perspective, warped pillars, uneven floors, crooked window frames, messy wiring, clutter, blurry textures, cartoonish rendering, lowres, oversaturated colors
```

### Why it works:
- Enforces geometric precision and vertical architectural alignments.
- Keeps interior floors and lighting clean.

---

## 🎨 4. Digital Art & Anime

Use this for fantasy concept art, character illustrations, and anime scenes:

```text
mutated anatomy, bad hands, missing fingers, extra eyes, muddy colors, bad lineart, compressed jpeg artifacts, cropped, worst quality, low quality, glitch
```

---

## 💡 Best Practices

1. **Keep Negative Prompts Focused**: Adding 200+ negative tokens can dilute prompt fidelity and wash out natural color grading. 15-25 targeted tokens are ideal.
2. **Complement with Lighting**: If an image feels washed out, reinforce lighting descriptors in your main prompt (e.g., *"volumetric rim light"*, *"deep contrasting shadows"*) rather than over-relying on negative keywords.
3. **Test in Real Time**: Experiment with different combinations in the [Vistella Web App](https://www.vistella.xyz/en/playground?utm_source=github&utm_medium=negative_prompts_footer).
