def ruum3_1():
        print('"Kuhu nüüd?" küsid endalt. Pärast põgenemist oled järjest mööda kitsaid koridore jooksnud, ilma kedagi kohtamata. Sa arvad, et oled nüüd piisavalt jooksnud, et korraks hinge tõmmata ja hakata mõtlema, kuhu minna.')
        print("Sa võtad hoo maha ja uurid ümbrust. Seisad kitsas koridoris, ümbritsevad sind kivist seinad, põrand ja lagi. Näed eespool koridori lõppu, kust hargnevad teed paremale ja vasakule. Tagasi minemine on mõtlematu, sa oled juba pikemat aega mööda seda koridori jooksnud ning tagasi minemine seaks sind ohtu. Peale koridori lõppu jooksmise, märkad laes ka justkui mingisugust õhutusava. Mida soovid teha?")
        print("1.) Üritad õhutusava lahti saada ning sinna pugeda.")
        print("2.) Jooksed koridori lõppu ja pöörad paremale.")
        print("3.) Jooksed koridori lõppu ja pöörad vasakule.")
        valik = int(input("Valik: "))
        return valik


def ruum3_2(sisend):
    if sisend == 1:
        print("Üritad kõigest jõust hüpata õhutusavani, kuid sa lihtsalt ei ulata. Oled hüppamisest juba nii väsinud, et ei jaksa edasi liikuda.")
        print("Eemalt on kosta sammude lähenemist. Kuidas käitud?")
        print("1.) Tead, et rusikatega sa valvuritele, kes sind juba kaugelt märkavad, vastu ei saa. Põgened.")
        print("2.) Mängid surnut, äkki suudad valvurid ära petta.")
        valik = int(input("Valik: "))
    if sisend == 2:
        print("Sa jooksed koridori lõppu ja muule mõtlemata pöörad koheselt paremale ning annad jalgadele valu.")
        print("Pärast pikaajalist, mis tundus justkui terve eluaeg, jooksmist jõuad lõpuks ühe raudukseni. Selle kõrval on kolm nuppu ning täiesti tundmatus keeles pealkirjad nuppudel.")
        print("Kuidas toimid?")
        print("1.) Vajutad nuppe.")
        print("2.) Parem ei jända nuppudega, lähed tagasi ja võtad teise koridori hargnevuse.")
        valik = int(input("Valik: "))
        if valik == 1:
            print("Mis järjekorras soovid nuppe vajutada? (Sisesta arvud 1,2,3 õiges järjekorras üksteise järel, ilma komade või tühikuteta).")
            valik = int(input("Järjekord: "))

    if sisend == 3:
        print("Sa jooksed koridori lõppu ja muule mõtlemata pöörad koheselt vasakule ning annad jalgadele valu.")
        print("Avastad end korraga koridorist, kus on palju uksi, vasakul seinas kolm, paremal neli järjest. Samas kuuled ka samme lähenemas ja inimesi kõnelemas kuskil ümbruses. Kuidas käitud?")
        print("1.) Valid hoolikalt ruumi kuhu peita end. Ukse taga veidi kuulates oled kindel, et ruum on seest tühi. Saaksid seal veidi aega mööda saata ja hiljem üritada põgeneda. Sisened ruumi.")
        print("2.) Jooksed ruumidest mööda ja püüad leida väljapääsu.")
        valik = int(input("Valik: "))
    return valik


def ruum3_3(algus, järg):
    if algus == 1:
        if järg == 1:
            print("Jooksed nii kaua kui jaksad, kuid see ei ole piisav kui avastad end järsku tupikust. Kuhugi pole enam minna kui tagasi... Aga sealt tulevad valvurid... Kukud suurest paanikast ja väsimusest lihtsalt kokku.")
            return True
        if järg == 2:
            print("Surnu mängimine kedagi ära ei peta ja karistuseks valvurite ründamise eest asetatakse su pea pakule ja...")
            return True

    if algus == 2:
        if järg == 213:
            print("Uks avaneb... Sa näed enda ees suur avarat aeda ning võimalust põgeneda.")
            print("Kuidas toimid?")
            valik = input("Põgened? (jah)/(ei): ")
        if järg == 2:
            print("Kuhu nüüd siis edasi?")
            print("1.) Jooked tagasi ja võtad selle koridori, mis viis vasakule ning püüad sealt kuhugi jõuda.")
            print("2.) Istud maha esimesse ruumi, mille leiad ja puhkad. Lihtsalt ei jaksa enam joosta. Juhtugu, mis juhtuma peab.")
            valik = int(input("Valik: "))
            if valik == 1:
                valik += 2
        if järg != 213 and järg > 10:
            print("Käima läheb kõva sireen ja sekundiga on kohal hulk valvureid, kes avavad sinu pihta tule...")
            return True
            
        
    if algus == 3:
        if järg == 1:
            print("Tunned järsku kuidas oled jube väsinud. Silmad vajuvadki kinni ja...")
            print("Ärkad ehmatusega halvast unenäost, kuid õnneks pole sinuga midagi vahepeal juhtunud. Ainult veidi külm on justkui.")
            print("Kuidas käitud edasi?")
            print("1.) Väljud ruumist ja püüad edasi väljapääsu leida.")
            print("2.) Ootad, kuni kuuled kedagi möödumas ning püüad neid siis äkitselt rünnata, et saada relva või võtmeid enda valdusesse")
            print("3.) Magad veel veidi.")
            valik = int(input("Valik: ")) + 4
        if järg == 2:
            print("Oma suures paanikas jooksed täiesti mõtlematult ringi ning kukud alla treppidest, mida sa märganud ei olnud...")
            return True  
    return valik

def ruum3_4(sisend):
    if sisend == 2:
        print("Sisened tühja ruumi ja jääd suurest väsimusest lihtsalt magama. Sa ei pane tähele kui külm selles ruumis on. Magad nii kaua, et sinu keha lihtsalt alajahtub. Su eluvaim kustub...")
        return True
    if sisend == 5 or sisend == 3:
        print('Pärast hoolikad ja ettevaatlikku otsimist ning koridoride uurimist leiad ukse, mis erineb teistest. "Kas see võiks olla mu pääs välja?" küsid endamisi. "Mis küll oleks see võimalus, et see uks on lahti..."')
        print("Vajutad lingi alla ja uks avanebki. Kas sa näed und või oled sa vabadusse pääsemas?")
        print("Märkad veel ukse kõrval riiulit, kus asetsevad püstol, nuga ja näpitsad.")
        print("1.) Võtad püssi ja astud välja.")
        print("2.) Võtad noa ja astud välja.")
        print("3.) Ei võta relva ja astud õue.")
        print("4.) Võtad näpitsad, kes teab, äkki läheb vaja?")
        valik = int(input("Valik: ")) + 1
    if sisend == 6:
        print("Su ootamine tasus end ära. Kuuled kedagi oma ruumist möödumas ja nüüd on sinu hetk tegutseda.")
        print("Kuidas käitud?")
        print("1.) Lööd ukse järsult lahti ja asud võitlusesse.")
        print("2.) Lased valvuril mööduda ja hiilid seejärel välja ning otsid põgenemisteed edasi.")
        otsus = int(input("Valik: "))
        if otsus == 1:
            print("Asud valvuriga võitlusesse ja oled isegi võitmas, sest tabad teda väga haavataval hetkel. Siiski peab mees piisavalt kaua vastu, et oma kõva häälega teisi appi kutsuda ning kui sa lõpuks suudad tema elu võtta, kaotad abivägedele enda oma...")
            return True
        if otsus == 2:
            print('Pärast hoolikad ja ettevaatlikku otsimist ning koridoride uurimist leiad ukse, mis erineb teistest. "Kas see võiks olla mu pääs välja?" küsid endamisi. "Mis küll oleks see võimalus, et see uks on lahti..."')
            print("Vajutad lingi alla ja uks avanebki. Kas sa näed und või oled sa vabadusse pääsemas?")
            print("Märkad veel ukse kõrval riiulit, kus asetsevad püstol, nuga ja näpitsad.")
            print("1.) Võtad püssi ja astud välja.")
            print("2.) Võtad noa ja astud välja.")
            print("3.) Ei võta relva ja astud õue.")
            print("4.) Võtad näpitsad, kes teab, äkki läheb vaja?")
            valik = int(input("Valik: ")) + 1
    if sisend == 7:
        print("Magades ei pane sa tähele kui külm sul on ja sa alajahtud. Vaikselt ja rahulikult unes saabub su surm...")
        return True
    if sisend == True:
        return True
    if sisend == "jah":
        return False
    if sisend == "ei":
        print("Hakkad tagasi pöörama, kuid juba on sulle jälile saadud. Vaatad tõtt pika ja jõulise valvuriga, kelle püssitoru on sinu poole sihitud. Kõlab lask...")
        return True
    
    return valik