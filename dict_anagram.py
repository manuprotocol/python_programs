# find whether a value is a anagram or not
from collections import Counter
def find_ana(val1, val2):
    val1=bin(val1)[2:]
    val2=bin(val2)[2:]
    ans=abs(len(val1) - len(val2))

    if(len(val1) < len(val2)):
        val1=ans * '0' + val1

    else:
        val2=ans * '0' +val2

    dict_one=Counter(val1)
    dict_two=Counter(val2)

    if(dict_one['0'] == dict_two['0'] and dict_two['1'] == dict_two['1']):
        print('this is anagram')
    else:
        print('not anagram')

val1=4
val2=5
find_ana(val1, val2)

