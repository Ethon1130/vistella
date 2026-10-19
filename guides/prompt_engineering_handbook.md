# 📚 The Vistella Visual Prompt Engineering Handbook

A comprehensive, production-grade guide to mastering composition, lighting, camera optics, and aesthetic styling for AI visual creation on [Vistella (vistella.xyz)](https://www.vistella.xyz/en/playground?utm_source=github&utm_medium=handbook).

---

## 🎯 The Core Philosophy: Natural Description over Keyword Stuffing

Early AI image systems relied on long lists of buzzwords (e.g. `trending on artstation, 8k, hyperrealistic, masterpiece`).  
Modern generation systems on Vistella are fundamentally **semantic-first**:
- They understand **spatial relationships**, **material physics**, and **photographic conventions**.
- Full descriptive phrases yield far better visual coherence than comma-separated tag clouds.

---

## 💡 Chapter 1: The Lighting Masterclass

Lighting dictates 70% of the mood, depth, and three-dimensionality of your image. Always specify light sources and their quality.

### 1.1 Natural & Environmental Lighting
| Lighting Type | Prompt Keyword | Best For | Visual Impact |
| :--- | :--- | :--- | :--- |
| **Golden Hour** | `golden hour warm low-angle sunlight` | Portraits, Landscapes, Architecture | Warm amber highlights, long soft shadows |
| **Blue Hour** | `blue hour twilight, cool ambient tones` | Cityscapes, Moody Portraits | Deep cerulean sky, calm and contemplative |
| **Overcast Diffused** | `diffused soft overcast skylight, shadowless` | Fashion, Editorial, Product Shots | Even exposure, highly accurate color fidelity |
| **Dappled / Foliage** | `dappled sunlight filtering through tree leaves` | Outdoor Portraits, Still Life | Organic shadows, high depth of field |
| **Volumetric Rays** | `god rays, volumetric sunbeams through mist` | Forest, Ancient Temples, Lofts | Tyndall effect, cinematic drama |

### 1.2 Studio & Artificial Lighting
| Technique | Prompt Keyword | Visual Impact |
| :--- | :--- | :--- |
| **Rembrandt Lighting** | `Rembrandt lighting, subtle triangle shadow on cheek` | Classic, dramatic portraiture |
| **Rim / Edge Light** | `strong volumetric rim lighting, illuminated silhouette` | Separates subject from dark background |
| **Softbox Studio** | `large octabox soft diffused studio lighting` | Clean commercial and e-commerce looks |
| **Neon Backlight** | `neon backlight with cyan and magenta color bleed` | Cyberpunk, streetwear, nighttime urban |
| **Chiaroscuro** | `chiaroscuro high-contrast lighting, deep deep shadows` | Baroque, moody fine art |

---

## 📷 Chapter 2: Camera Optics, Lenses & Perspective

Simulating real-world camera optics gives your creations tangible physical realism and removes the "AI synthetic" feel.

### 2.1 Focal Lengths & Field of View
- **Wide Angle (16mm - 24mm)**: `shot on 20mm ultra-wide lens, dynamic perspective, expansive background`  
  *Best for:* Dramatic architecture, grand landscapes, immersive action.
- **Classic Street & Narrative (35mm)**: `shot on 35mm f/1.8 lens, cinematic street photography perspective`  
  *Best for:* Environmental portraits, documentary aesthetic, authentic candid moments.
- **Standard Natural Eye (50mm)**: `50mm prime lens, natural field of view, gentle depth of field`  
  *Best for:* Everyday lifestyle, editorial portraits, balanced product displays.
- **Portrait Telephoto (85mm - 135mm)**: `shot on 85mm f/1.2 lens, creamy shallow depth of field, compressed background`  
  *Best for:* Studio beauty close-ups, professional headshots, isolating subjects.
- **Macro (100mm Macro)**: `extreme close-up macro photography, visible microscopic texture, razor-thin focal plane`  
  *Best for:* Jewelry, water droplets, botanical details, iris close-ups.

### 2.2 Camera Systems for Style Emulation
- **Hasselblad / Medium Format**: `shot on Hasselblad H6D-100c medium format, ultimate clarity, neutral studio color science`
- **Leica M Series**: `Leica M11 aesthetic, authentic contrast, street documentary richness`
- **Analog 35mm Film**: `vintage 35mm film photography, subtle halation, organic grain, Kodak Portra 400 tones`

---

## 🎨 Chapter 3: Color Science & Film Emulation

Color grading establishes subconscious emotion. Instead of generic "colorful", use professional color terms:

| Color Grading | Prompt Phrase | Emotional Tone |
| :--- | :--- | :--- |
| **Kodak Portra 400** | `Kodak Portra 400 tones, flattering warm skin, soft pastel highlights` | Nostalgic, human, warm editorial |
| **Cinestill 800T** | `Cinestill 800T tungsten film look, red halation around bright neon lights` | Nighttime, retro-cinematic, moody |
| **Fujifilm Pro 400H** | `Fujifilm Pro 400H colors, airy soft greens, delicate cool cyan shadows` | Clean, fresh, fine art wedding |
| **Monochromatic Noir**| `high-contrast black and white, deep silver tones, rich velvety blacks` | Dramatic, timeless, classic |
| **Muted Earth Tones** | `monochromatic earthy palette of beige, raw linen, travertine, and ochre` | Modern luxury, architectural, calm |

---

## 📐 Chapter 4: Composition & Framing Rules

Guide the visual flow of the viewer's eye:

1. **Rule of Thirds**: `off-center subject positioned along the right third, breathing room in negative space`
2. **Symmetrical Geometry**: `perfect architectural symmetry, centered composition, balanced reflection`
3. **Low-Angle Hero Shot**: `shot from a low dramatic upward angle, imposing silhouette against sky`
4. **High-Angle / Bird's-Eye**: `overhead top-down knolling perspective, flat-lay arrangement, clean 90-degree angle`
5. **Framing Within a Frame**: `subject viewed through a geometric doorway arch, layered foreground bokeh`

---

## 🛡️ Chapter 5: Negative Prompt Optimization

Negative prompts act as guardrails. Use them strategically rather than randomly pasting giant blocklists.

- **For People & Portraits**:
  ```text
  deformed fingers, extra limbs, bad hands, plastic skin, unnatural face asymmetry, cross-eyed, watermark, signature
  ```
- **For Clean Commercial Shots**:
  ```text
  dust, scratches, fingerprints, harsh reflections, cluttered background, cartoon, oversaturated, blurry
  ```
- **For Architecture & Interiors**:
  ```text
  warped pillars, crooked perspective, uneven floors, messy wires, cartoonish, low resolution
  ```

---

## 🚀 Take It to the Canvas

Practice combining these elements directly on [Vistella (星境)](https://www.vistella.xyz/en/playground?utm_source=github&utm_medium=handbook_bottom).

> **Pro Tip:** Start with **Subject + Lighting**, test the result, then layer in **Lens/Optics + Color Grading** to fine-tune the final mood.
