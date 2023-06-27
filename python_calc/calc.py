#add
def add(n1,n2):
  return n1 + n2
#subtarct function
def subtract(n1,n2):
  return n1 - n2
#multiply function
def multiply(n1,n2):
  return n1 * n2
#divide function
def divide(n1,n2):
  return n1 / n2

#creating a dictionary
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

num1 = int(input("whats the first number? "))
num2 = int(input("whats the second number? "))
for symbol in operations:
  print(symbol)

operation_symbol = input("pick an operation from the line above: ")
calculator_function = operations[operation_symbol]
answer = calculator_function(num1,num2) # THIS LINE OF CODE SIMPLY MAKES THE calculator_function varaible, a placeholder for whatever function will be called by the user input.
print(f"{num1} {operation_symbol} {num2} = {answer}")