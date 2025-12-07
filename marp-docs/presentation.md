---
marp: true
title: Product Documentation
paginate: true
theme: custom-theme
class: lead
---

<!-- Custom Theme -->
<style>
section {
  font-family: "Segoe UI", sans-serif;
}

h1 {
  color: #1e88e5;
}

p {
  font-size: 26px;
}

footer {
  color: #666;
}

/* Custom page number styling */
section::after {
  content: attr(data-marpit-pagination) " / " attr(data-marpit-pagination-total);
  position: absolute;
  bottom: 15px;
  right: 30px;
  font-size: 18px;
  opacity: 0.7;
}
</style>

<!-- Theme Definition -->
<style id="custom-theme">
:root {
  --background-color: #ffffff;
  --text-color: #222222;
}

section {
  background-color: var(--background-color);
  color: var(--text-color);
}
</style>

# 📘 Product Documentation  
### Prepared by  
**23f1001785@ds.study.iitm.ac.in**

---

# 📦 Product Overview

Our software platform provides:

- Modular architecture  
- Secure API framework  
- Real-time analytics  
- Cloud scalability  

This documentation illustrates the architecture and complexity breakdown.

---

<!-- Background image slide -->
<!-- Replace the image URL with any public or repo-hosted image -->
<!-- Example background image from Unsplash -->
![bg](https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200)

# System Architecture  
### (With background image)

---

# 🔧 Setup Instructions

To install:

```bash
git clone https://github.com/your/repo.git
cd repo
npm install
npm start
