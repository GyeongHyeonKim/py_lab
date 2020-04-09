#!/usr/bin/python


def fibo(n):
    res=0;f1=1;f2=1

    if n==0:
        return 1
    elif n==1:
        return 1


    else:

        for i in range(n-1):
            res=f1+f2
            f1=f2
            f2=res
        

    return res

num = int(input("The number of fibonacci : "))

for i in range(num):
    if i==num-1:
        print(fibo(i));
        continue

    print(fibo(i),end=",");

print("F%d = %d" % (num,fibo(num-1)))

