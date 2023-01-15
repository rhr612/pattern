n=int(input('How many line do you want?\n'))

for row in range(1,n+1):
    #print(row)
    for star in range(1,row+1):
        print('*',end='')
    print('')
