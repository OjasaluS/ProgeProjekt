def ruum4(sisend):
    print('Said lõpuks toast välja, väljas on suhteliselt pime. Kuid harjud pimedusega ruttu. Vabadus on peaaegu käes..')
    
    if sisend == 2:
        #püss
        print('Kuuled kedagi karjumas ja tulistad refleksist sinna poole. Tundub, et keegi väljastpoolt kuulis sinu lasku. Sind lasti maha enne, kui sa sammugi astuda said.')
        return False
    elif sisend == 3:
        #nuga
        print('Nuga käes astud õue ja oled täis raevu. Selle asemel, et põgeneda, sa hoopis ründad valvurit, kes sind takistama tuleb.')
        print("Võitluse käigus said sa rängalt vigastada ning sinu kõhul on suur veritsev noahaav. Oled jõuetu ning kukud sealsamas kokku.")
        return False
    elif sisend == 4 or sisend == False:
        #mittemidagi
        print('Näed enda ees suurt aeda, mis on okastraadiga kaetud. Üritades ronida üle vigastad end korralikult, kuid saad teisele poole.')
        print('Naudi vabadust. Ja otsi palun arstiabi. Sinu õnneks on armid moes..')
        return True
    elif sisend == 5:
        #näpitsad
        print('Välja tulles näed suurt seina okastraadiga, ronid kiirelt ja lõikad traati oma näpitsatega.')
        print('Naudi vabadust.')
        return True