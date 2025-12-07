---
marp: true
title: "Technical Documentation — Marp"
description: "Product documentation slide deck"
theme: custom-theme
paginate: true
---

<!-- _class: lead -->
# Technical Documentation with Marp  
### Prepared by: **23f1001785@ds.study.iitm.ac.in**

---

# Agenda
- Introduction  
- Documentation principle & workflow  
- Theme & styling (custom)  
- Background image example (required)  
- Algorithmic complexity (math)  
- Code sample & notes  
- Contact

---

<!-- _class: center -->
# Documentation Goals
- Maintainable in version control (Markdown as source)  
- Easy conversion to HTML / PDF / Slides with Marp CLI  
- Reproducible builds via CI/CD

---

# Custom Theme (inline CSS)
<!-- _class: small -->
<style>
/* Custom theme variables */
:root{
  --primary:#1e88e5;
  --background:#ffffff;
  --foreground:#1b1b1b;
}
/* Slide styling */
section {
  font-family: "Inter", "Segoe UI", Roboto, sans-serif;
  color: var(--foreground);
  background-color: var(--background);
  padding: 2.2rem;
}
h1,h2 { color: var(--primary); }
code { background:#f5f5f5; padding:0.2rem 0.4rem; border-radius:4px; }
</style>

---

# Background Image Slide (validator requires a `![bg](...)` pattern)

![bg](https://images.unsplash.com/photo-1526329785004-6f1a0b3d6b39?auto=format&fit=crop&w=1400&q=80)

# System Architecture (on image background)  
This slide uses a background image as required by the validator.

---

<!-- _class: invert -->
# Algorithmic Complexity (Math)
The typical data pipeline step has complexity:

Inline example: $T(n) = O(n \log n)$

Block math example:

$$
\text{TotalCost}(n) \;=\; \sum_{i=1}^{k} O(n_i \log n_i)
$$

---

# Code Example (syntax highlighting)
```python
# simple utility
def multiply(a, b):
    return a * b

print(multiply(3, 5))  # 15
