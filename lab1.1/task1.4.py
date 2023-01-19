import argparse
from itertools import chain, combinations


parser = argparse.ArgumentParser(description=('Capacity of a knapsack'))
parser.add_argument('-W', '--capacity', type=int, help = "bag`s capacity")
parser.add_argument('-w', '--weights', type=int, nargs='+', help = "each gold bar weight") 
parser.add_argument('-n', '--bars_number', type=int, help = "number of bars")
args = parser.parse_args()


def countcapacity(weights):
    weightslist = list(weights)
    return chain.from_iterable(combinations(weightslist, r) for r in range(len(weightslist)+1))


def knapsack_task(W, w, n):
    if args.bars_number == len(args.weights):
        max_weight = int()
        for x in countcapacity(args.weights):
            if (sum(x) > max_weight) and (sum(x) <= args.capacity):
                max_weight = sum(x)
            else:
                continue
        print("Max weight:", max_weight)
    else:
        print("Bars cnumber does not match entered list of weights.")



print(knapsack_task(args.capacity, args.weights, args.bars_number))