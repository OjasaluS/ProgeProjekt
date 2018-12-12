def teise_toa_algus():
    print('Istud külmal põrandal ja toibud veidi. Sul tekib palju küsimusi- Mis juhtus? Miks sa külmal pinnal lebad? Kus sa oled? Ere tuli sinu peakohal süüdatakse. Kuuled juttu pealt..')
    print('-Noh ja mis me temaga teeme? Täiesti mõttetu katsealuse tõid.')
    print('-Ta oli ainuke kelle me kätte saime, teised põgenesid.')
    print('-Uskumatu, mul pole temaga mitte midagi teha.. Oota, miks tal silmad lahti on? Kui palju sa talle andsid?')
    print('Kuna hääl kostab teisest toa otsast on sul veidi aega, Mida teed?')
    print('1. Proovin end ruttu välja saada.')
    print('2. Mitte midagi.')
    
    esimene_valik = int(input('Kumma valiku teed?'))
   
    
    
    if esimene_valik == 1:
        print('Tõusid, et lahkuda, kuid olid liiga nõrk. Vajusid samas kokku. Sind tõsteti tagasi samale lauale, kuid seekord seoti sind kinni.')
        
    print('Tuttav mees ning naine, kelle häält oled kuulnud lähenevad sulle ning vaatavad sind hoolikalt. Jälgivad iga sinu reaktsiooni ja iga sinu kehaosa väga hoolikal. Üks võõrastest on sulle nii lähedal, et sa saaksid panna käe ta taskusse ja varastada ta käärid. Mis teed?')
    print('1. Võtad käärid.')
    print('2. Ei tee midagi.')
    teine_valik= int(input('Kumma valiku teed?'))
    
    if teine_valik==2 and esimene_valik==2:
        lõpp=4
    
    if teine_valik == 1 and esimene_valik == 1:
        print('Kahjuks olid enne juba põgenemise tõttu kinni seotud, ning ei saanud kääre kätte. Kuid midagi välja mõelda on juba hilja. Nägid uksest sisse tulemas valvurit. Ta teeb su lahti ning viib taaskord kuhugi mujale.')
        lõpp = 3
        
        
    elif esimene_valik== 1 and teine_valik== 2:
        lõpp=3
        ähvardus=0
        print('Mõne aja pärast tuleb sulle järgi juba tuttavaks saanud valvur ning viib su uude kohta.')
    
    elif teine_valik== 1 :
        
        print('Kas ähvardad neid inimesi kääridega?')
        print('1. Jah.')
        print('2. Ei.')
        
        ähvardus = int(input('Kumma valiku teed?'))
        
  
         
        
        if ähvardus == 1:
            
            if teine_valik == 1 and esimene_valik == 2 :
                
                print('Ärhvardad neid kääridega. Nii mees kui naine tunduvad väga hirmunud. Nende käed on üleval ja nad kuulavad, mis sul öelda on. Näed, et naine vajutab vaikset häirenuppu. Tead, et sul ei ole võimalik põgeneda ning aega napib, sul on aega küsida üks küsimus.')
                print('1. Miks ma siin olen?')
                print('2. Kes te olete?')
                print('3. Mida te just uurisiste?')
                
                küsimuse_valik= int(input('Millise küsimuse küsid?'))
                if küsimuse_valik== 1:
                    print('Sa.. Sa oled eriline, sinus on üks geen, mis...')
                elif küsimuse_valik== 2:
                    print('Me.. Me oleme teadlased, soovime teha vaid paar katset teie peal, sest..')
                elif küsimuse_valik== 3:
                    print('Me.. Me just uurisime sinu silmi, kuna sul on... ')
                    
                print('Uksest tormab sisse valvur enne, kui lause sai lõpetatud. Valvur viib su minema. ')
                lõpp = 3 
                
        if ähvardus==2:
            
            if teine_valik == 1 and esimene_valik == 2 :
                print('Üks toasviibijatest müksab sind, sinu käärid kukuvad maha. Toasviibijad on hämmingus. Nad ei oska midagi teha ning kutsuvad sulle valvuri järgi. Sind viiakse mujale.')
                lõpp = 3
            
            
    if lõpp== 3:
        print("Teel uude kohta ütleb valvur 'Ma pole iial pidanud mitte kedagi nii karmi valve alla kedagi saatma. Sinu otsused on sind viinud nii kaugele.' Ehk oleks aeg rahuneda?")
             
             
    if lõpp== 4:
        print('Lebad rahulikult kogu protseduuri aja, inimesed su ümber räägivad sinust tundmatute sõnadega ning jälgivad sind väga pingsalt. Umbes poole tunni pärast tuleb valvur ja viib su rahulikult minema.')
        
    
    return(lõpp)

teise_toa_algus()
            
            
            
