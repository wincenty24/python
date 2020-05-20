import numpy as np


def takeSecond(elem):
    return elem[1]

class DANE(object):
    Dane=""


class liczbywtablicy():
    tablica_liczb_Po_liczbach = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


class SORTOWANIE(liczbywtablicy):
    tablica_liczb=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#najczęściej pojawiające się liczby
    zero=0
    jeden = 0
    dwa = 0
    trzy = 0
    cztery = 0
    piec = 0
    szesc = 0
    siedem = 0
    osiem = 0
    dziewiec = 0
    dziesiec=0
    jedenascie=0
    dwanascie=0
    trzynascie=0
    czternascie=0
    pietnascie=0
    szesnascie=0
    siedemnascie=0
    osiemnascie=0
    dziewietnascie=0
    dwadziescia=0
    dwadziesciajeden=0
    dwadziesciadwa=0
    dwadziesciatrzy=0
    dwadziesciacztery=0
    dwadziesciapiec=0
    dwadziesciaszesc=0
    dwadziesciasiedem=0
    dwadziesciaosiem=0
    dwadziesciadziewiec=0
    trzydziesci=0
    trzydziescijeden=0
    trzydziescidwa=0
    trzydziescitrzy=0
    trzydziescicztery=0
    trzydziescipiec=0
    trzydziesciszesc=0
    trzydziescisiedem=0
    trzydziesciosiem=0
    trzydziescidziewiec=0
    czterdziesci=0
    czterdziescijeden=0
    czterdziescidwa=0
    czterdziescitrzy=0
    czterdziescicztery=0
    czterdziescipiec=0
    czterdziesciszesc=0
    czterdziescisiedem=0
    czterdziesciosiem=0
    czterdziescidziewiec=0

    def zerowanie(self):
        zero = 0
        jeden = 0
        dwa = 0
        trzy = 0
        cztery = 0
        piec = 0
        szesc = 0
        siedem = 0
        osiem = 0
        dziewiec = 0
        dziesiec = 0
        jedenascie = 0
        dwanascie = 0
        trzynascie = 0
        czternascie = 0
        pietnascie = 0
        szesnascie = 0
        siedemnascie = 0
        osiemnascie = 0
        dziewietnascie = 0
        dwadziescia = 0
        dwadziesciajeden = 0
        dwadziesciadwa = 0
        dwadziesciatrzy = 0
        dwadziesciacztery = 0
        dwadziesciapiec = 0
        dwadziesciaszesc = 0
        dwadziesciasiedem = 0
        dwadziesciaosiem = 0
        dwadziesciadziewiec = 0
        trzydziesci = 0
        trzydziescijeden = 0
        trzydziescidwa = 0
        trzydziescitrzy = 0
        trzydziescicztery = 0
        trzydziescipiec = 0
        trzydziesciszesc = 0
        trzydziescisiedem = 0
        trzydziesciosiem = 0
        trzydziescidziewiec = 0
        czterdziesci = 0
        czterdziescijeden = 0
        czterdziescidwa = 0
        czterdziescitrzy = 0
        czterdziescicztery = 0
        czterdziescipiec = 0
        czterdziesciszesc = 0
        czterdziescisiedem = 0
        czterdziesciosiem = 0
        czterdziescidziewiec = 0

    def __init__(self,p):
        self.p=p

    def ciąg_liczb_takich_samych(self,nazwa_pliku):
        file = open(f'{nazwa_pliku}', 'r')

        for znaki in file.readlines():
            x = ""
            for o in znaki:
                if o == '.':
                    o = ' '
                    x += o
                elif o == ',':
                    o = ' '
                    x += o
                else:
                    x += o

            dane = x.split(' ')
            dane.pop(1)
            file2 = open('lotto_bez_plusa_krotkie_2', 'r')
            for str in file2.readlines():
                x1 = ""
                for o1 in str:
                    if o1 == '.':
                        o1 = ' '
                        x1 += o1
                    elif o1 == ',':
                        o1 = ' '
                        x1 += o1
                    else:
                        x1 += o1

                dane2 = x1.split(' ')
                dane2.pop(1)
                #print(dane2)
                file2.close()
                if(dane[4]==dane2[4] and dane[5]==dane2[5] and dane[6]==dane2[6]  and dane[0]!=dane2[0] and dane[3]=='2018' and dane2[3]=='2018'):
                    print(dane2,dane)
        file.close()

    def liczby_po_liczbach(self,nazwa_pliku):
        file = open(f'{nazwa_pliku}', 'r')
        for znaki in file.readlines():
            x = ""
            for o in znaki:
                if o == '.':
                    o = ' '
                    x += o
                elif o == ',':
                    o = ' '
                    x += o
                else:
                    x += o

            dane = x.split(' ')
            dane.pop(1)
            for q,qwe in dane:
               print(qwe)



        file.close()

    def liczby_pojawiajace_sie_najczesciej_w_danym_roku(self, nazwa_pliku,rok):
        file = open(f'{nazwa_pliku}', 'r')
        tablica_liczb_w_danym_roku = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for znaki in file.readlines():
            x = ""
            for o in znaki:
                if o == '.':
                    o = ' '
                    x += o
                elif o == ',':
                    o = ' '
                    x += o
                else:
                    x += o

            dane = x.split(' ')
            dane.pop(1)
            if dane[3]==str(rok):
                if dane[4] == '0' or dane[5] == '0' or dane[6] == '0' or dane[7] == '0' or dane[8] == '0' or dane[
                    9] == '0':
                    tablica_liczb_w_danym_roku[0] += 1
                if dane[4] == '1' or dane[5] == '1' or dane[6] == '1' or dane[7] == '1' or dane[8] == '1' or dane[
                    9] == '1':
                    tablica_liczb_w_danym_roku[1] += 1
                if dane[4] == '2' or dane[5] == '2' or dane[6] == '2' or dane[7] == '2' or dane[8] == '2' or dane[
                    9] == '2':
                    tablica_liczb_w_danym_roku[2] += 1
                if dane[4] == '3' or dane[5] == '3' or dane[6] == '3' or dane[7] == '3' or dane[8] == '3' or dane[
                    9] == '3':
                    tablica_liczb_w_danym_roku[3] += 1
                if dane[4] == '4' or dane[5] == '4' or dane[6] == '4' or dane[7] == '4' or dane[8] == '4' or dane[
                    9] == '4':
                    tablica_liczb_w_danym_roku[4] += 1
                if dane[4] == '5' or dane[5] == '5' or dane[6] == '5' or dane[7] == '5' or dane[8] == '5' or dane[
                    9] == '5':
                    tablica_liczb_w_danym_roku[5] += 1
                if dane[4] == '6' or dane[5] == '6' or dane[6] == '6' or dane[7] == '6' or dane[8] == '6' or dane[
                    9] == '6':
                    tablica_liczb_w_danym_roku[6] += 1
                if dane[4] == '7' or dane[5] == '7' or dane[6] == '7' or dane[7] == '7' or dane[8] == '7' or dane[
                    9] == '7':
                    tablica_liczb_w_danym_roku[7] += 1
                if dane[4] == '8' or dane[5] == '8' or dane[6] == '8' or dane[7] == '8' or dane[8] == '8' or dane[
                    9] == '8':
                    tablica_liczb_w_danym_roku[8] += 1
                if dane[4] == '9' or dane[5] == '9' or dane[6] == '9' or dane[7] == '9' or dane[8] == '9' or dane[
                    9] == '9':
                    tablica_liczb_w_danym_roku[9] += 1
                if dane[4] == '10' or dane[5] == '10' or dane[6] == '10' or dane[7] == '10' or dane[8] == '10' or dane[
                    9] == '10':
                    tablica_liczb_w_danym_roku[10] += 1
                if dane[4] == '11' or dane[5] == '11' or dane[6] == '11' or dane[7] == '11' or dane[8] == '11' or dane[
                    9] == '11':
                    tablica_liczb_w_danym_roku[11] += 1
                if dane[4] == '12' or dane[5] == '12' or dane[6] == '12' or dane[7] == '12' or dane[8] == '12' or dane[
                    9] == '12':
                    tablica_liczb_w_danym_roku[12] += 1
                if dane[4] == '13' or dane[5] == '13' or dane[6] == '13' or dane[7] == '13' or dane[8] == '13' or dane[
                    9] == '13':
                    tablica_liczb_w_danym_roku[13] += 1
                if dane[4] == '14' or dane[5] == '14' or dane[6] == '14' or dane[7] == '14' or dane[8] == '14' or dane[
                    9] == '14':
                    tablica_liczb_w_danym_roku[14] += 1
                if dane[4] == '15' or dane[5] == '15' or dane[6] == '15' or dane[7] == '15' or dane[8] == '15' or dane[
                    9] == '15':
                    tablica_liczb_w_danym_roku[15] += 1
                if dane[4] == '16' or dane[5] == '16' or dane[6] == '16' or dane[7] == '16' or dane[8] == '16' or dane[
                    9] == '16':
                    tablica_liczb_w_danym_roku[16] += 1
                if dane[4] == '17' or dane[5] == '17' or dane[6] == '17' or dane[7] == '17' or dane[8] == '17' or dane[
                    9] == '17':
                    tablica_liczb_w_danym_roku[17] += 1
                if dane[4] == '18' or dane[5] == '18' or dane[6] == '18' or dane[7] == '18' or dane[8] == '18' or dane[
                    9] == '18':
                    tablica_liczb_w_danym_roku[18] += 1
                if dane[4] == '19' or dane[5] == '19' or dane[6] == '19' or dane[7] == '19' or dane[8] == '19' or dane[
                    9] == '19':
                    tablica_liczb_w_danym_roku[19] += 1
                if dane[4] == '20' or dane[5] == '20' or dane[6] == '20' or dane[7] == '20' or dane[8] == '20' or dane[
                    9] == '20':
                    tablica_liczb_w_danym_roku[20] += 1
                if dane[4] == '21' or dane[5] == '21' or dane[6] == '21' or dane[7] == '21' or dane[8] == '21' or dane[
                    9] == '21':
                    tablica_liczb_w_danym_roku[21] += 1
                if dane[4] == '22' or dane[5] == '22' or dane[6] == '22' or dane[7] == '22' or dane[8] == '22' or dane[
                    9] == '22':
                    tablica_liczb_w_danym_roku[22] += 1
                if dane[4] == '23' or dane[5] == '23' or dane[6] == '23' or dane[7] == '23' or dane[8] == '23' or dane[
                    9] == '23':
                    tablica_liczb_w_danym_roku[23] += 1
                if dane[4] == '24' or dane[5] == '24' or dane[6] == '24' or dane[7] == '24' or dane[8] == '24' or dane[
                    9] == '24':
                    tablica_liczb_w_danym_roku[24] += 1
                if dane[4] == '25' or dane[5] == '25' or dane[6] == '25' or dane[7] == '25' or dane[8] == '25' or dane[
                    9] == '25':
                    tablica_liczb_w_danym_roku[25] += 1
                if dane[4] == '26' or dane[5] == '26' or dane[6] == '26' or dane[7] == '26' or dane[8] == '26' or dane[
                    9] == '26':
                    tablica_liczb_w_danym_roku[26] += 1
                if dane[4] == '27' or dane[5] == '27' or dane[6] == '27' or dane[7] == '27' or dane[8] == '27' or dane[
                    9] == '27':
                    tablica_liczb_w_danym_roku[27] += 1
                if dane[4] == '28' or dane[5] == '28' or dane[6] == '28' or dane[7] == '28' or dane[8] == '28' or dane[
                    9] == '28':
                    tablica_liczb_w_danym_roku[28] += 1
                if dane[4] == '29' or dane[5] == '29' or dane[6] == '29' or dane[7] == '29' or dane[8] == '29' or dane[
                    9] == '29':
                    tablica_liczb_w_danym_roku[29] += 1
                if dane[4] == '30' or dane[5] == '30' or dane[6] == '30' or dane[7] == '30' or dane[8] == '30' or dane[
                    9] == '30':
                    tablica_liczb_w_danym_roku[30] += 1
                if dane[4] == '31' or dane[5] == '31' or dane[6] == '31' or dane[7] == '31' or dane[8] == '31' or dane[
                    9] == '31':
                    tablica_liczb_w_danym_roku[31] += 1
                if dane[4] == '32' or dane[5] == '32' or dane[6] == '32' or dane[7] == '32' or dane[8] == '32' or dane[
                    9] == '32':
                    tablica_liczb_w_danym_roku[32] += 1
                if dane[4] == '33' or dane[5] == '33' or dane[6] == '33' or dane[7] == '33' or dane[8] == '33' or dane[
                    9] == '33':
                    tablica_liczb_w_danym_roku[33] += 1
                if dane[4] == '34' or dane[5] == '34' or dane[6] == '34' or dane[7] == '34' or dane[8] == '34' or dane[
                    9] == '34':
                    tablica_liczb_w_danym_roku[34] += 1
                if dane[4] == '35' or dane[5] == '35' or dane[6] == '35' or dane[7] == '35' or dane[8] == '35' or dane[
                    9] == '35':
                    tablica_liczb_w_danym_roku[35] += 1
                if dane[4] == '36' or dane[5] == '36' or dane[6] == '36' or dane[7] == '36' or dane[8] == '36' or dane[
                    9] == '36':
                    tablica_liczb_w_danym_roku[36] += 1
                if dane[4] == '37' or dane[5] == '37' or dane[6] == '37' or dane[7] == '37' or dane[8] == '37' or dane[
                    9] == '37':
                    tablica_liczb_w_danym_roku[37] += 1
                if dane[4] == '38' or dane[5] == '38' or dane[6] == '38' or dane[7] == '38' or dane[8] == '38' or dane[
                    9] == '38':
                    tablica_liczb_w_danym_roku[38] += 1
                if dane[4] == '39' or dane[5] == '39' or dane[6] == '39' or dane[7] == '39' or dane[8] == '39' or dane[
                    9] == '39':
                    tablica_liczb_w_danym_roku[39] += 1
                if dane[4] == '40' or dane[5] == '40' or dane[6] == '40' or dane[7] == '40' or dane[8] == '40' or dane[
                    9] == '40':
                    tablica_liczb_w_danym_roku[40] += 1
                if dane[4] == '41' or dane[5] == '41' or dane[6] == '41' or dane[7] == '41' or dane[8] == '41' or dane[
                    9] == '41':
                    tablica_liczb_w_danym_roku[41] += 1
                if dane[4] == '42' or dane[5] == '42' or dane[6] == '42' or dane[7] == '42' or dane[8] == '42' or dane[
                    9] == '42':
                    tablica_liczb_w_danym_roku[42] += 1
                if dane[4] == '43' or dane[5] == '43' or dane[6] == '43' or dane[7] == '43' or dane[8] == '43' or dane[
                    9] == '43':
                    tablica_liczb_w_danym_roku[43] += 1
                if dane[4] == '44' or dane[5] == '44' or dane[6] == '44' or dane[7] == '44' or dane[8] == '44' or dane[
                    9] == '44':
                    tablica_liczb_w_danym_roku[44] += 1
                if dane[4] == '45' or dane[5] == '45' or dane[6] == '45' or dane[7] == '45' or dane[8] == '45' or dane[
                    9] == '45':
                    tablica_liczb_w_danym_roku[45] += 1
                if dane[4] == '46' or dane[5] == '46' or dane[6] == '46' or dane[7] == '46' or dane[8] == '46' or dane[
                    9] == '46':
                    tablica_liczb_w_danym_roku[46] += 1
                if dane[4] == '47' or dane[5] == '47' or dane[6] == '47' or dane[7] == '47' or dane[8] == '47' or dane[
                    9] == '47':
                    tablica_liczb_w_danym_roku[47] += 1
                if dane[4] == '48' or dane[5] == '48' or dane[6] == '48' or dane[7] == '48' or dane[8] == '48' or dane[
                    9] == '48':
                    tablica_liczb_w_danym_roku[48] += 1
                if dane[4] == '49' or dane[5] == '49' or dane[6] == '49' or dane[7] == '49' or dane[8] == '49' or dane[
                    9] == '49':
                    tablica_liczb_w_danym_roku[49] += 1

        #for indeks,e in enumerate(tablica_liczb_w_danym_roku):
            #print(f"Liczba {indeks} pojawiłą się  {e} razy")
        tabliczka = [[0 for i in range(2)] for j in range(50)]
        #print(tablica_liczb_w_danym_roku)
        for indeks in range(0, len(tablica_liczb_w_danym_roku)):
            # print(f"{indeks} {self.tablica_liczb[indeks]}")
            tabliczka[indeks][0] = f"{indeks}"
            tabliczka[indeks][1] = tablica_liczb_w_danym_roku[indeks]

        tabliczka.sort(key=takeSecond)
        print(f"Najczęściej losowane liczby w {rok}", tabliczka)
        file.close()


    def najczesciej_pojawiajace_sie_liczby(self,nazwa_pliku):

        file = open(f'{nazwa_pliku}', 'r')

        for znaki in file.readlines():
            x = ""
            for o in znaki:
                if o == '.':
                    o = ' '
                    x += o
                elif o == ',':
                    o = ' '
                    x += o
                else:
                    x += o

            dane = x.split(' ')
            dane.pop(1)
            if dane[4] == '0' or dane[5] == '0' or dane[6] == '0' or dane[7] == '0' or dane[8] == '0' or dane[9] == '0':
                self.zero += 1
                self.tablica_liczb[0] += 1
            if dane[4] == '1' or dane[5] == '1' or dane[6] == '1' or dane[7] == '1' or dane[8] == '1' or dane[9] == '1':
                self.jeden += 1
                self.tablica_liczb[1] += 1
            if dane[4] == '2' or dane[5] == '2' or dane[6] == '2' or dane[7] == '2' or dane[8] == '2' or dane[9] == '2':
                self.dwa += 1
                self.tablica_liczb[2] += 1
            if dane[4] == '3' or dane[5] == '3' or dane[6] == '3' or dane[7] == '3' or dane[8] == '3' or dane[9] == '3':
                self.trzy += 1
                self.tablica_liczb[3] += 1
            if dane[4] == '4' or dane[5] == '4' or dane[6] == '4' or dane[7] == '4' or dane[8] == '4' or dane[9] == '4':
                self.cztery += 1
                self.tablica_liczb[4] += 1
            if dane[4] == '5' or dane[5] == '5' or dane[6] == '5' or dane[7] == '5' or dane[8] == '5' or dane[9] == '5':
                self.piec += 1
                self.tablica_liczb[5] += 1
            if dane[4] == '6' or dane[5] == '6' or dane[6] == '6' or dane[7] == '6' or dane[8] == '6' or dane[9] == '6':
                self.szesc += 1
                self.tablica_liczb[6] += 1
            if dane[4] == '7' or dane[5] == '7' or dane[6] == '7' or dane[7] == '7' or dane[8] == '7' or dane[9] == '7':
                self.siedem += 1
                self.tablica_liczb[7] += 1
            if dane[4] == '8' or dane[5] == '8' or dane[6] == '8' or dane[7] == '8' or dane[8] == '8' or dane[9] == '8':
                self.osiem += 1
                self.tablica_liczb[8] += 1
            if dane[4] == '9' or dane[5] == '9' or dane[6] == '9' or dane[7] == '9' or dane[8] == '9' or dane[9] == '9':
                self.dziewiec += 1
                self.tablica_liczb[9] += 1
            if dane[4] == '10' or dane[5] == '10' or dane[6] == '10' or dane[7] == '10' or dane[8] == '10' or dane[
                9] == '10':
                self.dziesiec += 1
                self.tablica_liczb[10] += 1
            if dane[4] == '11' or dane[5] == '11' or dane[6] == '11' or dane[7] == '11' or dane[8] == '11' or dane[
                9] == '11':
                self.jedenascie += 1
                self.tablica_liczb[11] += 1
            if dane[4] == '12' or dane[5] == '12' or dane[6] == '12' or dane[7] == '12' or dane[8] == '12' or dane[
                9] == '12':
                self.dwanascie += 1
                self.tablica_liczb[12] += 1
            if dane[4] == '13' or dane[5] == '13' or dane[6] == '13' or dane[7] == '13' or dane[8] == '13' or dane[
                9] == '13':
                self.trzynascie += 1
                self.tablica_liczb[13] += 1
            if dane[4] == '14' or dane[5] == '14' or dane[6] == '14' or dane[7] == '14' or dane[8] == '14' or dane[
                9] == '14':
                self.czternascie += 1
                self.tablica_liczb[14] += 1
            if dane[4] == '15' or dane[5] == '15' or dane[6] == '15' or dane[7] == '15' or dane[8] == '15' or dane[
                9] == '15':
                self.pietnascie += 1
                self.tablica_liczb[15] += 1
            if dane[4] == '16' or dane[5] == '16' or dane[6] == '16' or dane[7] == '16' or dane[8] == '16' or dane[
                9] == '16':
                self.szesnascie += 1
                self.tablica_liczb[16] += 1
            if dane[4] == '17' or dane[5] == '17' or dane[6] == '17' or dane[7] == '17' or dane[8] == '17' or dane[
                9] == '17':
                self.siedemnascie += 1
                self.tablica_liczb[17] += 1
            if dane[4] == '18' or dane[5] == '18' or dane[6] == '18' or dane[7] == '18' or dane[8] == '18' or dane[
                9] == '18':
                self.osiemnascie += 1
                self.tablica_liczb[18] += 1
            if dane[4] == '19' or dane[5] == '19' or dane[6] == '19' or dane[7] == '19' or dane[8] == '19' or dane[
                9] == '19':
                self.dziewietnascie += 1
                self.tablica_liczb[19] += 1
            if dane[4] == '20' or dane[5] == '20' or dane[6] == '20' or dane[7] == '20' or dane[8] == '20' or dane[
                9] == '20':
                self.dwadziescia += 1
                self.tablica_liczb[20] += 1
            if dane[4] == '21' or dane[5] == '21' or dane[6] == '21' or dane[7] == '21' or dane[8] == '21' or dane[
                9] == '21':
                self.dwadziesciajeden += 1
                self.tablica_liczb[21] += 1
            if dane[4] == '22' or dane[5] == '22' or dane[6] == '22' or dane[7] == '22' or dane[8] == '22' or dane[
                9] == '22':
                self.dwadziesciadwa += 1
                self.tablica_liczb[22] += 1
            if dane[4] == '23' or dane[5] == '23' or dane[6] == '23' or dane[7] == '23' or dane[8] == '23' or dane[
                9] == '23':
                self.dwadziesciatrzy += 1
                self.tablica_liczb[23] += 1
            if dane[4] == '24' or dane[5] == '24' or dane[6] == '24' or dane[7] == '24' or dane[8] == '24' or dane[
                9] == '24':
                self.dwadziesciacztery += 1
                self.tablica_liczb[24] += 1
            if dane[4] == '25' or dane[5] == '25' or dane[6] == '25' or dane[7] == '25' or dane[8] == '25' or dane[
                9] == '25':
                self.dwadziesciapiec += 1
                self.tablica_liczb[25] += 1
            if dane[4] == '26' or dane[5] == '26' or dane[6] == '26' or dane[7] == '26' or dane[8] == '26' or dane[
                9] == '26':
                self.dwadziesciaszesc += 1
                self.tablica_liczb[26] += 1
            if dane[4] == '27' or dane[5] == '27' or dane[6] == '27' or dane[7] == '27' or dane[8] == '27' or dane[
                9] == '27':
                self.dwadziesciasiedem += 1
                self.tablica_liczb[27] += 1
            if dane[4] == '28' or dane[5] == '28' or dane[6] == '28' or dane[7] == '28' or dane[8] == '28' or dane[
                9] == '28':
                self.dwadziesciaosiem += 1
                self.tablica_liczb[28] += 1
            if dane[4] == '29' or dane[5] == '29' or dane[6] == '29' or dane[7] == '29' or dane[8] == '29' or dane[
                9] == '29':
                self.dwadziesciadziewiec += 1
                self.tablica_liczb[29] += 1
            if dane[4] == '30' or dane[5] == '30' or dane[6] == '30' or dane[7] == '30' or dane[8] == '30' or dane[
                9] == '30':
                self.trzydziesci += 1
                self.tablica_liczb[30] += 1
            if dane[4] == '31' or dane[5] == '31' or dane[6] == '31' or dane[7] == '31' or dane[8] == '31' or dane[
                9] == '31':
                self.trzydziescijeden += 1
                self.tablica_liczb[31] += 1
            if dane[4] == '32' or dane[5] == '32' or dane[6] == '32' or dane[7] == '32' or dane[8] == '32' or dane[
                9] == '32':
                self.trzydziescidwa += 1
                self.tablica_liczb[32] += 1
            if dane[4] == '33' or dane[5] == '33' or dane[6] == '33' or dane[7] == '33' or dane[8] == '33' or dane[
                9] == '33':
                self.trzydziescitrzy += 1
                self.tablica_liczb[33] += 1
            if dane[4] == '34' or dane[5] == '34' or dane[6] == '34' or dane[7] == '34' or dane[8] == '34' or dane[
                9] == '34':
                self.trzydziescicztery += 1
                self.tablica_liczb[34] += 1
            if dane[4] == '35' or dane[5] == '35' or dane[6] == '35' or dane[7] == '35' or dane[8] == '35' or dane[
                9] == '35':
                self.trzydziescipiec += 1
                self.tablica_liczb[35] += 1
            if dane[4] == '36' or dane[5] == '36' or dane[6] == '36' or dane[7] == '36' or dane[8] == '36' or dane[
                9] == '36':
                self.trzydziesciszesc += 1
                self.tablica_liczb[36] += 1
            if dane[4] == '37' or dane[5] == '37' or dane[6] == '37' or dane[7] == '37' or dane[8] == '37' or dane[
                9] == '37':
                self.trzydziescisiedem += 1
                self.tablica_liczb[37] += 1
            if dane[4] == '38' or dane[5] == '38' or dane[6] == '38' or dane[7] == '38' or dane[8] == '38' or dane[
                9] == '38':
                self.trzydziesciosiem += 1
                self.tablica_liczb[38] += 1
            if dane[4] == '39' or dane[5] == '39' or dane[6] == '39' or dane[7] == '39' or dane[8] == '39' or dane[
                9] == '39':
                self.trzydziescidziewiec += 1
                self.tablica_liczb[39] += 1
            if dane[4] == '40' or dane[5] == '40' or dane[6] == '40' or dane[7] == '40' or dane[8] == '40' or dane[
                9] == '40':
                self.czterdziesci += 1
                self.tablica_liczb[40] += 1
            if dane[4] == '41' or dane[5] == '41' or dane[6] == '41' or dane[7] == '41' or dane[8] == '41' or dane[
                9] == '41':
                self.czterdziescijeden += 1
                self.tablica_liczb[41] += 1
            if dane[4] == '42' or dane[5] == '42' or dane[6] == '42' or dane[7] == '42' or dane[8] == '42' or dane[
                9] == '42':
                self.czterdziescidwa += 1
                self.tablica_liczb[42] += 1
            if dane[4] == '43' or dane[5] == '43' or dane[6] == '43' or dane[7] == '43' or dane[8] == '43' or dane[
                9] == '43':
                self.czterdziescitrzy += 1
                self.tablica_liczb[43] += 1
            if dane[4] == '44' or dane[5] == '44' or dane[6] == '44' or dane[7] == '44' or dane[8] == '44' or dane[
                9] == '44':
                self.czterdziescicztery += 1
                self.tablica_liczb[44] += 1
            if dane[4] == '45' or dane[5] == '45' or dane[6] == '45' or dane[7] == '45' or dane[8] == '45' or dane[
                9] == '45':
                self.czterdziescipiec += 1
                self.tablica_liczb[45] += 1
            if dane[4] == '46' or dane[5] == '46' or dane[6] == '46' or dane[7] == '46' or dane[8] == '46' or dane[
                9] == '46':
                self.czterdziesciszesc += 1
                self.tablica_liczb[46] += 1
            if dane[4] == '47' or dane[5] == '47' or dane[6] == '47' or dane[7] == '47' or dane[8] == '47' or dane[
                9] == '47':
                self.czterdziescisiedem += 1
                self.tablica_liczb[47] += 1
            if dane[4] == '48' or dane[5] == '48' or dane[6] == '48' or dane[7] == '48' or dane[8] == '48' or dane[
                9] == '48':
                self.czterdziesciosiem += 1
                self.tablica_liczb[48] += 1
            if dane[4] == '49' or dane[5] == '49' or dane[6] == '49' or dane[7] == '49' or dane[8] == '49' or dane[
                9] == '49':
                self.czterdziescidziewiec += 1
                self.tablica_liczb[49] += 1

        tabliczka = [[0 for i in range(2)] for j in range(50)]
        #print(self.tablica_liczb)
        for indeks in range(0,len(self.tablica_liczb)):
            #print(f"{indeks} {self.tablica_liczb[indeks]}")
            tabliczka[indeks][0]=f"{indeks}"
            tabliczka[indeks][1] = self.tablica_liczb[indeks]

        tabliczka.sort(key=takeSecond)
        print("Najczęściej losowane liczby od 1957", tabliczka)
        file.close()


           # print(dane)






Slownik_liczb={0:"zero",
               1:"jeden",
               2:"dwa",
               3:"trzy",
               4:"cztery",
               5:"piec",
               6:"szesc",
7:'siedem',
8:'osiem' ,
9:'dziewiec',
10:'dziesiec',
11:'jedenascie' ,
12:'dwanascie' ,
13:'trzynascie' ,
14:'czternascie',
15:'pietnascie' ,
16:'szesnascie',
17:'siedemnascie',
18:'osiemnascie' ,
19:'dziewietnascie',
20:'dwadziescia' ,
21:'dwadziesciajeden',
22:'dwadziesciadwa' ,
23:'dwadziesciatrzy' ,
24:'dwadziesciacztery',
25:'dwadziesciapiec' ,
26:'dwadziesciaszesc' ,
27:'dwadziesciasiedem' ,
28:'dwadziesciaosiem' ,
29:'dwadziesciadziewiec',
30:'trzydziesci',
31:'trzydziescijeden',
32:'trzydziescidwa',
33:'trzydziescitrzy',
34:'trzydziescicztery',
35:'trzydziescipiec',
36:'trzydziesciszesc',
37:'trzydziescisiedem',
38:'trzydziesciosiem',
39:'trzydziescidziewiec',
40:'czterdziesci' ,
41:'czterdziescijeden',
42:'czterdziescidwa' ,
43:'czterdziescitrzy' ,
44:'czterdziescicztery',
45:'czterdziescipiec' ,
46:'czterdziesciszesc' ,
47:'czterdziescisiedem',
48:'czterdziesciosiem' ,
49:'czterdziescidziewiec'
               }

def selection_sort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x




#for x in range(0,50):
    #print(f"if dane[4]=='{x}' or dane[5]=='{x}' or dane[6]=='{x}' or dane[7]=='{x}' or dane[8]=='{x}' or dane[9]=='{x}':")
    #print(f"    tablica_liczb_w_danym_roku[{x}]+=1")


#str="6214. 05.02.2019 11,14,37,39,47,48"
file1 = open('lotek_bez_plusa.txt', 'r')
dane=DANE


rer=SORTOWANIE("d")
#rer.najczesciej_pojawiajace_sie_liczby('lotek_bez_plusa.txt')
rer.liczby_po_liczbach('lotek_bez_plusa.txt')
#rer.liczby_pojawiajace_sie_najczesciej_w_danym_roku('lotek_bez_plusa.txt',2018)
#rer.liczby_pojawiajace_sie_najczesciej_w_danym_roku('lotek_bez_plusa.txt',2019)
#rer.liczby_pojawiajace_sie_najczesciej_w_danym_roku('lotek_bez_plusa.txt',2020)
#rer.ciąg_liczb_takich_samych_3('lotto_bez_plusa_krotkie,txt')


#for indeks,e in enumerate(Najczesciej_losowane_liczby.tablica_liczb):
    #print(f"Liczba {indeks} pojawiłą się  {e} razy")

#Najczesciej_losowane_liczby.tablica_liczb.sort()
#print(Najczesciej_losowane_liczby.tablica_liczb)
#print(selection_sort(Najczesciej_losowane_liczby.tablica_liczb))

