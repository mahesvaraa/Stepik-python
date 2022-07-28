# Find the smallest

https://www.codewars.com/kata/573992c724fc289553000e95

You have a positive number n consisting of digits. You can do at most one operation: Choosing the index of a digit in
the number, remove this digit at that index and insert it back to another or at the same place in the number in order to
find the smallest number you can get.

**Task:**

Return an array or a tuple or a string depending on the language (see "Sample Tests") with

the smallest number you got
the index i of the digit d you took, i as small as possible
the index j (as small as possible) where you insert this digit d to have the smallest number.

**Examples:**

```python
smallest(261235) --> [126235, 2, 0] or (126235, 2, 0) or "126235, 2, 0"
```

126235 is the smallest number gotten by taking 1 at index 2 and putting it at index 0

```python
smallest(209917) --> [29917, 0, 1] or ...

[29917, 1, 0] could be a solution too but index `i` in [29917, 1, 0] is greater than 
index `i` in [29917, 0, 1].
```

29917 is the smallest number gotten by taking 2 at index 0 and putting it at index 1 which gave 029917 which is the
number 29917.

```python
smallest(1000000) --> [1, 0, 6] or ...
```

**Note**

Have a look at "Sample Tests" to see the input and output in each language

# Solution

```python
def smallest(n):
    min, min_idx, min_idx2 = n, 0, 0
    y = list(str(n))
    for i in range(len(y)):
        for j in range(len(y)):
            y.insert(j, y.pop(i))
            if int(''.join(y)) < min:
                min, min_idx, min_idx2 = int(''.join(y)), i, j
            y = list(str(n))
    return [min, min_idx, min_idx2]
```