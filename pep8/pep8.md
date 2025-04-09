

# PEP 8 - Python Style Guide (Compressed Overview)

PEP 8 is the official Python style guide that ensures code is readable, consistent, and maintainable. It's a set of conventions that guide how Python code should be written and formatted.

---

### 1. **Indentation**
- **Use 4 spaces per indentation level**. Never mix tabs and spaces.
- Code blocks are defined by indentation.
- Example:
    ```python
    def function():
        if condition:
            do_something()
    ```

### 2. **Line Length**
- Limit all lines to **79 characters** (72 for docstrings).
- Break long lines with `\` or use parentheses to make it more readable.
    ```python
    some_variable = (
        first_part_of_the_value + 
        second_part_of_the_value
    )
    ```

### 3. **Blank Lines**
- **Two blank lines** before top-level functions and classes.
- **One blank line** between methods inside a class.
- Use blank lines to separate logical sections in functions for better readability.

### 4. **Imports**
- Imports should be on separate lines:
    ```python
    import os
    import sys
    ```
- Group imports into three sections:
    1. Standard library imports.
    2. Third-party imports.
    3. Local application imports.

- **Import all modules** at the top of the file.

### 5. **Naming Conventions**
- **Function and variable names**: `snake_case` (e.g., `my_variable`).
- **Class names**: `PascalCase` (e.g., `MyClass`).
- **Constants**: `UPPERCASE_WITH_UNDERSCORES` (e.g., `MAX_LIMIT`).
- **Method names**: Follow the same pattern as functions.
- **Avoid single character variable names** unless used in loops or mathematical operations.

### 6. **Whitespace in Expressions**
- Avoid extra spaces around operators, except in specific cases:
    ```python
    x = 1 + 2
    y = (1 + 2) * (3 + 4)
    ```

- **Around assignment (`=`)**:
    ```python
    x = 1  # Correct
    x  = 1  # Incorrect
    ```

### 7. **Comments**
- Use **inline comments** sparingly, and only when the code isn’t self-explanatory.
- **Block comments**: Start with a `#` and use complete sentences.
- **Docstrings**: Use triple quotes `"""` for function/method docstrings.

Example:
```python
def function(arg1, arg2):
    """
    This function does something important with arg1 and arg2.
    """
    return arg1 + arg2
```

### 8. **Docstrings**
- Write docstrings for all public modules, functions, classes, and methods.
- Keep them concise but descriptive. The first line should be a brief summary.

### 9. **Programming Recommendations**
- **Use list comprehensions** for simple cases instead of `for` loops.
    ```python
    squares = [x**2 for x in range(10)]
    ```

- **Avoid using `global`** unless absolutely necessary.

- **Use `is` for comparisons with `None`**, not `==`.
    ```python
    if variable is None:
        # Correct
    if variable == None:
        # Incorrect
    ```

- **Avoid unnecessary lambda functions** when a normal function would suffice.

### 10. **Version Compatibility**
- Code should be compatible with **Python 3**.
- Avoid old Python 2-style code.

### 11. **Error Handling**
- Use **exceptions** for error handling instead of error codes.
- Catch specific exceptions, not generic ones.

Example:
```python
try:
    do_something()
except FileNotFoundError:
    print("File not found!")
```

### 12. **Type Annotations**
- Include **type hints** in function signatures for clarity:
    ```python
    def add(x: int, y: int) -> int:
        return x + y
    ```

### 13. **Avoiding Double Underscore Names**
- Use double underscores (`__name__`) only for special methods (e.g., `__init__`), to avoid name clashes.

### 14. **Miscellaneous**
- **Keep code DRY (Don't Repeat Yourself)**.
- **Use `enumerate()`** instead of `range(len())` for better readability in loops.

---

### Summary
PEP 8 is about making your code easier to read, understand, and maintain. By following these conventions, you make it easier for others (and yourself) to work with your Python code in the future. For the full guide, check the official [PEP 8 documentation](https://www.python.org/dev/peps/pep-0008/).

---

### Tips:
- **Readability over cleverness**: Always prefer code that’s easy to understand, even if it’s a bit longer.
- **Consistency**: Be consistent with your style across all codebases.

---

