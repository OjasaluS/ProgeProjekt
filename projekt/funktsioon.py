def algus():
    print("Avades silmad avastad end pimedast ruumist. Ainsaks valgusallikaks on toa teises otsas asetsev pisikene aken, kust kuult peegelduv valgus sisse kumab. Vaikselt hämarusega harjudes märkad enda kõrval lauda, kus on tikud ja küünal. 'Kus ma olen?' küsid sa endalt, püüdes meenutada, mis eelmistel päevadel oli juhtunud. Tühi. Täiesti tühi on pea. Aga nüüd on aeg tegutseda. Kuidas saada sellst kohast välja?")
    print("1.) Võtan tikud ja panen küünla põlema.")
    print("2.) Püüan aegamisi aknani jõuda ja sealt välja vaadata.")
    print("3.) Koban mööda seinu, äkki leidub kuskil lüliti?")
    valik_algus = int(input("Sisestage oma valik: "))
    return valik_algus

def es_r_1(sisend):
    if sisend == 1:
        print("Tikud on läbi vettinud toas tunda olevast tugevast niiskusest. Ei lähe põlema.")
        print("Mida soovid edasi teha?")
        print("1.) Püüan aegamisi aknani jõuda ja sealt välja vaadata.")
        print("2.) Koban mööda seinu, äkki leidub kuskil lüliti?")
        valik_es_r_1 = int(input("Valik: "))
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
    if algne == 1:
        if jätk == 1:
            print("Kuna toas on veel hämar siis välja vaadates näed justkui suurt seina, millele on tõmmatud okastraat. Kas su silmad petavad sind või viibid sa mingisuguses vanglataolises hoones? Jätad selle meelde")
            print("Enne, kui jõuad edasi tegutseda, lendab ruumi teises otsas pauguga lahti metalluks, mida sa pimedas märganud ei olnud. Ere valgus, mis ukseavast sisse kumab pimestab algselt, kuid kohe ilmub sinna ette jõulise mehe siluett, kelle nägu sa veel ei suuda tuvastada.")
            print('"Mulle öeldi, et sa oled ärkvel. Meeldiv," lausub mees madalal häälel.')
            print('"Kas sa tead, kus sa oled?"')
            print("Vastan: ")
            print('1.) "Pakun, et vanglas," jääb su vastus lühikeseks, kuid konkreetseks')
            print('2.) "Mul pole õrna aimugi. Palun, laske mind vabaks. Mul pole midagi väärtuslikku!" halad viimses hädas.')
            valik_es_r_2 = int(input("Valik: "))
            return valik_es_r_2
    if algne == 2:
        if jätk == 1:
            print("algne 2, jätk 1")
    if algne == 3:
        if jätk == 1:
            print("algne 3, jätk 1")