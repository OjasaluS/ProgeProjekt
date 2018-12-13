import time
import pygame
from ruum1 import *
from ruum3 import *
from ruum2 import *
from ruum4 import *
from intro import *

intro()

while True:
    #CHAPTER1
    try:
        print("ALGUS")
        valik_ruum1_1 = algus()
        if valik_ruum1_1 == 1:
            print("-"*97)
            print("Veel unise peaga ei tundnud sa seda imelikku lõhna, mis toas oli. Plahvatuslik gaas...")
            vastus = uuesti()
            if vastus == "jah":
                continue
            else:
                break
        print("-"*97)
        valik_ruum1_2 = es_r_1(valik_ruum1_1)
        print("-"*97)
        valik_ruum1_3 = es_r_2(valik_ruum1_1, valik_ruum1_2)
        print("-"*97)
        valik_ruum1_4 = es_r_3(valik_ruum1_3)
        print("-"*97)
        end_ruum1 = es_r_4(valik_ruum1_4)
        if end_ruum1 == 4:
            print("-"*97)
            print("Oodates juba suhteliselt pikka aega, kuuled lõpuks samme. Ukse peale ilmub hambuni relvastatud valvur, kes nähes kahte kolleegi maas teadvusetult lamamas, haarab paanikas oma relva, sihib sinu poole ja...")
            vastus = uuesti()
            if vastus == "jah":
                continue
            else:
                break
        print("-"*97)
        time.sleep(2)
        
        #CHAPTER2
        print("-"*97)
        print("\n")
        print("PÕGENEMINE")
        print("-"*97)
        if end_ruum1 == 3:
            end_ruum2 = teise_toa_algus()
            if end_ruum2 == 3
                print("Sa tunnetad ära, kuidas valvur on endast väljas ning ei pööra sulle piisavalt tähelepanu. Sinu võimalus tegutseda... Sa tunnetad ära õige hetke ja kogu oma keha massiga tõukad valvuri vastu seina.")
                print("Mehe pea põrub vastu kivist seina ning ta langeb teadvusetult maha...")
                valik_ruum3_1 = ruum3_1()
                valik_ruum3_2 = ruum3_2(valik_ruum3_1)               
                valik_ruum3_3 = ruum3_3(valik_ruum3_1, valik_ruum3_2)
                end_ruum3 = ruum3_4(valik_ruum3_3)
                if end_ruum3 == True:
                    vastus = uuesti()
                    if vastus == "jah":
                        continue
                    else:
                        break
                else:
                    lõpp = ruum4(end_ruum3)
                    if lõpp == True:
                        print("\n")
                        print("Palju õnne, saidki hakkama!")
                    if lõpp == False:
                        vastus = uuesti()
                        if vastus == "jah":
                            continue
                        else:
                            break
            if end_ruum2 == 4:
                print("Valvur, kes sind saatma on pandud tundub nõrgem kui teised ning justkui uus oma tööpostil. Kas nad on alahinnanud su tugevust või arvasid need inimesed, et rahustite mõju kestab sinu peal kauem?")
                print("Sa tunnetad ära, et suudad põgeneda. Ja just kui sa selle peale tuled, märkad sa koridori otsas veidi teistsugust ust...")
                print("Oma üle käiva jõuga vabastad käed ja lööd nõrga valvuri teadvusetuks. Seejärel jooksed ennist märgatud ukseni.")
                print("Vajutad lingi alla ja uks avanebki. Kas sa näed und või oled sa vabadusse pääsemas?")
                print("Märkad veel ukse kõrval riiulit, kus asetsevad püstol, nuga ja näpitsad.")
                print("1.) Võtad püssi ja astud välja.")
                print("2.) Võtad noa ja astud välja.")
                print("3.) Ei võta relva ja astud õue.")
                print("4.) Võtad näpitsad, kes teab, äkki läheb vaja?")
                otsus = int(input("Valik: ")) + 1
                lõpp = ruum4(otsus)
                if lõpp == True:
                    print("\n")
                    print("Palju õnne, saidki hakkama!")
                if lõpp == False:
                    vastus = uuesti()
                    if vastus == "jah":
                        continue
                    else:
                        break
        if end_ruum1 == 2:
            valik_ruum3_1 = ruum3_1()
            valik_ruum3_2 = ruum3_2(valik_ruum3_1)               
            valik_ruum3_3 = ruum3_3(valik_ruum3_1, valik_ruum3_2)
            end_ruum3 = ruum3_4(valik_ruum3_3)
            if end_ruum3 == True:
                vastus = uuesti()
                if vastus == "jah":
                    continue
                else:
                    break
            else:
                lõpp = ruum4(end_ruum3)
                if lõpp == True:
                    print("\n")
                    print("Palju õnne, saidki hakkama!")
                if lõpp == False:
                    vastus = uuesti()
                    if vastus == "jah":
                        continue
                    else:
                        break

        print("-"*97)
        time.sleep(3)
        
        break
        
    except:
        print("Väär sisestus, proovi uuesti.")
        print("-"*97)
        continue
        
