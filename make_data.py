import os
import sys
import argparse
from string import letters
from random import randint, choice

parser = argparse.ArgumentParser(description="Create specified number of directories.")
parser.add_argument("integer", metavar="N", type=int, help="Number of directories to be created.")
parser.add_argument("--sub-dirs", help="Create sub directories, default directory.")
args = parser.parse_args()

dir_list = []

for i in range(int(sys.argv[1])):
    dir_list.append(''.join([choice(letters) for i in range(randint(5, 25))]))

def make_dirs():
    for dir_name in dir_list:
        try:
            os.mkdir(dir_name)
            print("Created directory: {}".format(dir_name))
        except OSError:
            print("The directory {} already exists.".format(dir_name))
            pass

make_dirs()

# clean up

for dir_name in dir_list:
    print("Removing directory: {}".format(dir_name))
    os.rmdir(dir_name)
