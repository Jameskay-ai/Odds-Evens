# Odds-Evens

🔢 Even or Odd Number Checker (Python Beginner Project)
This is a simple Python script that asks the user for a number and checks whether it's even or odd. It's a foundational example of input handling, type conversion, and conditional logic in Python.

🧠 Concepts Covered
Concept	Description
input()	Prompts the user for input from the terminal (as a string).
int()	Converts the input to an integer so arithmetic can be performed.
Variables	The number variable stores user input.
% Modulo Operator	Used to check for divisibility (remainder of division).
Conditional Logic	if-else is used to execute different code based on the condition.
print()	Outputs results to the terminal.

🧾 Full Code
python
Copy
Edit
number = int(input("What number would you like to check?"))

if number % 2 == 0:
    print("even")
else:
    print("odd")
🔍 How It Works
Prompt the user to enter a number using input().

Convert the user input from a string to an integer using int().

Use the modulo operator (%) to check whether the number is divisible by 2:

If the remainder is 0, it's even.

Otherwise, it's odd.

The program then prints the result accordingly.

🧪 Example Outputs
User Input	Output
12	even
7	odd
0	even
-3	odd

✅ Learning Objectives
Learn how to get user input using input()

Practice converting string input to integers

Understand and apply if, else, and % (modulo)

Use print() to output results to the console

Improve indentation and control flow understanding
