# this program belongs to pickling iris program

import pickle

# data_set=[[5.1,3.5,1.4,0.2,'Iris-setosa'], [4.9,3.0,1.4,0.2,'Iris-setosa']]

# f=open("manu_iris.pkl", 'wb')
# data=pickle.dump(data_set,f)
# f.close()

#f=open('manu_iris.pkl', 'rb')
#data1=pickle.load(f)
#print(data1)

f=open('iris.data', 'r')
data_set=f.read()
#data_set.splitlines("\n")
red=[[i] for i in data_set]
#print(red)
f.close()
file='manu_iris.pkl'
f=open(file, 'wb')
data1=pickle.dump(red, f)
f.close()

new_list=[]
f=open(file, 'rb')
data_read=pickle.load(f)
for i in data_read:
    new_list.extend(i)
#print("".join(new_list))
f.close()

















