""" ex_5_3.py
This module contains an entry point that:

- creates a CLi that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation 1
- writes the file to the output file argument
"""
import numpy as np
import argparse
from argparse import ArgumentParser

if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename arguments from the command line
    # Rewrite your 5_3 logic here so that it utilizes the arguments passed from the command line.

    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)
    object5 = ArgumentParser(description="This program applies a standard scale transform to the data in infile and writes it to outfile")
    object5.add_argument("infile", type=argparse.FileType('r'))
    object5.add_argument("outfile", type=argparse.FileType('w'))
    args_p = object5.parse_args()
    data = np.loadtxt("input_data.txt")
    mv = np.mean(data)
    mv1 = data - mv
    std1 = np.std(mv1)
    prcd = mv1 / std1
    np.savetxt(object5.outfile, prcd,fmt='%.2e')
