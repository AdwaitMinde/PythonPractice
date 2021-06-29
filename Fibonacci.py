'''Display fibonacci series until n terms'''
n=int(input("Enter an integer: "))
a=0
b=1
if n==1:
    print(a)
if n==2:
    print(a,b)
else:
    print(a,b,end=" ")
    for i in range(0,n-2):
        fib=a+b
        print(fib,end=" ")
        a=b
        b=fib

'''output:
Enter an integer: 7
0 1 1 2 3 5 8 '''