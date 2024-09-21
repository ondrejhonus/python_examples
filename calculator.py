def calculate(num1, operator, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        print("Invalid example!")
        return
    print(f"{num1} {operator} {num2} = {result}")

try_again = 'y'
while try_again.lower() == 'y' or try_again == '':
    user_input = input("Please type a math example (12 + 48).\nAllowed characters: '+', '-', '*', '/'.\n")
    for char in '+-*/':
        if char in user_input:
            parts = user_input.split(char)
            try:
                num1 = int(parts[0].strip())
                operator = char
                num2 = int(parts[1].strip())
                calculate(num1, operator, num2)
            except:
                print("Invalid input format.")
    try_again = input("You want to calculate more? [Y/n]\n")
