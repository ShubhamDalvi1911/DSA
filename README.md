# DSA 🚀

**A collection of Data Structures & Algorithms implementations and practice problems in Python.**

## Overview
This repository contains implementations, notes, and solved problems organized by topic. It's intended for learning, reference, and small experiments.

## Features
- Implementations of DSA in Python.

## Project structure
- `Array/` — array implementations and examples (e.g., `dynamicarray.py`)
- `LinkedList/` — linked list implementations and examples (e.g., `linkedlist.py`) 
- `LinkedList/Assignment` — linked list questions and Answers (e.g., `replace_max.py , sum_odd_nodes , change_sentance , reverse_linkedlist`)

## Modules
- `Modules/` — reusable modules used by assignment scripts and examples:
  - `Modules/LL.py` — a simple `LinkedList` (and `Node`) implementation intended for reuse across scripts; assignment examples import it with `import Modules.LL as LL`.

**Note:** For imports like `Modules.LL` to work when running files directly, run scripts from the repository root (recommended), or the scripts add the project root to `sys.path` at runtime.

## Topics covered
- **Array** — Dynamic array implementation (`Array/dynamicarray.py`) ✅ **Covered**
  - Implementation includes:
    1. Create List
    2. len
    3. append
    4. print
    5. indexing
    6. pop
    7. clear
    8. find
    9. insert
    10. delete
    11. remove
- **LinkedList** — Singly linked list implementation (`LinkedList/linkedlist.py`) ✅ **Covered**
  - Implementation includes:
    1. Node class
    2. Linked List class
    3. len
    4. Print the linked list
    5. Insert at head
    6. Insert at tail
    7. Insert after a value
    8. Clear LL
    9. Delete at head
    10. Delete at tail
    11. Delete by value
    12. Delete by index
    13. Search by value
    14. Search by index 

## Requirements
- Python 3.8+

## Usage
Run an example file directly:

```bash
python Array/dynamicarray.py
```

Or import and use the implementation from your scripts:

```python
from Array.dynamicarray import MereList

lst = MereList()
lst.append("Alice")
lst.append(42)
print(lst, len(lst))
```

## Contributing
Contributions are welcome — open an issue or a pull request. Please keep changes small and include tests or examples when possible.

---

*Progress log:* Working through topics folder-by-folder; more content will be added as I practice and solve problems.
