# pytakeout

<https://github.com/idlesign/pytakeout>

[![release](https://img.shields.io/pypi/v/pytakeout.svg)](https://pypi.python.org/pypi/pytakeout)
[![lic](https://img.shields.io/pypi/l/pytakeout.svg)](https://pypi.python.org/pypi/pytakeout)
[![coverage](https://img.shields.io/coveralls/idlesign/pytakeout/master.svg)](https://coveralls.io/r/idlesign/pytakeout)

## Description

*Simplifies Python code extraction*

With this you can easily:

* extract function/method/class source code;
* perform basic code transformations;
* save code into a file.

## Sample

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
