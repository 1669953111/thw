import argparse
parser = argparse.ArgumentParser()

parser.add_argument("filename", metavar='F', type=str, help="Enter a filename to print.")
args = parser.parse_args()

file = open(args.filename)
print(file.read())
file.close()
