#jak kożystać z programu?
#program jest do szukania rezystorów w układzie potencjometrycznym z szeregu e24
#wszystkie parametry poniżej trzeba wypełnić!!!!!!!!!!!!!!!!!!!!!!!!!!
# UCC= tutaj wpisujesz napięcie wejściowe układu
# UBE= napięcie baza emiter
# B=250 #beta tutaj wpisujesz parametr wzmocnienia
# IC_zal #prąd jaki ma płynąć przez kolektor
# UCE_zal= spadek napięcia na kolektor emiter
# URC_zal=
# URE_zal spadek napięcia na rezystorze kolektorowym
# T0=25 temp zerowa układu
# T1= # temp w której układ też ma pracować
# T2=# temp w której układ też ma pracować



e24 = [1 , 1.1 , 1.2 , 1.3 , 1.5 , 1.6 , 1.8 , 2 , 2.2 , 2.4 , 2.7 , 3 , 3.3 , 3.6 ,
       3.9 , 4.3 , 4.7 , 5.1 , 5.6 , 6.2 , 6.8 , 7.5 , 8.2 , 9.1 , 10 , 11.0 , 12.0 ,
       13.0 , 15.0 , 16.0 , 18.0 , 20 , 22.0 , 24.0 , 27.0 , 30 , 33.0 , 36.0 , 39.0 ,
       43.0 , 47.0 , 51.0 , 56.0 , 62.0 , 68.0 , 75.0 , 82.0 , 91.0 , 100 ,
       110 , 120.0 , 130.0 , 150.0 , 160.0 , 180.0 , 200 ,
       220 , 240.0 , 270.0 , 300 , 330.0 , 360.0 , 390.0 , 430.0 , 470.0 ,
       510, 560.0 , 620.0 , 680.0 , 750.0 , 820, 910.0 ,
       1000 , 1100.0 , 1200.0 , 1300.0 , 1500.0 , 1600.0 , 1800.0 , 2000 , 2200.0 ,
       2400.0 , 2700.0 , 3000 , 3300.0 , 3600.0 , 3900.0 , 4300.0 , 4700.0 , 5100.0 ,
       5600.0 , 6200.0 , 6800.0 , 7500.0 , 8200.0 , 9100.0 , 10000 , 11000.0 , 12000.0 ,
       13000.0 , 15000.0 , 16000.0 , 18000.0 , 20000 , 22000.0 , 24000.0 , 27000.0 , 30000 ,
       33000.0 , 36000.0 , 39000.0 , 43000.0 , 47000.0 , 51000.0 , 56000.0 , 62000.0 ,
       68000.0 , 75000.0 , 82000.0 , 91000.0 , 100000 , 110000 , 120000.0 ,
       130000.0 , 150000.0 , 160000.0 , 180000.0 , 200000 , 220000 , 240000.0 ,
       270000.0 , 300000 , 330000.0 , 360000.0 , 390000.0 , 430000.0 , 470000.0 ,
       510000 , 560000.0 , 620000.0 , 680000.0 , 750000.0 , 820000 ,
       910000.0 , 1000000 , 1100000.0 , 1200000.0 , 1300000.0 , 1500000.0 , 1600000.0 , 1800000.0 ,
       2000000 , 2200000.0 , 2400000.0 , 2700000.0 , 3000000 , 3300000.0 , 3600000.0 , 3900000.0 ,
       4300000.0 , 4700000.0 , 5100000.0 , 5600000.0 , 6200000.0 , 6800000.0 , 7500000.0 , 8200000
        , 9100000.0 ]
ilosc_kombi_nie_zmieniac=0
c=-0.002#tego nie można zmienić
y=0.005#tego nie można zmienić

UCC=12#to można zmienić
UBE=0.7#to można zmienić
B=250 #beta #to można zmienić
IC_zal=0.009#w amperach #to można zmienić
UCE_zal=4.8#to można zmienić
URC_zal=4.8#to można zmienić
URE_zal=2.4#to można zmienić
T0=25#to można zmienić
T1=-15#to można zmienić
T2=50#to można zmienić

for RC in e24:
    for RE in e24:
            UCE = UCC - IC_zal * RC - (IC_zal +(IC_zal/B)) * RE
            if(UCE >=UCE_zal*0.95 and UCE <=UCE_zal*1.05):
                for RB1 in e24:
                    for RB2 in e24:
                        UBB = (RB2 * UCC) / (RB1 + RB2)
                        RBB = (RB1 * RB2) / (RB1 + RB2)
                        IB = (UBB - UBE) / (RBB + RE * (B + 1))
                        IC = IB * B
                        if (IC >= IC_zal * 0.95 and IC <= IC_zal * 1.05):
                            B_T1=B*(1+y*(T1-T0))
                            U_BE_T1= UBE+c*(T1-T0)
                            IB_T1=(UBB -U_BE_T1)/(RBB+RE*(B_T1+1))
                            IC_T1=B_T1*IB_T1
                            UCE_T1=UCC-IB_T1*(B_T1*RC+(B_T1+1)*RE)
                            B_T2 = B * (1 + y * (T2 - T0))
                            U_BE_T2 = UBE + c*(T2 - T0)
                            IB_T2 = (UBB - U_BE_T2) / (RBB + RE * (B_T2 + 1))
                            IC_T2 = B_T2 * IB_T2
                            UCE_T2 = UCC - IB_T2 * (B_T2 * RC + (B_T2 + 1) * RE)
                            if UCE_T2<=UCE_zal*1.05 and UCE_T2>=UCE_zal*0.95 and IC_T2<=IC_zal*1.05 and IC_T2>=IC_zal*0.95 and UCE_T1<=UCE_zal*1.05 and UCE_T1>=UCE_zal*0.95 and IC_T1<=IC_zal*1.05 and IC_T1>=IC_zal*0.95 and IC*RC >= URC_zal*0.95 and IC*RC <= URC_zal*1.05 and IC*RE >= URE_zal*0.95 and IC*RE <= URE_zal*1.05:
                                ilosc_kombi_nie_zmieniac=ilosc_kombi_nie_zmieniac+1
                                print(f"{ilosc_kombi_nie_zmieniac}) " f"RB1 {RB1} ", f"RB2 {RB2} ", f"RE {RE} ",
                                      f"RC {RC} ", f"IB {IB} ", f"IC {IC} ", f"UBB {UBB} ", f"RBB {RBB} ",
                                      f"UCE {UCE} ", f"URE {IC * RE} ", f"URC {IC * RC} ", f"IC_T1 {IC_T1} ",
                                      f"IB_T1 {IB_T1} ", f"UCE_T1 {UCE_T1} ", f"URC_T1 {RC * IC_T1} ",
                                      f"URE_T1 {RE * IC_T1} ", f"IC_T2 {IC_T2} ", f"IB_T2 {IB_T2}", f"UCE_T2 {UCE_T2} ",
                                      f"URC_T2 {RC * IC_T2} ", f"URE_T2 {RE * IC_T2} ", f"B_T1 {B_T1} ",
                                      f"B_T2 {B_T2} ")
