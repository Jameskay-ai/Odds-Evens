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
number = int(input("What number would you like to check?"))	Prompts the user for a number, converts the input from a string to an integer, and stores it in the variable number.
if number % 2 == 0:	Uses the modulo operator % to check if the number is divisible by 2. If the remainder is 0, the number is even.
print("even")	If the condition is true, this line executes and prints "even".
else:	If the condition is not true, this block runs. That means the number is odd.
print("odd")	Prints "odd" when the number is not divisible by 2.

🧪 Example Runs
User Input	Internal Value of number	Output
4	4	even
7	7	odd
0	0	even
-5	-5	odd

✅ What This Teaches
How to get user input in Python

Type conversion from string to integer

Use of conditional logic with if-else

Basic arithmetic with modulo operator

Proper indentation and control structure in Python

📘 Real-World Applications
Detecting even/odd IDs

Alternating logic in games or automation

Basic input validation logic
