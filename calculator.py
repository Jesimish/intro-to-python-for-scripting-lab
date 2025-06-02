x = float(input("enter your first number: "))
operator = input("input an operator (= - * /): ")
y = float(input("enter your second number: "))

if operator == "+":
    result = x + y
    print(round(result, 4))
elif operator == "-":
    result = x - y
    print(round(result, 4))
elif operator == "*":
    result = x * y
    print(round(result, 4))
elif operator == "/":
    result = x / y
    print(round(result, 4))
else:
    print("oops! Thats not a valid function! Please try again")