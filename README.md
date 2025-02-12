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

## **7. Structured Data**
### **Lists**
```python
list1 = [1, 2, 3, 4, 5]
list1.append(6)  # Adds element
list1.remove(2)  # Removes element
list1.sort()  # Sorts list
list1.reverse()  # Reverses list
print(list1)
```

### **Tuples**
```python
tuple1 = (1, 2, 3, 4, 5)
print(tuple1[0])
print(tuple1.count(2))  # Counts occurrences of an element
```

### **Dictionaries**
```python
dict1 = {"name": "Python", "version": 3.9}
dict1["release"] = 1991  # Adds key-value pair
print(dict1.keys())  # Prints all keys
print(dict1.values())  # Prints all values
```

### **Sets**
```python
set1 = {1, 2, 3}
set1.add(4)
set1.remove(1)
print(set1)
```

### **List Comprehension**
```python
squares = [x**2 for x in range(5)]
print(squares)
```

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
