n=int(input(' how many row do you want?\n'))
count=n
for row in range(n,0,-1):
    #print(row)
    for space in range(0,n-row):
        print(' ',end='')
    count=count-1
    for star in range(0,row+count):
        print('*',end='')
    print('')
