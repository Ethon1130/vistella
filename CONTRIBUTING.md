# 🤝 Contributing to Vistella Community Resources

Thank you for your interest in contributing to the Vistella open-source repository! We welcome prompt recipes, visual engineering insights, style presets, and documentation improvements.

---

## 🌟 How You Can Contribute

1. **Submit New Prompt Recipes**:
   - Tested in the [Vistella Web Playground](https://www.vistella.xyz/playground?utm_source=github&utm_medium=contributing).
   - Produces consistent, high-fidelity visual results.
   - Categorized under the appropriate markdown file in `prompts/`.
2. **Refine Negative Prompts**:
   - Share effective negative tokens that eliminate specific artifacts (e.g. hand geometry, glass reflections, font noise).
3. **Enhance Guides & Documentation**:
   - Expand the [Prompt Engineering Handbook](guides/prompt_engineering_handbook.md) or add new domain breakdowns (e.g. food photography, macro jewelry, concept vehicles).

---

## 📝 Prompt Recipe Format

When submitting a new recipe via Pull Request, please follow this standardized format:

```markdown
## 🌟 Recipe Name

- **Recommended Ratio:** `1:1`, `16:9`, `3:4`, etc.
- **Lighting:** Describe the lighting setup
- **Style / Atmosphere:** Key aesthetic mood

\`\`\`text
Your full descriptive prompt text here...
\`\`\`

👉 [Run this Recipe on Vistella Playground →](https://www.vistella.xyz/playground?utm_source=github&utm_medium=community_recipe)
```

---

## 🛠️ Contribution Workflow

1. Fork this repository on GitHub.
2. Clone your fork locally:
   ```bash
   git clone https://github.com/<your-username>/vistella.git
   cd vistella
   ```
3. Create a feature branch:
   ```bash
   git checkout -b feature/my-new-prompt-recipe
   ```
4. Commit your changes:
   ```bash
   git commit -m "feat(prompts): add cybernetic portrait recipe"
   ```
5. Push to your branch and open a Pull Request!

---

## 📜 Community Code of Conduct

- Be welcoming, respectful, and constructive.
- Ensure all contributed prompt texts adhere to ethical visual creation standards.
- Content must not contain defamatory, hateful, or non-consensual material.
