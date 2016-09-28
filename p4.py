import random
import zlib
import os

def randomHex(n):
    return ''.join([random.choice('0123456789ABCDEF') for x in range(n)])


def foo():
    count = 0
    vals = {}
    x = ('4C8A994704EF6E9CDA1CC7A7A83ADB3F')
    xCrc = zlib.crc32(x)
    while(1):
        count += 1
        if count%5000000 == 0:
            print str(count)+' iterations'

        y = randomHex(random.randint(1,25))
        yCrc = zlib.crc32(y)
        if yCrc == xCrc and y != x:
            print 'we have a winner! ' + y
            return

foo()
