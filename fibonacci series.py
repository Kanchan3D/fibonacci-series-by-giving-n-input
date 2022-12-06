range=int(input("how many terms"))
a,b=0,1
count,fib=0,0
while(count<range):
    print(fib)
    a=b
    b=fib
    fib=a+b
    count=count+1