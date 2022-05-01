import argparse

parser = argparse.ArgumentParser()
parser.add_argument("interger", type=str, help="Enter a interger to print")
parser.add_argument("-f", help="foo")
parser.add_argument("-b", help="bar")

args = parser.parse_args()

print(args)
