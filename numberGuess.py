import random 

print('[-] ')


# input
print('\t\n Guess the number I hold.')
#print(rand)
try:
    # min = 
    # max = 
    # number guessing game
    rand = random.randint(int(input('[MIN NUMBER]> ')),int(input('[MAX NUMBER]> ')))
    trys=1
    intInput = int(input('[:+:]> '))

    while intInput!=rand:
        if intInput>rand:
            print(f'[-] the number is less than {intInput}')
        elif intInput<rand:
            print(f'[-] the number is grater than {intInput}')
        print('You Gessed wrong !')
        trys=trys+1
        intInput = int(input('[:+:]> '))
    print(f'[+] You guessed the right the number, is < {intInput}={rand} > you found the number in < {trys} > trys!')
except :
    print('< Input invalid >')
finally:
    print('< Game Over >')

    
