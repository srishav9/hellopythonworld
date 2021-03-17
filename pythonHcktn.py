#!/bin/python3
import math
import os
import random
import re
import sys
import json
import urllib.request
import urllib.parse
# Complete the 'avgRotorSpeed' function below.
# --URL--status={statusQuery}&page={number}
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING statusQuery
#  2. INTEGER parentId
def avgRotorSpeed(statusQuery, parentId):
    url = "---------------URL----------------"
    url += urllib.parse.urlencode({"status":statusQuery,"page":parentId})
    data = urllib.request.urlopen(url).read().decode()
    data = data.get("data")
    x = 0
    c = 0
    for data_dict in data:
        parent = data_dict.get('parent')
        if parent is not None and parent.get('id') == 2:
            x += data_dict.get('operatingParams').get('rotorSpeed')
            c+= 1
    try:
        return x//c
    except:
        return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    statusQuery = input()

    parentId = int(input().strip())

    result = avgRotorSpeed(statusQuery, parentId)

    fptr.write(str(result) + '\n')

    fptr.close()
