def prime(r):
    ctr=0
    a=[]
    for i in range(2,r):
        for j in range(1,i):
            if(i%j==0):
                ctr+=1
        if(ctr==1):
            a.append(i)
        ctr=0
    return(a)
a=int(input("Enter range of prime number-"))
o=prime(a)
print(o)
print("Total number of prime numbers in given range is-",len(o))
    