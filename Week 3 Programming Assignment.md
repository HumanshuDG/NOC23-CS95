# Assignment $-$ 3

> Instructions:
> Write three Python functions as specified below. Paste the text for all three functions together into the submission window. Your function will be called automatically with various inputs and should return values as specified. Do not write commands to read any input or print any output.
> You may define additional auxiliary functions as needed.
> - In all cases, you may assume that the value passed to the function is of the expected type, so your function does not have to check for malformed inputs.
> - For each function, there are normally some public test cases and some (hidden) private test cases.
> - "Compile and run" will evaluate your submission against the public test cases.
> - "Submit" will evaluate your submission against the hidden private test cases. There are 12 private test cases, with equal weightage. You will get feedback about which private test cases pass or fail, though you cannot see the actual test cases.
> - Ignore warnings about "Presentation errors".

### 1. Write a function `expanding(l)` that takes as input a list of integer `l` and returns `True` if the absolute difference between each adjacent pair of elements strictly increases.

Here are some examples of how your function should work:
```
>>> expanding([1, 3, 7, 2, 9])
True
```
> **Explanation**\
> Differences between adjacent elements are:\
> 3 - 1 = 2\
> 7 - 3 = 4\
> 7 - 2 = 5\
> 9 - 2 = 7\
> Which is strictly increasing.

```
>>> expanding([1, 3, 7, 2, -3]) 
False
```
> **Explanation**\
> Differences between adjacent elements are:\
> 3 - 1 = 2\
> 7 - 3 = 4\
> 7 - 2 = 5\
> 2 - (-3) = 5\
> So, not strictly increasing.

```
>>> expanding([1, 3, 7, 2, 9])
True
```
> **Explanation**\
> Differences between adjacent elements are:\
> 3 - 1 = 2\
> 7 - 3 = 4\
> 10 - 7 = 3\
> So, not strictly increasing.

### Solution:
```
def expanding(l: list):
	flag = True
		for i in range(len(l) - 2):
			prev = abs(l[i] - l[i + 1])
			curr = abs(l[i + 1] - l[i + 2])
			if prev < curr:
				continue
			else:
				return False
	return flag
```

### 2. Write a Python function `sumsquare(l)` that takes a non-empty list of integers and returns a list `[odd, even]`, where `odd` is the sum of squares of all the odd numbers in `l` and `even` is the sum of squares of all the even numbers in `l`.

Here are some examples to show how your function should work:
```
>>> sumsquare([1, 3, 5])
[35, 0]

>>> sumsquare([2, 4, 6])
[0, 56]

>>> sumsquare([-1, -2, 3, 7])
[59, 4]
```

### Solution:
```
def sumsquare(l: list):
	sum_odd, sum_even = 0, 0
	for n in l:
		if n % 2:
			sum_odd += n ** 2
		else:
			sum_even += n ** 2
	return [sum_odd, sum_even]
```

3. A two-dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix.

For instance, the matrix:
```
1  2  3  4
5  6  7  8
```
would be represented as `[[1, 2, 3, 4], [5, 6, 7, 8]]`.\

The transpose of a matrix converts each row into a column. The transpose of the matrix above is:
```
3  2  1
6  5  4
9  8  7
```
which would be represented as `[[3, 2, 1], [6, 5, 4], [9, 8, 7]]`.\
A vertical flip reflects each column.\

For instance, if we flip the previous matrix that has already been flipped horizontally, we get:
```
1  5
2  6
3  7
4  8
```
which would be represented as `[[1, 5], [2, 6], [3, 7], [4, 8]]`.

Write a Python function `transpose(m)` that takes as input a two-dimensional matrix `m` and returns the transpose of `m`.\
The argument `m` should remain undisturbed by the function.

Here are some examples to show how your function should work. You may assume that the input to the function is always a non-empty matrix.
```
>>> transpose([[1, 2, 3], [4, 5, 6]])
[[1, 4], [2, 5], [3, 6]]

>>> transpose([[1], [2], [3]])
[[1, 2, 3]]

>>> transpose([[3]])
[[3]]
```

### Solution:
```

```
