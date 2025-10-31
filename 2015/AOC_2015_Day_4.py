## AOC 2015 Day 4

import hashlib

key = 'ckczppom'
num = 1

while True:
    strng = key + str(num)
    encstr = strng.encode('utf-8')
    answer = hashlib.md5(encstr)
    hexans = str(answer.hexdigest())
    if hexans[0:6] == "000000":
        print(num)
        break
    num += 1
    

