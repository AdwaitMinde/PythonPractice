'''Convert time entered into seconds'''
t_h=int(input("Enter hours: "))
t_m=int(input("Enter minutes: "))
t_s=int(input("Enter seconds: "))
tot_time=t_h*3600+t_m*60+t_s
print("Time in seconds= ",tot_time)

'''output:
Enter hours: 4
Enter minutes: 53
Enter seconds: 21
Time in seconds=  17601'''