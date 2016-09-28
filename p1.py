from collections import Counter
import random
import operator

hashText = 'GVULAVFLUZGLVZQLBBTCHQRZRJICAVVQGVZQLBBTFJIZVKULLFZVKZGJAMQLBBTTINTQTPBTNVLWMGVZRJILWTPLZZHBLATQLLINLMMGVCAVVQGVZQFHIXQFLZVMLGJZMGJXGZTINFVXZQLBBTTINWTJFVNCKTFTAXVZPTQVMLBVVMMGVMLPZLWGJZZGLVZNLMGVULHFNTFUTKZQLBVMLZQGLLFMGHZQLBBTXLLNGHBLAVNFKTINFTHXGJIXNLMGVUTZTFUTKZJIXLLNGVTFMGQLBBTIVOVAZJQRQLBBTGTNTIVYQVFFVIMQLIZMJMHMJLITINMLLRQTAVLWJMNLMQATUWLANMTHXGMBTIIVAZTWVTMHAVLWCTQRULLNZVNHQTMJLIMLUGJQGNLAZVKGTNILMTZPJAVNNLMQATUWLANGTNNLHCMFVZZJIMALNHQVNJMTZTAVWJIVBVIMUGJQGULHFNPHMMLZGTBVMGVGHBCFVVWWLAMZLWGJZPAVNVQVZZLA'

i = 0

def count_pairs(text):
    pairList = {}
    for i in range(0, len(text)-1):
        pair = text[i] + text[i+1]
        if pairList.has_key(pair):
            pairList[pair] += 1
        else:
            pairList.update({pair: 1})
    sorted_pairList = sorted(pairList.items(), key=operator.itemgetter(1))
    sorted_pairList.reverse()
    print sorted_pairList[0:20]

def count_triples(text):
    pairList = {}
    for i in range(0, len(text)-2):
        pair = text[i] + text[i+1] + text[i+2]
        if pairList.has_key(pair):
            pairList[pair] += 1
        else:
            pairList.update({pair: 1})
    sorted_pairList = sorted(pairList.items(), key=operator.itemgetter(1))
    sorted_pairList.reverse()
    print sorted_pairList[0:20]

def count_quads(text):
    pairList = {}
    for i in range(0, len(text)-3):
        pair = text[i] + text[i+1] + text[i+2] + text[i+3]
        if pairList.has_key(pair):
            pairList[pair] += 1
        else:
            pairList.update({pair: 1})
    sorted_pairList = sorted(pairList.items(), key=operator.itemgetter(1))
    sorted_pairList.reverse()
    print sorted_pairList[0:10]

def count_quints(text):
    pairList = {}
    for i in range(0, len(text)-4):
        pair = text[i] + text[i+1] + text[i+2] + text[i+3] + text[i+4]
        if pairList.has_key(pair):
            pairList[pair] += 1
        else:
            pairList.update({pair: 1})
    sorted_pairList = sorted(pairList.items(), key=operator.itemgetter(1))
    sorted_pairList.reverse()
    print sorted_pairList[0:10]

def count_sext(text):
    pairList = {}
    for i in range(0, len(text)-5):
        pair = text[i]
        for j in range(1, 6):
            pair = pair + text[i+j]
        if pairList.has_key(pair):
            pairList[pair] += 1
        else:
            pairList.update({pair: 1})
    sorted_pairList = sorted(pairList.items(), key=operator.itemgetter(1))
    sorted_pairList.reverse()
    print sorted_pairList[0:10]

count_pairs(hashText)
count_triples(hashText)
count_quads(hashText)
count_quints(hashText)
count_sext(hashText)
