# my solution
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f","--foo",help="foo")
parser.add_argument("-b","--bar",help="bar")
parser.add_argument("-v","--version",help="Print program's version")
parser.parse_args()