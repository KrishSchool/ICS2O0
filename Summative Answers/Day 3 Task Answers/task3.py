#task3.py
#WORKS ONLY IN PYTHON 3.6 AND ABOVE!

def calculate_factorial(number):
    factorial = 1
    for x in range(1,number+1):
        factorial = factorial*x
    return factorial

def square(number):
    return number**2 #    ** stands for to the power of

def mode_select():
    valid_inputs=["factorial","square"]
    is_valid_input = False
    while not is_valid_input:
        try:
            input_from_user = (input('What operation do you want to do?: '))
            if input_from_user.lower() not in valid_inputs:
                raise ValueError #this will send it to the print message and back to the input option
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid choice. You can either 'factorial' or 'square' the input.")
        else:
            return input_from_user.lower()

def user_input(mode):
    is_valid_input = False
    while not is_valid_input:
        try:
            input_from_user = int(input(f'What number would you like to {mode}?: '))
            if input_from_user < 0:
                raise ValueError #this will send it to the print message and back to the input option
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid choice.")
        else:
            return input_from_user


mode=mode_select()
number = user_input(mode)
output = None
if mode=='factorial':
    output=calculate_factorial(number)
elif mode == 'square':
    output=square(number)

with open("answers.txt",'a') as file:
    file.write(f"\nThe {mode} of {number} is: {output}.")
    print(f"The {mode} of {number} is: {output}")
    file.close()
