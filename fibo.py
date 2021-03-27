# this program belongs to fobonacci series


num=int(input("enter number: "))
a=0
b=1
count=0
if(num == 1 or num == 0):
    print('inserted value is 0 or 1')
else:
    while(1):
        c=a+b
        if(c == num):
            count=count+1
            break
        elif(c > num):

            break

        else:
            a=b
            b=c

    if(count > 0):
        print('found')
    else:
        print('not found')
