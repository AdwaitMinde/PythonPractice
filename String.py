#some programs based on strings
#count occerence in string
str=input("Enter the string: ")
lst=[]
lst=str.split()
lst1=[]

for i in lst:
    if i not in lst1:
        lst1.append(i)


for i in lst1:
    print(i,"occerence: ",str.count(i))

'''output:
Enter the string: hello hello ok bye bye
hello occerence:  2
ok occerence:  1   
bye occerence:  2'''