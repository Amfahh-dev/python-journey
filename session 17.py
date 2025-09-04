def greet_user(name):
    print("Hello", name)

greet_user("Amfahh")
greet_user("Shiza")



def newmember(name):
    print("Welcome to the team", name)

    newmember("Amfahh")

    def Operations(a, b):
    print("Sum of two numbers is ", a + b)
    print("Difference of two numbers is ", a - b)
    print("Product of two numbers is ", a * b)
    if b != 0:
        print("Division of two numbers is ", a / b)
    else:
        print("Division by zero is not allowed")



Operations(10, 5)

def welcome_message(name):
    return f"Welcome to the team {name}"

def user_defined_function(names):
    messages = []
    for name in names:
        messages.append(welcome_message(name))
    return messages


team_names = ["Amfahh", "Ayesha"]
result_messages = user_defined_function(team_names)
for message in result_messages:
    print(message)
