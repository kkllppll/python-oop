import argparse

parser = argparse.ArgumentParser(description='To calculate math result enter number operation number')
parser.add_argument('num1', type=int, help='first number')
parser.add_argument('oprtn', type=str, help = "operation")  
parser.add_argument('num2', type=int, help='second number')

args = parser.parse_args()

def task(num1, oprtn, num2):
    try:
        return eval(f'{num1} {oprtn} {num2}')
    except (ZeroDivisionError):
        print("Can't divide by zero")


print(task(args.num1, args.oprtn, args.num2))
