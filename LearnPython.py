print("Calculator")
numOne = int(input("Enter first number: "))
numTwo = int(input("Enter second number: "))
calcSymbol = input("Enter +, -, *, or /: ")

if calcSymbol == '+':
    print("The sum of", numOne, "and", numTwo, "is:", numOne + numTwo)
elif calcSymbol == '-':
    print(numOne, "minus", numTwo, "is:", numOne - numTwo)
elif calcSymbol == '*':
    print(numOne, "multiplied by", numTwo, "is:", numOne * numTwo)
else:
    print(numOne, "divided by", numTwo, "is:", numOne / numTwo)
