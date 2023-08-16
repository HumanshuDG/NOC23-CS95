# Assignment $-$ 4

> Instructions:
> Write two Python functions as specified below. Paste the text for all three functions together into the submission window. Your function will be called automatically with various inputs and should return values as specified.\
> Do not write commands to read any input or print any output.
> - You may define additional auxiliary functions as needed.
> - In all cases, you may assume that the value passed to the function is of the expected type, so your function does not have to check for malformed inputs.
> - For each function, there are normally some public test cases and some (hidden) private test cases.
> - "Compile and run" will evaluate your submission against the public test cases.
> - "Submit" will evaluate your submission against the hidden private test cases. There are 10 private test cases, with equal weightage. You will get feedback about which private test cases pass or fail, though you cannot see the actual test cases.
> - Ignore warnings about "Presentation errors".

### 1. Write a Python function `histogram(l)` that takes as input a list of integers with repetitions and returns a list of pairs as follows:
- for each number `n` that appears in `l`, there should be exactly one pair `(n, r)` in the list returned by the function, where `r` is the number of repetitions of `n` in `l`.
- the final list should be sorted in ascending order by `r`, the number of repetitions. For numbers that occur with the same number of repetitions, arrange the pairs in ascending order of the value of the number.

For instance:
```
>>> histogram([13,12,11,13,14,13,7,7,13,14,12])
[(11, 1), (7, 2), (12, 2), (14, 2), (13, 4)]

>>> histogram([7,12,11,13,7,11,13,14,12])
[(14, 1), (7, 2), (11, 2), (12, 2), (13, 2)]

>>> histogram([13,7,12,7,11,13,14,13,7,11,13,14,12,14,14,7])
[(11, 2), (12, 2), (7, 4), (13, 4), (14, 4)]
```

### Solution:
```
def histogram(l: list):
	return
```

### 2. A college maintains academic information about students in three separate lists:
- course_details: A list of pairs of form `(coursecode, coursename)`, where both entries are strings.\
For instance, `[("MA101", "Calculus"), ("PH101", "Mechanics"), ("HU101", "English")]`.
- student_details: 
For instance, `[("UGM2018001", "Rohit Grewal"), ("UGP2018132", "Neha Talwar")]`.
- grades: 
For instance, `[("UGM2018001", "MA101", "AB"), ("UGP2018132", "PH101", "B"), ("UGM2018001", "PH101", "B")]`.

You may assume that each roll number and course code in the grade list appears in the student details and course details, respectively.
Your task is to write a function `transcript(course_details, student_details, grades)` that takes these three lists as input and produces consolidated grades for each student.

Each of the input lists may have its entries listed in arbitrary order. Each entry in the returned list should be a tuple of the form\
`(rollnumber, name, [(coursecode_1, coursename_1, grade_1), ..... , (coursecode_k, coursename_k, grade_k)])`\
where the student has grades for $k \geq 1$ courses reported in the input list grades.

The output list should be organized as follows:
- The tuples should be sorted in ascending order by roll number.
- Each student's grades should be sorted in ascending order by course code.

For instance:
```
>>>transcript([("MA101", "Calculus"), ("PH101", "Mechanics"),("HU101", "English")],
				[("UGM2021001", "Rohit Grewal"),("UGP2021132", "Neha Talwar")],
				[("UGM2021001", "MA101", "AB"),("UGP2021132", "PH101", "B"),("UGM2021001", "PH101", "B")])
[('UGM2021001', 'Rohit Grewal', [('MA101', 'Calculus', 'AB'), ('PH101', 'Mechanics', 'B')]), ('UGP2021132', 'Neha Talwar', [('PH101', 'Mechanics', 'B')])]

>>>transcript([("T1", "Test 1"),("T2", "Test 2"),("T3", "Test 3")],
				[("Captain", "Rohit Sharma"),("Batsman", "Virat Kohli"),("No3", "Cheteshwar Pujara")],
				[("Batsman", "T1", "14"),("Captain", "T1", "33"),("No3", "T1", "30"),("Batsman", "T2", "55"),("Captain", "T2", "158"),("No3", "T2", "19"), ("Batsman", "T3", "33"),("Captain", "T3", "95"),("No3", "T3", "51")])
[('Batsman', 'Virat Kohli', [('T1', 'Test 1', '14'), ('T2', 'Test 2', '55'), ('T3', 'Test 3', '33')]), ('Captain', 'Rohit Sharma', [('T1', 'Test 1', '33'), ('T2', 'Test 2', '158'), ('T3', 'Test 3', '95')]),('No3', 'Cheteshwar Pujara', [('T1', 'Test 1', '30'), ('T2', 'Test 2', '19'), ('T3', 'Test 3', '51')])]
```

### Solution:
```
def transcript(course_details: list, student_details: list, grades: list):
	return
```

