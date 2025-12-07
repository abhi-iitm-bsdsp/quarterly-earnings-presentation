---
marp: true
title: Product Documentation Presentation
theme: custom-theme
paginate: true
paginate-style: "font-size: 0.7em; text-align: right; color: #666;"
---

<!-- Custom Theme -->
<style>
section {
  font-family: "Segoe UI", sans-serif;
}

h1 {
  color: #2d6cdf;
}

footer {
  font-size: 0.6em;
  text-align: right;
}

section.center-large h1 {
  font-size: 2.2em;
}

img.bg-cover {
  object-fit: cover;
}
</style>

<!-- Custom Theme Definition -->
<!-- You can also save this as a .css file, but inline works in Marp -->
<style>
:root {
  --color-background: #ffffff;
  --color-foreground: #1a1a1a;
  --color-accent: #2d6cdf;
}
</style>

# 📘 Product Documentation  
### Technical Writer Presentation  
**Created by:** 23f1001785@ds.study.iitm.ac.in

---

# 📄 Agenda
- Introduction  
- Documentation Principles  
- Version Control Workflow  
- Rendering to Multiple Formats  
- Algorithmic Complexity Example  
- Summary  

---

# 🧩 What is Good Documentation?

- Clear and concise writing  
- Version-controlled source (Markdown preferred)  
- Renderable to:  
  - PDF  
  - HTML  
  - Slides  
  - GitHub Pages  
- Automated builds via CI/CD  

---

<!-- Slide With Background Image -->
<!-- Replace URL with any valid public image -->
![bg](https://images.unsplash.com/photo-1547658718-1cdaa085b6f6?auto=format&fit=crop&w=1350&q=80)

# ✨ Documentation at Scale
Maintaining consistency across teams and products requires:
- Style guides  
- Templates  
- Automated checks  

---

# 🔢 Algorithmic Complexity

We often document algorithms with complexity analysis:

### Example  
Bubble sort complexity is:

\[
T(n) = O(n^2)
\]

Binary search complexity:

\[
T(n) = O(\log n)
\]

---

# 🛠 Version Control Workflow

1. Edit Markdown  
2. Commit changes  
3. Generate HTML / PDF using Marp CLI  
4. Publish to repository or GitHub Pages  

---

# 🏁 Summary

- Marp enables documentation-as-code  
- Markdown is maintainable and version-friendly  
- Supports themes, diagrams, equations, automation  
- Easily export to multiple formats  

---

# 📧 Contact
**23f1001785@ds.study.iitm.ac.in**

Thank you!
