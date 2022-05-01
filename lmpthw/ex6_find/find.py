import os, argparse
parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser()

parser.add_argument("path", metavar="P", type=str, help="Enter a path to find.")
parser.add_argument("filename", metavar="F", type=str, help="Enter a filename to find.")
args = parser.parse_args()

for root,dirs,files in os.walk(args.path,topdown=True):
    if args.filename in files:
        print("found it.")
        print(root)
        break
    else:
        pass
