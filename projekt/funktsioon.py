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
        global hint1
        hint1 = True
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
            print('1.) "Kes sa oled?" küsid suure enesekindlusega.')
            print('2.) "Mul pole õrna aimugi. Palun, laske mind vabaks. Mul pole midagi väärtuslikku!" halad viimses hädas.')
            valik_es_r_2 = int(input("Valik: "))
    if algne == 3:
        if jätk == 2:
            print('Sead sammud toa nurgas oleva akna poole. Püüdes sealt välja vaadata, näed vaid enda peegeldust. "Oleksin pidanud seda enne tulede põlema panemist tegema," kirud ennast. Järsku kuuled samme toa ukse taga...')
            print("Ereda toa teises otsas olev metalluks lendab pauguga lahti. Uksest vaatab vastu sulle pikka kasvu ja jõuline habemega mees. Ta tundub justkui tuttav, kuid kuidagi ei meenu, kust sa teda tunned.")
            print('"Mulle öeldi, et sa oled ärkvel. Meeldiv... Näe, isegi lüliti oled üles leidnud" lausub mees madalal häälel.')
            print('"Kas sa tead, kus sa oled?"')
            print("Vastan: ")
            print('1.) "Kes sa oled?" küsid suure enesekindlusega.')
            print('2.) "Mul pole õrna aimugi. Palun, laske mind vabaks. Mul pole midagi väärtuslikku!" halad viimses hädas.')
            valik_es_r_2 = int(input("Valik: "))
    return valik_es_r_2

def es_r_3(sisend):
    if sisend == 1:
        if hint1 == True:
            print('"Tundub, et vahelduseks on keegi targem ka siia sattunud... Tõstke ta ümber!" käsutab mees kedagi, ise samal ajal ümberpöörates ja kongist eemaldudes.')
            print("Siiski tundus, et mehe hääles oli justkui positiivne toon. Kas ma olin teda üllatanud?")
            print("Sisse tulevad kaks meest, kes suunduvad sinu poole, et sind kuhugi mujale viia.")
            print('1.) Hakkan vastu. Püüan lüüa ja vabadusse rabeleda.')
            print('2.) Lasen end rahulikult kinni võtta. ')
            valik_es_r_3 = int(input("Valik: "))
        if hint1 != True:
            print('"Eriti enesekindel mõni... Tõstke ta ümber!" käsutab mees kedagi, ise samal ajal ümberpöörates ja kongist eemaldudes.')
            print("Sisse tulevad kaks meest, kes suunduvad sinu poole, et sind kuhugi mujale viia.")
            print('1.) Hakkan vastu. Püüan lüüa ja vabadusse rabeleda.')
            print('2.) Lasen end rahulikult kinni võtta.')
            valik_es_r_3 = int(input("Valik: "))
    if sisend == 2:
        print('"Kas sellise siia tõi?" küsib mees kelleltki, kes ukse taga viibib. "Mis ma sellise nõrgukesega peale hakkan?"')
        print('"Igatahes..." lausub mees ümber pöörates. "Tõstke ümber," jagab ta kellelegi veel viimase käsu enne lahkumist.')
        print("Sisse tulevad kaks meest, kes suunduvad sinu poole, et sind kuhugi mujale viia.")
        print('1.) Hakkan vastu. Püüan lüüa ja vabadusse rabeleda.')
        print('2.) Lasen end rahulikult kinni võtta.')
        valik_es_r_3 = int(input("Valik: "))
    return valik_es_r_3
        
def es_r_4(sisend):
    if sisend == 2:
        print("Lased end rahus kinni võtta. Silmade ette pannakse riie nii, et sa ei näe enam midagi. Tunned järsku veel viimase asjana torget kaelal ja kaotad seejärel teadvuse.")
        lopp_1 = 3
    if sisend == 1:
        print("Nähes sind rusikaid tõstmas, võtavad valvurid välja oma nuiad ja valmistuvad rüseluseks.")
        print("Kas soovid jätaka esialgse plaaniga või langetad rusikad ja lased end kinni võtta?")
        print('1.) Ei anna alla! Võitlen lõpuni!')
        print('2.) Ei ma saa kahe vastu. Langetan rusikad ja alistun.')
        valik = int(input("Valik: "))
        if valik == 2:
            print("Lased end rahus kinni võtta. Silmade ette pannakse riie nii, et sa ei näe enam midagi. Tunned järsku veel viimase asjana torget kaelal ja kaotad seejärel teadvuse.")
            lopp_1 = 3
        if valik == 1:
            print("Vehid oma rusikatega kui segane, valvurid ei julge alguses lähedalegi tulla. Tundub, et nad pole sellega väga varem pidanud niimoodi tegelema.")
            print("Su käitumine on nad segadusse ajanud ja selle asemel, et su löökide eest ära põigata, tabad sa mõlemat. Valvurit vajuvad teadusetult kokku ning sa avastad enda ees vaba ukse ja võimaluse põgeneda.")
            print("Kuidas toimid?")
            print('1.) Võtad valvurilt nuia ja liigud ukse poole.')
            print('2.) Jätad kõik asjad maha, et oleksid kiirem ja kergem.')
            print('3.) Otsustad mitte põgeneda ja jääd oma saatust ootama voodil istudes.')
            lopp_1 = int(input("Valik: "))
            
            
            
        