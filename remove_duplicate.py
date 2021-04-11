# remove all the duplicate words from the given string
from collections import Counter
def find_dupli(my_str):
    new_list=my_str.split()
    print(type(new_list))
    k_list=[]
    #for i in range(0, len(new_list)):
     #   new_list[i]= "".join(new_list[i])

    new_list=Counter(new_list)
    print(new_list)

    s = " ".join(new_list.keys())
    return s
    # for i in range(len(new_list)):
    #     if(new_list[i] not in k_list):
    #         k_list.append(new_list[i])
    #
    # return k_list

my_str='Geeks for Geeks'
print(find_dupli(my_str))


