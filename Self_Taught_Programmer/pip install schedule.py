arrWord = ['C','A','L','E','B']
bFound = False
sWord = 'CALEB'
iNum = 0

while bFound == False:
    geuss = input('Whats your geuss?')
    iNum += 1
    if geuss in arrWord:
        print('You got a letter!')
    elif geuss not in arrWord:
        print('Thats not one of the letters! Geuss again')
    if input('Are you ready to geuss the full word?') == 'YES':
        if input('?') == sWord:
            print('you won! and it only took you ' + str(iNum) + ' geusses!' )
            bFound = True 