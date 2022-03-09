#Elements:  
`ǃ` (Uppercase/Plus one)&nbsp;&nbsp;Arity 1 
&nbsp;&nbsp;&nbsp;&nbsp;Either uppercases a string or adds one to a number.

```
Overloads:
    int a: a+1
    str a: a.upper()
```

`¡` (Lowercase/Minus one)&nbsp;&nbsp;Arity 1 
&nbsp;&nbsp;&nbsp;&nbsp;Either lowercases a string or subtracts one from a number.

```
Overloads:
    int a: a-1
    str a: a.lower()
```

`□` (Swap case/Negate)&nbsp;&nbsp;Arity 1 
&nbsp;&nbsp;&nbsp;&nbsp;Either swaps the case of a string or negates a number.

```
Overloads:
    int a: -a
    str a: a.swapcase()
```
