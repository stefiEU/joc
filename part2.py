inceput = int(input("Am o misiune importanta pentru tine, nu ma dezamagi! Esti un extraterestru numit Ollie si ai plecat spre Pamant. In parcursul tau pe Terra, vei avea de facut mai ulte decizii care iti vor influenta considerabil viitorul pe planeta dominata de oameni. Ce zici? Vrei sa intri in aceasta aventura? (1-da/0-nu)"))

if inceput == 0:
	break
else:
	print ("Buna alegere! Mult succes, Ollie! Acum, trebuie sa faci a doua ta alegere: mergi in Europa (1) sau in Asia (2)?")
        
    oe = int(input("Ai ajuns in Europa, Ollie! Sper sa-ti placa aici. Te-ai obisnuit cu alegerile? Esti pus in fata uneia noi: mergi in Brasov (1) sau in Barcelona (2)?"))

    if oe == 1:
	print ("Ai aterizat in Brasov, unul dintre cele mai frumoase orase din Romania. Aici mai ai de facut o alegere: vrei sa interactionezi cu oamenii sau vrei sa te feresti de ei?")
    else:
	    print ("Ai aterizat in Barcelona, un oras calduros nu numai la propriu, ci si la figurat. Oamenii de aici sunt foarte prietenosi. Pacat ca nu-i poti cunoaste... de fapt, e alegerea ta daca vrei sa-i cunosti sau nu. Te vezi cu oamenii sau te izolezi?")

        print('BOOM! A explodat planeta! PA!')
        break
else:    

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
