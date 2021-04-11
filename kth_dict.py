#K’th Non-repeating Character in Python using List Comprehension and OrderedDict
# from collections import Counter
# def find_incre(data_str, k):
#     count=0
#     dict_set=Counter(data_str)
#     print(dict_set)
#     count = 0
#     for key, value in dict_set.items():
#         if(value == 1 and count !=k):
#             count=count+1
#     return key
#
#
# data_str = 'geeksforgeeks'
# k=3
# print(find_incre(data_str, k))

# second way
from collections import OrderedDict

def find_dict(data_str, k):
    new_dict=OrderedDict.fromkeys(data_str, 0)

    for ch in data_str:
        new_dict[ch] = new_dict[ch] + 1

    # for key, value in new_dict.items():
    #     if(value == 1):
    #         l_list.append(key)
    #         count=count+1

    l_list=[ key for key, value in new_dict.items() if (value == 1)]

    if(len(l_list) < k):
        print('no such element')
    return l_list[k-1]

data_str = 'geeksforgeeks'
k=1
print(find_dict(data_str, k))

