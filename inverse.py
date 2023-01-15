n=int(input('How many line do you want?\n'))

for row in range(n,0,-1):###################################
    for star in range(1,row+1):
        print('*',end='')
    print('')
