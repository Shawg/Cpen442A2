import random
import zlib
import os

def randomHex(n):
    return ''.join([random.choice('0123456789ABCDEF') for x in range(n)])


def foo():
    count = 0
    vals = {}
    x = randomHex(random.randint(6,20))
    xCrc = zlib.crc32(x)
    vals[x] = xCrc
    while(1):
        count += 1
        if count%50000 == 0:
            print str(count)+' iterations'
            print 'number of entries: ' + str(len(vals))

        x = randomHex(random.randint(6,20))
        xCrc = zlib.crc32(x)

        if x in vals.keys():
            print 'double :('
        else:
            if xCrc in vals.values():
                print 'we got a value!'
                for i in vals.keys():
                    if vals[i] == xCrc:
                        print 'x: '+x
                        print 'y: '+i
                        print str(count)+' iterations'
                        return
            else:
                vals[x] = xCrc

foo()
