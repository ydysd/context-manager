# Context manager

an object designed to be used in a with-statement
---
```python
with context-manager as ctxm:
    context-manager.begin()
    body
    context-manager.end()

```

---

## Context manager protocol
```python
__enter__(self)
__exit__(self, exc_type, exc_val, exc_tb)

```

- exc_type - exception type
- exc_val  - exception object
- exc_tb   - exception trace

---

[PEP 343](https://www.python.org/dev/peps/pep-0343/)


# contextlib

1. contextlib.contextmanager
