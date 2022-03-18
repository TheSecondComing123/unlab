# Elements:

## `s` Slice
Slice a string
- Arity: 3

```
Overloads:
    a, b, c (any: str|int): a[b:c]
```

## `h` Slice from start
Slice a string from index 0
- Arity: 2

```
Overloads:
    a, b (any: str|int): a[:b]
```

## `t` Slice until end
Slice a string until end
- Arity: 2

```
Overloads:
    a, b (any: str|int): a[b:]
```