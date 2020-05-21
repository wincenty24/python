import numpy as np

class SORTOWANIE(object):
    def __init__(self,nazwapliku_):
        self.nazwapliku_=nazwapliku_

    def ciąg_liczb_takich_samych(self):
        file = open(f'{self.nazwapliku_}', 'r')
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

    def ilczby_pojawiające_sie_po_liczbach(self,od_roku,do_roku):
        def wez2element(elem):
            return elem[1]
        file = open(f'{self.nazwapliku_}', 'r')
        liczby= [[0 for i in range(50)] for j in range(50)]
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

            if int(dane[3])>=od_roku and int(dane[3])<=do_roku:
                for valuearray in range(0,50):
                    for var in range(4,9):
                        if(int(dane[var]) == valuearray):
                            for value in range(0, 50):
                                if int(dane[var+1]) == value:
                                    liczby[valuearray][value] += 1
        file.close()
        #for value in range(50):
            #print(f"dla liczby {value}", liczby[value][:])
        tablica_liczb_sort = [[[0 for i in range(2)] for j in range(50)] for k in range(50)]
        for t in range(50):
            for k in range(50):
                tablica_liczb_sort[t][k][0] = k
                tablica_liczb_sort[t][k][1] = liczby[t][k]
            tab=tablica_liczb_sort[t][:][:]
            tab.sort(key=wez2element)
            #print(tab)
            print([i[::-1] for i in tab[::-1]])
            #print(f"po liczie {t} najczęściej pojawaiała się ", f" liczba: {tab[t][0]} tyle razy: {tab[t][1]}" )
            #print(f"tls{t} ",tablica_liczb_sort[t][:][:])
    def najczesciej_pojawiajace_sie_liczby(self,od_roku,do_roku):
        def wez2element(elem):
            return elem[1]

        tablica=[0]*50
        file = open(f'{self.nazwapliku_}', 'r')
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
            if int(dane[3])>=od_roku and int(dane[3])<=do_roku:
                for value in range(50):
                    for value_array in range(4,10):
                        if(int(dane[value_array])==value):
                            tablica[value]+=1
        tablica_liczb_sort = [[0 for i in range(2)] for j in range(50)]

        for var in range(50):
            tablica_liczb_sort[var][0] = var
            tablica_liczb_sort[var][1] = tablica[var]
        tablica_liczb_sort.sort(key=wez2element)

        for var in range(50):
            print(f"Liczba {tablica_liczb_sort[var][0]} pojawiła się {tablica_liczb_sort[var][1]}")





rer=SORTOWANIE('lotek_bez_plusa.txt')
rer.najczesciej_pojawiajace_sie_liczby(2019,2019)
rer.ilczby_pojawiające_sie_po_liczbach(2019,2019)
"""
tablica_liczb_sort = [[[0 for i in range(2)] for j in range(5)] for k in range(5)]
tablica_liczb_sort[0][0][0]=0
tablica_liczb_sort[0][0][1]=1
tablica_liczb_sort[0][1][0]=2
tablica_liczb_sort[2][4][1]=3
for t in range(5):
    for k in range(5):
        tablica_liczb_sort[t][k][0] = k
    print(tablica_liczb_sort[t][:][:])"""