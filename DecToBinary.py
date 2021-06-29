#Convert Decimal number to Binary Number
dec_n=int(input("Enter number"))
bin_n=0
k=1
while dec_n!=0:
    r=int(dec_n%2)
    bin_n=bin_n+(r*k)
    dec_n=dec_n/2
    k=k*10
print(bin_n)

'''output:
Enter number10
1010'''