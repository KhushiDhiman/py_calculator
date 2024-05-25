from art import logo
print(logo)


#ADD
def add(n1 , n2):
    return n1+n2
#Subtract
def sub(n1,n2):
    return n1-n2
#Multiply
def mul(n1,n2):
    return n1*n2
#Divide
def div(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}
def calculator():
    num1 = float(input("What's the first number? :"))
    for operator in operations:
        print(operator)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number? :"))
        function = operations[operation_symbol]
        answer =function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        result = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation: ")
        if result == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
