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
else:
    print('Ai ales sa te intorci in Europa')
    oe = int(input("Ai ajuns in Europa, Ollie! Sper sa-ti placa aici. Te-ai obisnuit cu alegerile? Esti pus in fata uneia noi: mergi in Brasov (1) sau in Barcelona (2)?"))

    if oe == 1:
	    print("Ai aterizat in Brasov, unul dintre cele mai frumoase orase din Romania.")
        print('BOOM! A explodat planeta')
        break
    else:
	    print ("Ai aterizat in Barcelona, un oras calduros nu numai la propriu, ci si la figurat. Oamenii de aici sunt foarte prietenosi. Pacat ca nu-i poti cunoaste... de fapt, e alegerea ta daca vrei sa-i cunosti sau nu.")
        print('BOOM! A explodat planeta')
        break
