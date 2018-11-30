def uuesti():
    print("-"*97)
    print("You died")
    print("Kas soovid uuesti mängida?")
    print("jah?")
    vastus = input("Vastus:")
    if vastus == "jah":
        return "jah"
    else:
        return "ei"

def algus():
    print("-"*97)
    print("Avades silmad avastad end pimedast ruumist. Ainsaks valgusallikaks on toa teises otsas asetsev pisikene aken, kust kuult peegelduv valgus sisse kumab. Vaikselt hämarusega harjudes märkad enda kõrval lauda, kus on tikud ja küünal. 'Kus ma olen?' küsid sa endalt, püüdes meenutada, mis eelmistel päevadel oli juhtunud. Tühi. Täiesti tühi on pea. Aga nüüd on aeg tegutseda. Kuidas saada sellst kohast välja?")
    print("1.) Võtan tikud ja panen küünla põlema.")
    print("2.) Püüan aegamisi aknani jõuda ja sealt välja vaadata.")
    print("3.) Koban mööda seinu, äkki leidub kuskil lüliti?")
    valik_algus = int(input("Sisestage oma valik: "))
    return valik_algus   

def es_r_1(sisend):
    if sisend == 2:
        print("Kuna toas on veel hämar siis välja vaadates näed justkui suurt seina, millele on tõmmatud okastraat. Kas su silmad petavad sind või viibid sa mingisuguses vanglataolises hoones? Jätad selle meelde")
        print("Mida soovid edasi teha?")
        print("1.) Võtan nüüd tikud ja panen küünla põlema.")
        print("2.) Näen kõrvalseinas lülitit, lähen panen tule põlema.")
        valik_es_r_1 = int(input("Valik: "))
    if sisend == 3:
        print("Toa keskel laes läheb eredalt põlema lamp, mis pimestab sind täielikult. Vaikselt nägemise taastudes saad edasi tegutseda.")
        print("1.) Võtan nüüd tikud ja panen küünla põlema.")
        print("2.) Lähen vaatan aknast välja, et näha, kus ma olen.")
        valik_es_r_1 = int(input("Valik: "))
    return valik_es_r_1

def es_r_2(algne, jätk):
    if algne == 2:
        if jätk == 1:
            print('Just kui sa hakkad tikku tõmbama, et küünalt selles pimedas ruumis põlema panna, tunned veidrat lõhna. "Mis lõhn see on?" püüad endamisi selgusele jõuda selle kummalise tähelepaneku osas.')
            print("Enne, kui jõuad edasi tegutseda, lendab ruumi teises otsas pauguga lahti metalluks, mida sa pimedas märganud ei olnud. Ere valgus, mis ukseavast sisse kumab pimestab algselt, kuid kohe ilmub sinna ette jõulise mehe siluett, kelle nägu sa veel ei suuda tuvastada.")
            print('"Mulle öeldi, et sa oled ärkvel. Meeldiv," lausub mees madalal häälel.')
            print('"Kas sa tead, kus sa oled?"')
            print("Vastan: ")
            print('1.) "Pakun, et vanglas," jääb su vastus lühikeseks, kuid konkreetseks')
            print('2.) "Mul pole õrna aimugi. Palun, laske mind vabaks. Mul pole midagi väärtuslikku!" halad viimses hädas.')
            valik_es_r_2 = int(input("Valik: "))
    if algne == 2:
        if jätk == 2:
            print('Olles veel veidi segaduses oma nähtusest, püüad pimedas ruumis lülitit leida. Tugevalt silmi kissitades märkad justkui midagi kõrvalseinas. "Kas see võiks lüliti olla?" küsid endamisi.')
            print("Enne, kui jõuad edasi tegutseda, lendab ruumi teises otsas pauguga lahti metalluks, mida sa pimedas märganud ei olnud. Ere valgus, mis ukseavast sisse kumab pimestab algselt, kuid kohe ilmub sinna ette jõulise mehe siluett, kelle nägu sa veel ei suuda tuvastada.")
            print('"Mulle öeldi, et sa oled ärkvel. Meeldiv," lausub mees madalal häälel.')
            print('"Kas sa tead, kus sa oled?"')
            print("Vastan: ")
            print('1.) "Pakun, et vanglas," jääb su vastus lühikeseks, kuid konkreetseks')
            print('2.) "Mul pole õrna aimugi. Palun, laske mind vabaks. Mul pole midagi väärtuslikku!" halad viimses hädas.')
            valik_es_r_2 = int(input("Valik: "))
    if algne == 3:
        if jätk == 1:
            print('Võtad kätte tikud ja hakkad juba küünalt põlema panema kui su mõistus hakkab taastuma. "Miks mul eredas toas küünalt on vaja?" oled segaduses endaga. Oma mõtetes selgusele jõuda püüdes kuuled järsku samme.')
            print("Ereda toa teises otsas olev metalluks lendab pauguga lahti. Uksest vaatab vastu sulle pikka kasvu ja jõuline habemega mees. Ta tundub justkui tuttav, kuid kuidagi ei meenu, kust sa teda tunned.")
            print('"Mulle öeldi, et sa oled ärkvel. Meeldiv... Näe, isegi lüliti oled üles leidnud" lausub mees madalal häälel.')
            print('"Kas sa tead, kus sa oled?"')
            print("Vastan: ")
            print('1.) "Pakun, et vanglas," jääb su vastus lühikeseks, kuid konkreetseks')
            print('2.) "Mul pole õrna aimugi. Palun, laske mind vabaks. Mul pole midagi väärtuslikku!" halad viimses hädas.')
            valik_es_r_2 = int(input("Valik: "))
    if algne == 3:
        if jätk == 2:
            print('Sead sammud toa nurgas oleva akna poole. Püüdes sealt välja vaadata, näed vaid enda peegeldust. "Oleksin pidanud seda enne tulede põlema panemist tegema," kirud ennast. Järsku kuuled samme toa ukse taga...')
            print("Ereda toa teises otsas olev metalluks lendab pauguga lahti. Uksest vaatab vastu sulle pikka kasvu ja jõuline habemega mees. Ta tundub justkui tuttav, kuid kuidagi ei meenu, kust sa teda tunned.")
            print('"Mulle öeldi, et sa oled ärkvel. Meeldiv... Näe, isegi lüliti oled üles leidnud" lausub mees madalal häälel.')
            print('"Kas sa tead, kus sa oled?"')
            print("Vastan: ")
            print('1.) "Pakun, et vanglas," jääb su vastus lühikeseks, kuid konkreetseks')
            print('2.) "Mul pole õrna aimugi. Palun, laske mind vabaks. Mul pole midagi väärtuslikku!" halad viimses hädas.')
            valik_es_r_2 = int(input("Valik: "))
    return valik_es_r_2

def es_r_3(sisend):
    print(sisend)