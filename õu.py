def õuesolek(relv):
    print('Said lõpuks toast välja, väljas on suhteliselt pime. Kuid harjud pimedusega ruttu. Vabadus on peaaegu käes..')
    
    if relv == 1 :
        #püss
        print('Kuuled kedagi karjumas.. Tundub, et keegi väljastpoolt kuulis sinu lasku. Sind lasti maha enne, kui sa sammugi astuda said.')
        print('You died')
    elif relv == 2:
        #nuga
        print('Võitluse käigus vigastasid end rängalt ning sinu kõhul on suur veritsev noahaav. Oled jõuetu ning kukud sealsamas kokku. ')
        print('You died')
    elif relv ==3:
        #näpitsad
        print('Välja tulles näed suurt seina okastraadiga, ronid kiirelt ja lõikad traati oma näpitsatega.')
        print('Naudi vabadust.')
    elif relv == 0:
        #mittemidagi
        print('Näed enda ees suurt aeda, mis on okastraadiga kaetud. Üritades ronida üle vigastad end korralikult, kuid saad teisele poole.')
        print('Naudi vabadust. Ja otsi palun arstiabi. Sinu õnneks on armid moes..')
        
