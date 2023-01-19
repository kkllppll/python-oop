import argparse
import operator

parser = argparse.ArgumentParser(description='To calculate math result. enter number operation number')
parser.add_argument('oprtn', type=str, help = "operation")
parser.add_argument('num1', type=int, help='first number')
parser.add_argument('num2', type=int, help='second number')
 

args = parser.parse_args()

def task(num1, num2, oprtn):
    oper = getattr(operator, args.oprtn)
    return oper(args.num1, args.num2)

print(task(args.num1, args.oprtn, args.num2,))