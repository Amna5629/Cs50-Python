expression = input("Expression:").strip()

expression = expression.split()

if expression[1] == "+":
    Ans = int(expression[0]) + int(expression[2])
    print(float(Ans))
elif expression[1] == "-":
    Ans = int(expression[0]) - int(expression[2])
    print(float(Ans))
elif expression[1] == "/":
    Ans = int(expression[0]) / int(expression[2])
    print(float(Ans))
else:
    Ans = int(expression[0]) * int(expression[2])
    print(float(Ans))
