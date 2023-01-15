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

count1=n
for row1 in range(n,0,-1):
    #print(row)
    for space1 in range(0,n-row1):
        print(' ',end='')
    count1=count1-1
    for star1 in range(0,row1+count1):
        print('*',end='')
    print('')
