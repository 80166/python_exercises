from datetime import datetime

import math
import os
import random
import re
import sys


def time_delta(t1, t2):
    date_time = "%a %d %b %Y %X %z" 
    date_t1 = datetime.strptime(t1, date_time)
    date_t2 = datetime.strptime(t2, date_time)
    
    return str(abs(int(date_t1.timestamp() - date_t2.timestamp())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()