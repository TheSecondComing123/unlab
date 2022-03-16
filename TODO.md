# Elements:

## `i` Index
Get element at index
- Arity: 2

```
Overloads:
    str a, int b: a[b]
    int a, str b: b[a]
    int a, int b: str(a)[b]
    str a, str b: a[int(b)]
```
