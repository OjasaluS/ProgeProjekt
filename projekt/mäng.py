from funktsioon import *
while True:
    valik_ruum1_1 = algus()
    if valik_ruum1_1 == 1:
        vastus = uuesti()
        if vastus == "jah":
            continue
        else:
            break
    print("-"*97)
    valik_ruum1_2 = es_r_1(valik_ruum1_1)
    print("-"*97)
    valik_ruum1_3 = es_r_2(valik_ruum1_1, valik_ruum1_2)
    valik_ruum1_4 = es_r_3(valik_ruum1_3)
    
    break