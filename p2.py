from collections import Counter
from math import log10
import random
import operator

englishFrequency = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N':
        6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78,
        'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P':
        1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10,
        'Z': 0.07}

cipherText = 'ZLQWZFYUHVIZUREYZIYKHYUYQODFULPRQPWYNKCZSPDWCIZXBLPRQPQCHVUZZDXPXLFYQWRKCSEKHPQPWYYTLILRCIZKRCXYHYUQZDVUOIKDPRQPZAOFQUOCXTXRNEHVIZFOQUWYDSZXWVECBZZLBZSPVKULAECXIKEWMZXRWYXTOQZOTUPRQPPVROZAUWLTLQQXXYHAAZDZORDFPRQPWEEUZIXTXRKQDZWEMQUOYKIXYOBXKZNEWYUDZLQLTHSPZFRCEPWVCIZKZARLZAEDCZAUOAGIZKKQTHOYWNZRGMZIKYWYXYPQEWMZCIULEXIFXYSBEYZCRQCEEFDUPRQPQUNEZLOFZIZFILYKCTIOWVZCHMZCNKDZZXCDPRQPWYXTUOXNICKCSPZDVKQUZXTYCSDSKZEQYFZALNCNKZSPMIZOHYUQYXHVKSNEDZOKUQYCSDDZAEMVHDZKRCIKIFEKHPQPWYYKTACIHVLRWYPVKSOKTVYZYXUOONHVZIQWBIZKHVCRUZHBUOYVEWQOLDEKHMEXTVYIRNCKKZSPMIZOZYVASPSDAEOACFKDPUUPOFXPXHKYLRWYWEKQAEVDLQRCZRIFZYEIEKHPQPWYXCPIAPTVOQYKIXRKIDEKHPQPWYKCZLQPXGUOUYZIXTXRLAWYXNIKGWEKHPQPWYYTOYXTFOAECXRWWYKDWIUYCHZXHQQUZCBEPRQPWYKCZLDFPRCRKUPKIXLTCLACTQKZZXDVKZZLZOZFBIKZWEEKEQZUEKHPQPOFIFZFQZKOZXQPIDRPZIEKHPQPWYKDPRQPWEEKEQZUEKHPQPPUXLIZUOXPUXOKDVCIOKUQTVXEEXWVIKHDHVIZUOZIKUIZSKYIYFGMIZWEZOZFQZYXIZAEMVVAZPQPOCSYDZUOIYDFPRULPRQPYCZOWVHVUZLQRLBEPRQPQDHUAELTYIQWRKCSHVCRWYATWYKTUPDBQPXEYIVGUOPBYIICXIPIKIFUZYDVZXVAQAIKHDHVUIZIOMUZFIHDHVLRZUFHUZQUZUDVQDHVLOZROMOIZKBIKZHVLOZROLBEAEQZCZAWEQUYIOTHPIWEEUQIAEGIPQUOIXKYIBUZTUPRQPWYXCUOZFHVIRGWIZEKHPQPNEZLZIPUUXSPUQIDHVYIBVKIAODZVHZLQPHDZCBEPRQPZKUYHPRPIDAEEKHPQPWYXKZRZFPVKSYKQPRFIALSWSCIWICZPZYZUPIXQDZYHDZDWVIKGWWIKQDZWEDZIKCTCSHVLROYRZDZIALWIRMXUOZIZAYIZCYVUFXUOSAQIXZDRXKDPRQPHVKSHVUIOMUEIZZKFIEKEQWQCZZLXRWAZYZDWIQDRNZNWVYIZKDZQOHVIZHVWYALSKIFIXZKDZQDHVLILIIZZDWIWEPUDZHCUEOZGXUZTYKZPVIZIOZDZQUOXPUXHVIRGWIZTHSPSKZIZKMCPQULPRQPHVUIAEMVHDZKRCTVAOYFKXKZHVUZUFENTVIFHYZACVZLZOWKZOWYOMAWZOCZRZRQAOVADZZLZFQIIUOQIKZDCVZLZURLXVKYHVIOGOQAHVUIOACFKDEPZUHVIZNZIZHVPQUZPUZKRFHVIZIKHDHVUIKUSCPUUXIKHVYZPUWIBVZLRXIWBZZOQCSKQITHZIPQUQIXYIHVCRKUPOKSIZTYKZHVUIIBNZLOAZHTYIZKHVCRCIWEHVUZZBUOBLPRQPWYXNIBKOLTOYYVKUZRHYVUZRGMWYBCKRWYBDPRQPWYXIOYXLFQFIKZDECRAKBIZAIFZFQIZBLICIKZHVUZNRVHWEHVAZFIKZDECRAKBIZQAEZUZUZFQIFZXEYITHYIDCYIQXYWSCZIIKZDEUUFNOWYHDZKZCOQUOLTWICIAODFPRQPWYXTPQRLZOZKZFBZZLZLKYWEHVLRWYPVAWCSDZLAEKHPQPFYZDEXSPZFODXPFUXTXREKHPQPWYKCZLIYOACFKTEQXSXREKHPQPWYXKCSHVCRAKBILAWZIZHVFRQOZFQUKSPRQTZKIFIKZDRLDVORIFKCZLZUEUUFYIQVWERXIFZKSPMIZOTUPRQPWYXTUZOYXTLZKYHVLROAQZCZSPDVSPCKKZZLUQYXZLIWZKXFNUUFHVFOWYZCKCAPXECHZLQPWGZPUKYUCIHVCRAKBIZKRCALSCKLPRQPQCHDHVKSZLTVAECXEXOCZKHUQYMVZCBZZLPVPEIRLVYZUWRXUXWYYKXPXLYZEGOIIXUQIXZIUPZDWITUPRQPWYKCZLDGEQIXAOXVYZZPYUCIKZHVYZZULRCIZKRLZKRCRWYIBVPIWEOQEKHPQPWYXYUQYXZAZKSPMIZOTQCSZLWYVAIZCIIWSKRDZKENCKKZZUGZLILRPUEXPEUXOFXPEMNRVHEKHPQPWYXYNBAKIXZYWVEKRXUTWIQVWIHVIZEYYVIKZDOKTZLICIZKZLOQSPMIZOVQPIWIYIHVYZMCPIKIHVOZTHAUZBOYIXKZOFIFZFZRFQVHZKPUEPOAEQYITHYIDCZAENYUZDLUZKICRFIFQOZCYIZKRLZIZNIXDEZDZFIFHYTYKZDZOKUQEPWVPVXECRUERZIOEKCFNBCZSPMIZOTHKZKPUORPZILTZOTHYOWFOIOACVZLUYRDULCDPRQPQCZDUYLDLUCICIKSUPTHEKHPQPWYXTLOZRRXZUXBCZSPHVFOAECXHAOQCZZLEGOIIXUQIXZIUPZDWIUQSKXPFUZFDVTUPRQPWYNKAECXIWHTYIBFPRDEZAWVZADVZLQEYIHY'

def count_pairs(text):
    pairList = {}
    for i in range(0, len(text)-1):
        pair = text[i] + text[i+1]
        if ' ' not in pair:
            if pairList.has_key(pair):
                pairList[pair] += 1
            else:
                pairList.update({pair: 1})
    sorted_pairList = sorted(pairList.items(), key=operator.itemgetter(1))
    sorted_pairList.reverse()
    print sorted_pairList[0:20]

# returns the "extended head" of a list
def head_pair(text):
    return text[0]+text[1]

# splits text into bigraphs for easier reading
def split_text(text):
    split_text = ''
    while len(text) > 0:
        split_text+=head_pair(text)
        split_text+=' '
        text = text[2:]
    return split_text

def decryptDigraph(grid, input):
    first = input[0]
    second = input[1]

    firstPosition = grid.index(first)
    secondPosition = grid.index(second)

    firstX = firstPosition % 5
    firstY = firstPosition / 5
    secondX = secondPosition % 5
    secondY = secondPosition / 5

    if firstX == secondX:
            firstLetter = grid[(((firstY - 1) % 5) * 5) + firstX]
            secondLetter = grid[(((secondY - 1) % 5) * 5) + secondX]
    elif firstY == secondY:
            firstLetter = grid[(firstY * 5) + ((firstX - 1) % 5)]
            secondLetter = grid[(secondY * 5) + ((secondX - 1) % 5)]
    else:
            firstLetter = grid[(firstY * 5) + secondX]
            secondLetter = grid[(secondY * 5) + firstX]

    digraph = firstLetter+secondLetter
    return digraph

def decrypt_message(grid, text):
    decrypt = ''
    while len(text) > 2:
        decrypt+=decryptDigraph(grid,head_pair(text))
        text = text[2:]
    return decrypt

# compares the frequency of the english and candidate text
def frequency_score(english, candidate):
    score = 0
    for key in english.keys():
        score += abs(english[key] - candidate[key])
    return -score

def letter_frequency(text):
    length = len(text)
    letters = Counter(text)
    for key in letters.keys():
        letters[key] = round((float(letters[key])/length)*100,2)
    return letters

def shuffle_letters(string):
    return ''.join(random.sample(string,len(string)))

def swap_letters(string):
    j = random.randint(0,24)
    i = random.randint(0,24)
    strr = list(string)
    buf = strr[i]
    strr[i] = strr[j]
    strr[j] = buf
    string = ''.join(strr)
    return string

def swap_letters3(string):
    j = random.randint(0,24)
    i = random.randint(0,24)
    k = random.randint(0,24)
    strr = list(string)
    buf = strr[i]
    strr[i] = strr[j];
    strr[j] = strr[k];
    strr[k] = buf;
    string = ''.join(strr)
    return string

def swap_rows(string):
    j = random.randint(0,4)
    i = random.randint(0,4)
    strr = list(string)
    buf = strr[i]
    for k in range(0,5):
        temp = strr[i*5+k]
        strr[i*5 + k] = strr[j*5 + k];
        strr[j*5 + k] = temp;
    string = ''.join(strr)
    return string

def swap_cols(string):
    j = random.randint(0,4)
    i = random.randint(0,4)
    strr = list(string)
    buf = strr[i]
    for k in range(0,5):
        temp = strr[k*5+i]
        strr[k*5 + i] = strr[k*5 + j];
        strr[k*5 + j] = temp;
    string = ''.join(strr)
    return string

def flipTB(string):
    strr = list(string)
    temp = strr[:]
    for j in range(0,5):
        for i in range(0,5):
            temp[i + 5 * j] = strr[(4-i) + 5 * j]
    string = ''.join(temp)
    return string

def flipLR(string):
    strr = list(string)
    temp = strr[:]
    for j in range(0,5):
        for i in range(0,5):
            temp[i + 5 * j] = strr[i + 5 * (4-j)]
    string = ''.join(temp)
    return string

def flipTBLR(string):
    strr = list(string)
    temp = strr[:]
    for i in range(0,5):
        for j in range(0,5):
            temp[i + 5 * j] = strr[(4 - i)+5*(4-j)]
    string = ''.join(temp)
    return string

def changeGrid(grid):
    n = random.random()*100
    if n < 40:
        return swap_letters(grid)
    if n < 60:
        return swap_rows(grid)
    if n < 80:
        return swap_cols(grid)
    else:
        return shuffle_letters(grid)

def string_score(string, frequency, num):
    x = 0
    for i in range(len(string)-4):
        if string[i:i+4] in frequency:
            x += frequency[string[i:i+4]]
        else:
            x += log10(float(1)/num)
    return x

splitCipher = split_text(cipherText)

quadGrams = {}
for i in file('english_quadgrams.txt'):
    key, count = i.split(' ')
    quadGrams[key] = int(count)
summ = 0
for i in quadGrams.keys():
    summ += quadGrams[i]
for i in quadGrams.keys():
    quadGrams[i] = log10(float(quadGrams[i])/summ)
# grid = 'HZRTDYEPKLABVFMXNGCQOIWSU'
# grid = 'AIKVUZHTNMSDXCGRYBFWOQLPE'
# grid = 'APHRXVSCUKGQMWFEDZTOBLNIY'
# grid = 'EQDOSIXTZHPFBNUVMGKCLRYAW'
# grid = 'KQOCPBGRYTILEVMNZAHDFSWUX'
# grid = 'LRZHAQMNDKYVFEOTWPIGUBSXC'
# grid = 'LRZHAQMNDKYVFEOTWPIGUBSXC'
# grid = 'NWQBCXRUOTGHVZLSFMEKPADIY'
# grid = 'abcdefghiklmnopqrstuvwxyz'
# grid = 'gthvoxznfelrbyiucqmspkdwa'
grid = 'QBMGRSTHVZUCLFEYDXNIAKPWO'

grid = grid.upper()
grid = shuffle_letters(grid)
bestGrid = grid
print bestGrid

candidate = decrypt_message(grid, cipherText)

score = string_score(candidate, quadGrams, summ)
maxScore = score
bestScore = score
maxGrid = bestGrid
print bestScore
# candidateFrequency = letter_frequency(candidate)
# bestScore = frequency_score(englishFrequency, candidateFrequency)
while(1):
    bestGrid = maxGrid
    grid = bestGrid
    bestScore = maxScore

    for temp in range(80,1,-1):
        for count in range(0,10000):
            grid = changeGrid(bestGrid)
            candidate = decrypt_message(grid, cipherText)
            score = string_score(candidate, quadGrams, summ)
            df = score - bestScore
            if(df>=0):
                bestScore = score
                bestGrid = grid
            else:
                val = 2.71828**(df/temp)
                if (val>random.random()):
                    bestScore = score
                    bestGrid = grid
            if(bestScore > maxScore):
                maxGrid = bestGrid
                maxScore = bestScore
                print 'best so far:'
                print maxScore
                print maxGrid
                print decrypt_message(maxGrid, cipherText).lower()

    # max is the max of all iteration, best is best current
    if(bestScore > maxScore):
        maxGrid = bestGrid
        maxScore = bestScore
        print 'best so far:'
        print maxScore
        print maxGrid
        print decrypt_message(maxGrid, cipherText).lower()
