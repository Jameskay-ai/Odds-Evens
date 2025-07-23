🔢 Even or Odd Checker (Python)
This simple Python script checks whether a given number is even or odd. It demonstrates basic but essential programming concepts such as user input, type casting, conditional logic, and modulo arithmetic.

🧾 Full Code
python
Copy
Edit
number = int(input("What number would you like to check?"))

if number % 2 == 0:
    print("even")
else:
    print("odd")
🧠 Key Concepts Explained
Concept	Description
input()	Gets user input as a string from the terminal.
int()	Converts the input string into an integer.
Variables	number stores the integer value entered by the user.
% Modulo Operator	Returns the remainder of the division (number % 2).
if-else Conditional	Makes a decision based on whether the number is even or odd.
print()	Outputs the result to the console.
Type Casting	Converts one data type to another (str → int).
Control Flow	Uses conditions to control program execution.

🔍 Step-by-Step Breakdown
Line	Explanation
number = int(input(...))	Prompts the user for a number, converts it to an integer, and stores it in number.
if number % 2 == 0:	Checks if the number is divisible by 2 with no remainder.
print("even")	Runs if the number is divisible by 2. Prints even.
else:	Runs if the condition is false (number is not divisible by 2).
print("odd")	Executes and prints odd.

🧪 Example Runs
User Input	Internal number	Output
4	4	even
7	7	odd
0	0	even
-5	-5	odd

✅ What You Learn
How to get user input in Python

How to convert data types (string to integer)

How to apply conditional logic using if-else

How to use the modulo operator

Understanding code structure and indentation
