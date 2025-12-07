# marimo notebook
import marimo as mo

# --- Cell 1: basic variable ---
a = 10
# This cell defines 'a'

# --- Cell 2: dependent variable (required by validator) ---
# This cell depends on variable a
b = a * 2

# --- Cell 3: interactive slider widget ---
slider = mo.ui.slider(start=1, stop=100, value=20, label="Select a number")

# --- Cell 4: dynamic markdown output ---
mo.md(f"""
# Interactive Data Analysis Notebook  
Email: **23f1001785@ds.study.iitm.ac.in**

The value of **a** is `{a}`,  
The value of **b = a * 2** is `{b}`.

The slider value is: **{slider.value}**
""")

# --- Cell 5: show interactive slider ---
slider
