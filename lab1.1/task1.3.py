import argparse

parser = argparse.ArgumentParser(description='Put a string here ')
parser.add_argument('user_input', type=str, help = "users input") 
args = parser.parse_args()

def task(user_input):
        if user_input[0].isdigit() and user_input[-1].isdigit() and  user_input.replace('-', '').replace('+', '').isdigit():

            return "True", eval(user_input)
    
        else:
            return "False, None"


print(task(args.user_input))

    