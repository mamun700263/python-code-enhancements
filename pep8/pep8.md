
# 🐍 PEP 8 - Python Style Guide (Compressed)

> A minimal yet practical summary of Python's PEP 8 — simplified for quick understanding and clean coding.

---

## 🔹 Indentation
- Use **4 spaces** per level.
- **Never mix tabs and spaces**.

```python
def greet():
    print("Hello")
```

---

## 🔹 Line Length
- Limit lines to **79 characters**.
- For long expressions, use **parentheses** or `\`.

```python
total = (
    price + tax +
    shipping + discount
)
```

---

## 🔹 Blank Lines
- 2 blank lines before top-level **functions/classes**.
- 1 blank line between **methods** inside a class.
- Extra blank lines can be used *sparingly* to separate logic within functions.


---

## 🔹 Imports
- Imports go at the **top**.
- One import per line.
- Order:
  1. Standard libs
  2. Third-party
  3. Local modules

```python
import os
import sys

import requests

from my_app.utils import clean_data
```

---

## 🔹 Naming Conventions

| Type       | Style        | Example         |
|------------|--------------|-----------------|
| Variable   | `snake_case` | `user_name`     |
| Function   | `snake_case` | `get_data()`    |
| Class      | `PascalCase` | `UserProfile`   |
| Constant   | `UPPER_CASE` | `MAX_SIZE`      |

---

## 🔹 Whitespace Rules
✅ Good:
```python
x = 1 + 2
my_list = [1, 2, 3]
```

❌ Bad:
```python
x=1+2
my_list = [ 1 , 2 , 3 ]
```

---

## 🔹 Comments & Docstrings
- Use `#` for inline/single-line comments.
- Use `"""Docstrings"""` for modules, functions, classes.

```python
def add(a, b):
    """Add two numbers."""
    return a + b
```

---

## 🔹 Recommendations
- Use `is`/`is not` for `None`.
- Prefer **list comprehensions**.
- Catch **specific exceptions**.
- Avoid unnecessary `lambda`.

---

## 🔹 Type Hints (Python 3.5+)
```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```
## 🔹 The Main Entry Point

Use this to make your script runnable and also import-safe:

```python
if __name__ == "__main__":
    main()
```
---

## 🔹 Tools for Auto-formatting

| Tool     | Purpose                        |
|----------|--------------------------------|
| `black`  | Format code automatically      |
| `isort`  | Sort import statements         |
| `flake8` | Linting for style violations   |

```bash
pip install black isort flake8
black script.py
isort script.py
flake8 script.py
```
## DRY: don't repeat yourself
always try to reuse codes by making funcitons

```python
def send_email(user):
    # Logic to send email
    ...

send_email("mamun")
send_email("alex")

```

> `black` defaults to 88-character lines — PEP 8 says 79. Use `flake8` to catch long lines.

---
Look this guidline is to increase your code readabilty and works by making your code consistent . There will be some times when you might need to ignore some rules as they will be unablicable. On those moments you have to use your brain and take the best possible decision . 

## ✅ Final Tip
Write code like someone else will read it — because someone (or future you) will. Stick to the style, stay consistent, and let tools handle the rest.

---

🧠 _Maintained by Mamun — feel free to open a PR or issue for suggestions._
```

---
