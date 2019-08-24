#!/bin/python3

import math
import os
import random
import string 
import re
import sys

'''
INPUT
1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
abc
OUTPUT
9
https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
'''

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    my_dict={}
    s = list()
    test_list = list(string.ascii_lowercase)
    for (a, b) in zip(test_list, h): 
        my_dict[a] = b
    for key,val in my_dict.items():
        if key in word:
            s.append(val)
    m = max(s)
    l = len(word)
    return m*l


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
