# Usage

```python
from pytakeout import extract_code, code_to_file


def func_to_extract():
    # This function needs to be extracted.
    return True


# Extract code as a string.
code = extract_code(func_to_extract)

# Save it into a temporary file.
tmp_code_file = code_to_file(code)
```
