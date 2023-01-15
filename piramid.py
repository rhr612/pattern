name=input("Hey! What's your name?\n" )
n=int(input(name+' how many row do you want?\n'))
count=0
for row in range(0,n):
    for space in range(0,n-row-1) :#jokhon input 4, 1st space:4-0-1=3
        print(' ',end='')          #jokhon input 4, 2nd space:4-1-1=2

    count=count+1
    for star in range(0,row+count):
        print('*',end='')
    print()
