# unlist_nested

A simple Python package to unlist (flatten) a list of any level of nesting.

## Installation

```bash
pip install unlist_nested
```

## Usage

```python
from unlist_nested import unlist

nested = [1, [2, [3, 4], 5], 6]
flat = unlist(nested)
print(flat)
# Output: [1, 2, 3, 4, 5, 6]
```
