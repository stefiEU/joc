print("Ai ajuns in Asia.")
print(' ')
print("Ce alegi sa faci?")
print('1. Mergi in Tokyo')
print('2. Te intorci in Europa')
optiune = int(input('Unde vei merge?'))

if optiune == 1:
    print('Te afli in Tokyo')
    print('Ce vrei sa faci?')
    print('1. Te ascunzi si urmaresti oamenii')
    print('2. Te duci si incerci sa descoperi noul loc.')
    optiune2 = int(input('Care este alegerea ta?'))
    if optiune2 == 1:
        print(" BOOM! A explodat planeta")
        break
    else:
        print('BOOM! A explodat planeta')
        break
elif optiune == 2:
    print('Ai ales sa te intorci in Europa')

else:
    print('Optiune invalida')
