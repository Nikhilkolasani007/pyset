# Python Study Guide for Exam Preparation

## **1. Introduction**
### **Python Overview**
- Python is a high-level, interpreted programming language known for its simplicity and readability.
- Used in web development, data science, automation, AI, and more.
- Supports multiple programming paradigms (Procedural, Object-Oriented, Functional).

### **Python Applications**
- Web Development: Django, Flask
- Data Science: Pandas, NumPy, Scikit-learn
- Automation: Scripting, Selenium
- Machine Learning & AI: TensorFlow, PyTorch
- Cybersecurity: Ethical Hacking, Forensics

## **2. Installation**
### **Installing Python**
1. Download from [python.org](https://www.python.org/downloads/)
2. Install and check using:
   ```bash
   python --version
   ```
3. Install IDEs like PyCharm, VS Code, or Jupyter Notebook.

## **3. Language Overview**
### **Coding Practices**
- Follow PEP 8 for styling.
- Use meaningful variable names.
- Keep functions small and modular.

### **Hello World Program**
```python
print("Hello, World!")
```

### **Statements and Expressions**
- Statements perform actions.
- Expressions evaluate to values.

### **Whitespace and Comments**
```python
# This is a comment
print("Python uses indentation for blocks")
```

### **Using `print()`**
```python
print("This is a message")
print("Value of x:", x)
```

### **Block and Scope**
- Indentation defines blocks.
- Variables inside functions have local scope.

## **4. Types and Values**
### **Overview**
- Dynamic typing, no need to declare types explicitly.

### **Common Data Types**
```python
string_var = "Hello"
int_var = 10
float_var = 10.5
bool_var = True
list_var = [1, 2, 3]
tuple_var = (1, 2, 3)
dict_var = {"name": "Python"}
set_var = {1, 2, 3}
```

### **`type()` and `id()`**
```python
print(type(string_var))  # Returns type of variable
print(id(string_var))    # Returns memory location
```

## **5. Operators**
### **Arithmetic Operators**
```python
x = 10
y = 3
print(x + y, x - y, x * y, x / y, x % y, x ** y, x // y)
```

### **Bitwise Operators**
```python
print(x & y, x | y, x ^ y, ~x, x << 2, x >> 2)
```

### **Boolean Operators**
```python
print(True and False, True or False, not True)
```

### **Operator Precedence**
1. `()`
2. `**`
3. `*`, `/`, `%`, `//`
4. `+`, `-`
5. `>`, `<`, `==`, `!=`

## **6. Flow Control**
### **Conditional Statements**
```python
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is 5")
else:
    print("x is less than 5")
```

### **Loops**
#### **While Loop**
```python
x = 0
while x < 5:
    print(x)
    x += 1
```

#### **For Loop**
```python
for i in range(5):
    print(i)
```

#### **Additional Controls**
```python
for i in range(10):
    if i == 5:
        break  # Exits loop
    if i % 2 == 0:
        continue  # Skips even numbers
    print(i)

```

Here are the **most important** and commonly used **list, tuple, dictionary, and set operations** in Python.  

---

## **1. List Operations (`list`)**  
Mutable (can be changed), ordered, allows duplicates.  

```python
# Creation
lst = [1, 2, 3, 4, 5]

# Adding elements
lst.append(6)         # [1, 2, 3, 4, 5, 6]
lst.insert(2, 10)     # [1, 2, 10, 3, 4, 5, 6]
lst.extend([7, 8])    # [1, 2, 10, 3, 4, 5, 6, 7, 8]

# Removing elements
lst.remove(10)        # Removes first occurrence of 10
popped = lst.pop()    # Removes last element and returns it
del lst[1]            # Deletes element at index 1

# Accessing elements
print(lst[0])         # First element
print(lst[-1])        # Last element
print(lst[1:4])       # Slicing [start:end]

# Searching
print(lst.index(3))   # Get index of first occurrence of 3
print(4 in lst)       # True if 4 exists in the list

# Sorting and reversing
lst.sort()            # Sorts in ascending order
lst.reverse()         # Reverses list

# Copying
lst_copy = lst.copy() # Creates a copy of the list

# Length
print(len(lst))       # Returns number of elements
```

---

## **2. Tuple Operations (`tuple`)**  
Immutable (cannot be changed), ordered, allows duplicates.  

```python
# Creation
tpl = (1, 2, 3, 4, 5)

# Accessing elements
print(tpl[0])         # First element
print(tpl[-1])        # Last element
print(tpl[1:4])       # Slicing

# Searching
print(tpl.index(3))   # Get index of first occurrence of 3
print(4 in tpl)       # True if 4 exists in the tuple

# Counting elements
print(tpl.count(2))   # Counts occurrences of 2

# Length
print(len(tpl))       # Returns number of elements

# Tuple unpacking
a, b, c, d, e = tpl   # Assign values to variables
print(a, b, c)        # 1, 2, 3

# Converting to list (since tuple is immutable)
tpl_list = list(tpl)  # Convert tuple to list
```

---

## **3. Dictionary Operations (`dict`)**  
Key-value pairs, mutable, unordered (Python 3.6+ maintains insertion order).  

```python
# Creation
dct = {"name": "Alice", "age": 25, "city": "New York"}

# Accessing values
print(dct["name"])        # Alice
print(dct.get("age"))     # 25 (preferred, avoids errors)

# Adding/updating values
dct["age"] = 26           # Update value
dct["gender"] = "Female"  # Add new key-value pair

# Removing elements
dct.pop("city")           # Removes and returns value
del dct["age"]            # Deletes key
dct.clear()               # Clears dictionary

# Checking existence
print("name" in dct)      # True if key exists

# Getting keys, values, items
print(dct.keys())         # dict_keys(['name', 'gender'])
print(dct.values())       # dict_values(['Alice', 'Female'])
print(dct.items())        # dict_items([('name', 'Alice'), ('gender', 'Female')])

# Iterating through dictionary
for key, value in dct.items():
    print(key, value)

# Copying
dct_copy = dct.copy()

# Length
print(len(dct))           # Number of key-value pairs
```

---

## **4. Set Operations (`set`)**  
Unordered, mutable, **unique** elements (no duplicates).  

```python
# Creation
st = {1, 2, 3, 4, 5}
st2 = {4, 5, 6, 7}

# Adding elements
st.add(6)           # {1, 2, 3, 4, 5, 6}
st.update([7, 8])   # {1, 2, 3, 4, 5, 6, 7, 8}

# Removing elements
st.remove(2)        # Removes 2, error if not found
st.discard(3)       # Removes 3, no error if not found
st.pop()            # Removes a random element
st.clear()          # Clears set

# Set operations
union = st | st2            # Union (all elements)
intersection = st & st2      # Intersection (common elements)
difference = st - st2        # Difference (elements in st but not in st2)
symmetric_diff = st ^ st2    # Symmetric difference (not in both)

# Checking existence
print(4 in st)       # True if 4 exists

# Length
print(len(st))       # Number of elements
```

---

### **🔥 Summary (Most Used Operations)**
| **Type**  | **Common Operations** |
|-----------|----------------------|
| **List**  | `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`, `index()`, `copy()` |
| **Tuple** | `index()`, `count()`, `len()`, `unpacking`, `conversion to list` |
| **Dictionary** | `get()`, `keys()`, `values()`, `items()`, `update()`, `pop()`, `copy()` |
| **Set** | `add()`, `remove()`, `union()`, `intersection()`, `difference()`, `symmetric_difference()` |


Here’s a **complete A to Z operations list** for **Lists, Tuples, Sets, Dictionaries, and Strings** in Python! 🚀  

---

### **A to Z Operations for Python Data Structures**  

---

## **1️⃣ List Operations (Mutable, Ordered, Allows Duplicates)**  
- **A**ppend → `list.append(item)`  
- **B**ackward Indexing → `list[-1]`  
- **C**ount → `list.count(value)`  
- **D**elete (Remove item) → `del list[index]`  
- **E**xtend (Concatenate lists) → `list.extend(iterable)`  
- **F**ilter → `[x for x in list if condition]`  
- **G**et Item (Indexing) → `list[index]`  
- **H**ead (First n elements) → `list[:n]`  
- **I**ndex → `list.index(value)`  
- **J**oin (Convert list to string) → `''.join(map(str, list))`  
- **K**ey Extraction (For list of dicts) → `[d['key'] for d in list]`  
- **L**ength → `len(list)`  
- **M**ap → `list(map(func, list))`  
- **N**ested Lists → `list_of_lists = [[1, 2], [3, 4]]`  
- **O**rdered Iteration → `for i in list: print(i)`  
- **P**op (Remove last or index) → `list.pop(index)`  
- **Q**uick Sort (Custom sorting) → `sorted(list, key=lambda x: x)`  
- **R**everse → `list.reverse()`  
- **S**ort → `list.sort()`  
- **T**ransform (List Comprehension) → `[x*2 for x in list]`  
- **U**nique Elements (Convert to set) → `list(set(list))`  
- **V**alue Replacement → `list[index] = new_value`  
- **W**hile Loop Iteration → `while list: list.pop()`  
- **X**tend with Unpacking → `new_list = [*list1, *list2]`  
- **Y**ield Elements (Generator) → `(x for x in list)`  
- **Z**ip Lists → `zip(list1, list2)`  

---

## **2️⃣ Tuple Operations (Immutable, Ordered, Allows Duplicates)**  
- **A**ccess Element → `tuple[index]`  
- **B**oolean Check → `bool(tuple)`  
- **C**ount Occurrences → `tuple.count(value)`  
- **D**estructuring → `a, b, c = tuple`  
- **E**numerate → `for i, v in enumerate(tuple): print(i, v)`  
- **F**ind Index → `tuple.index(value)`  
- **G**et Length → `len(tuple)`  
- **H**ashable (Used as Key) → `hash(tuple)`  
- **I**mmutability Check → `tuple[0] = new_value  # Error`  
- **J**oin (Concatenate Tuples) → `tuple1 + tuple2`  
- **K**ey-Value Tuple Extraction → `dict(tuple_list)`  
- **L**oop Iteration → `for i in tuple: print(i)`  
- **M**ultiply (Repeat Elements) → `tuple * n`  
- **N**esting → `nested_tuple = ((1, 2), (3, 4))`  
- **O**rdered Elements → `sorted(tuple)`  
- **P**acking → `packed_tuple = 1, 2, 3`  
- **Q**uick Unpacking → `a, *b = tuple`  
- **R**ange with Tuple → `tuple(range(n))`  
- **S**licing → `tuple[start:end]`  
- **T**uple to List Conversion → `list(tuple)`  
- **U**nique Elements (Set Conversion) → `set(tuple)`  
- **V**alue Extraction (Indexing) → `tuple[index]`  
- **W**rap Tuple in List → `[tuple]`  
- **X**tend via Concatenation → `tuple += (new_value,)`  
- **Y**ield Tuple Elements (Generator) → `(x for x in tuple)`  
- **Z**ip with Another Tuple → `zip(tuple1, tuple2)`  

---

## **3️⃣ Set Operations (Mutable, Unordered, No Duplicates)**  
- **A**dd Element → `set.add(value)`  
- **B**oolean Check → `bool(set)`  
- **C**opy → `set.copy()`  
- **D**ifference → `set1 - set2`  
- **E**mpty Set → `set()`  
- **F**reeze (Immutable) → `frozenset(set)`  
- **G**et Length → `len(set)`  
- **H**as Element → `value in set`  
- **I**ntersection → `set1 & set2`  
- **J**oin with Another Set → `set1 | set2`  
- **K**ey Removal → `set.discard(value)`  
- **L**oop Over Set → `for i in set: print(i)`  
- **M**ath Operations (Union, Diff, Intersect) → `set1.union(set2)`  
- **N**on-Ordered Elements → `set`  
- **O**rdered Set (Sorted) → `sorted(set)`  
- **P**op Element → `set.pop()`  
- **Q**uick Membership Test → `value in set`  
- **R**emove Element → `set.remove(value)`  
- **S**ubset Check → `set1.issubset(set2)`  
- **T**o List Conversion → `list(set)`  
- **U**pdate (Union with Another Set) → `set.update(set2)`  
- **V**erify Superset → `set1.issuperset(set2)`  
- **W**ipe Set → `set.clear()`  
- **X**or (Symmetric Difference) → `set1 ^ set2`  
- **Y**ield Unique Values (Generator) → `(x for x in set)`  
- **Z**ip for Set Comprehension → `{x for x in zip(set1, set2)}`  

---

## **4️⃣ Dictionary Operations (Key-Value, Mutable, Unordered)**  
- **A**ccess Value → `dict[key]`  
- **B**oolean Check → `bool(dict)`  
- **C**opy Dictionary → `dict.copy()`  
- **D**elete Key → `del dict[key]`  
- **E**numerate Key-Value → `for k, v in dict.items()`  
- **F**etch Value Safely → `dict.get(key, default)`  
- **G**et All Keys → `dict.keys()`  
- **H**as Key → `key in dict`  
- **I**terate Over Keys → `for key in dict:`  
- **J**oin Two Dicts → `{**dict1, **dict2}`  
- **K**ey Extraction → `list(dict.keys())`  
- **L**ength of Dict → `len(dict)`  
- **M**erge Dictionaries → `dict1.update(dict2)`  
- **N**ested Dict → `{ "outer": { "inner": "value" } }`  
- **O**verwrite Value → `dict[key] = new_value`  
- **P**op Key → `dict.pop(key)`  
- **Q**uick Default Value → `dict.setdefault(key, default)`  
- **R**emove Key-Value → `dict.popitem()`  
- **S**ort Dict by Key → `sorted(dict.items())`  
- **T**o List Conversion → `list(dict.items())`  
- **U**nique Keys (No Duplicates) → `set(dict.keys())`  
- **V**alue Extraction → `dict.values()`  
- **W**ipe Dictionary → `dict.clear()`  
- **X**tract Subdict → `{k: dict[k] for k in keys}`  
- **Y**ield Key-Value Pairs → `((k, v) for k, v in dict.items())`  
- **Z**ip into Dictionary → `dict(zip(keys, values))`  

---

## **8. Strings**
### **String Operations**
```python
s = "Hello Python"
print(s.upper())
print(s.lower())
print(s.replace("Python", "World"))
print(s.split())
print("-".join(["Hello", "World"]))
```

### **Escape Sequences**
```python
print("Hello\nWorld")  # Newline
```

### **Formatting Strings**
```python
name = "Python"
age = 30
print(f"{name} is {age} years old")
```

### **String Alignment**
```python
print("{:<10} {:^10} {:>10}".format("Left", "Center", "Right"))
```

# Python Basics - Practice Questions

## Set 1 - Fundamental Python Programs

1) **Write a Python program that accepts your date of birth as a parameter and prints your age.**

2) **Write a program using the for loop to print all the prime numbers less than 100. Rewrite the same program using a while loop.**

3) **Write a program that checks if a given number is positive, negative, or zero.**

4) **Create a program that takes a sentence as input and counts the number of words in it.**

5) **Create a loop that prints the first 10 even numbers.**

6) **Implement a program that swaps the values of two variables.**

7) **Create a program that takes a temperature in Celsius and converts it into Fahrenheit.**

8) **Implement a program that converts a given number of minutes into hours and minutes.**

9) **Write a Python program that compares three different integers and finds the biggest of them.**

10) **Given the following list with values and keys, write a program to convert it into the form of a list of dictionaries with key-value pairs, sort on id, and print.**  
   **Input:** `input_list = ["'morning", 1, "evening", 3, "afternoon", 2]`  
   **Key List:** `key_list = ["phase", "id"]`

11) **Write a program that finds the common elements between two lists and stores them in a new list.**  
   **Input:** `[1,2,3,4,5] , [1,5,6,7,8]`  
   **Output:** `[1,5]`

12) **Write a program that checks if a given list is sorted in ascending order or not.**  
   **Input:** `[-10,2,5,6,8,90]`  
   **Output:** `'Yes, the list is sorted in ascending order'`

13) **Write a Python program to count the occurrences of each element in a list.**  
   **Input:** `[1,3,4,1,1,1,3]`  
   **Output:**  
   `Count of 1 is 4`  
   `Count of 3 is 2`  
   `Count of 4 is 1`

14) **Write a program to concatenate two given lists into a single list.**  
   **Input:** `[1,2,3], [5,6,7]`  
   **Output:** `[1,2,3,5,6,7]`

15) **Write a program that finds the largest and smallest elements in a list.**

16) **Create a program that checks if two sets have any elements in common.**

17) **Write a Python program that counts the number of occurrences of each character in a given string using a dictionary.**

18) **Create two sets and write a program to find the union, intersection, and difference between them.**

19) **Implement a function that removes a key-value pair from a dictionary.**

20) **Write a program that takes two lists and creates a dictionary based on the number of occurrences.**  
   **Input:** `[4, 6, 8, 9]`, `[4, 6, 6, 5, 8, 10, 4, 9, 8, 10, 1]`  
   **Output:** `{4: 2, 6: 2, 8: 2, 9: 1}`  
   **Explanation:** `4 occurs 2 times, 6 occurs 2 times in the second list, and so on.`

21) **Split the string "Solar System, Earth, India" into individual words and print each word in a new line.**

22) **Write a program to reverse the order of words in a sentence.**  
   **Input:** `Learning Python is Very Easy`  
   **Output:** `Easy Very is Python Learning`

23) **Write a program to reverse the internal content of each word.**  
   **Input:** `Learning Python is Very Easy`  
   **Output:** `gninraeL nohtyP si yreV ysaE`

24) **Write a program that generates an output where if there is a digit after a character, it converts the digit into the number of occurrences of the preceding character.**  
   **Input:** `a4b3c2`  
   **Output:** `aaaabbbcc`

25) **Write a program to find the number of occurrences of each character present in the given string.**  
   **Input:** `ABCABCABBCDE`  
   **Output:** `A-3, B-4, C-3, D-1, E-1`

---

This README provides a list of fundamental Python practice questions to improve programming skills. Each question covers different concepts, including loops, conditionals, functions, lists, dictionaries, sets, and string manipulation. Happy Coding! 🚀
