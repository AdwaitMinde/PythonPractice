#Some patterns using python
#1)
h="#"
n=int(input("Enter an integer: "))
for i in range(0,n):
    print(h)
    h=h+"#"

'''output:
Enter an integer: 5
#
##
###
####
#####'''

#2)Pascal's Pyramid
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
        
n=int(input("Enter no of rows"))
for i in range(0,n):
    for j in range(0,n-i+1):
        print(" ",end=" ")
    for j in range(0,i+1):
        print((fact(i)//(fact(j)*fact(i-j)))," ", end=" ")    
    print()
'''output:
Enter no of rows5
            1
          1   1
        1   2   1
      1   3   3   1
    1   4   6   4   1'''