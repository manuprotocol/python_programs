#Python – Extract digits from Tuple list

def find_data(test_list):
    new_list=[]
    for tup in test_list:

        for value in range(len(tup)):
            if(tup[value] not in new_list):
                new_list.append(tup[value])

    k_list=[]
    for fi in new_list:
        if(fi > 9):

            while(fi !=0):
                x=fi % 10
                k_list.append(x)
                fi=fi // 10
        else:
            k_list.append(fi)

    return k_list

test_list = [(15, 3), (3, 9)]

print(find_data(test_list))

