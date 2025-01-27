from datetime import *
from calendar import *
from math import *

# Ülesanne 10
try:
    min=float(input("Sisestage aeg minutites: "))
    if min>0:
        tunnid=min//60
        jäägid_min=min%60
        print(f"{tunnid}:{jäägid_min}")
    else:
        print("Aega peavad olema suuremad kui 0 olla!")
except:
    print("Vale andmed")

#Ülesanne 9
try:
    Kiirus=29.9*5/18
    M=float(input("Ajakulu: ")) 
    if M>0:
        Kaugus=Kiirus*M
        print(f"Kaugus: {Kaugus}")
    else:
        print("Aega peavad olema suuremad kui 0 olla!")
except:
    print("Vale andmed")

#Ülesanne 8
try:
    L=float(input("Liitrit kütust paagis: "))
    km=float(input("Läbitud kilomeetrid: "))
    if L>0 and km>0:
        tarbimine=(L/km)*100
        print(f"Keskmine kütusekulu 100 km kohta: {tarbimine}")
    else:
        print("Liitrid ja kilomeetrid peavad olema suuremad kui 0 olla!")
except:
    print("Vale andmed")

#Ülesanne 7
try:
    a=float(input("A: "))
    b=float(input("B: "))
    if a>0 and b>0:
        print("Pindala ja ümbermõõdu rvutamine: ")
        S=a*b
        P=(a+b)*2
        print(f"S={S}, P={P}")
    else:
        print("Arvud peavad suurem kui 0 olla!")
except:
    print("Vale andmed")

#Ülesanne 6
tekst="Rong see sõitis tsuhh tsuhh tsuhh, \n piilupart oli rongijuht. \n Rattad tegid rat tat taa, \n rat tat taa ja tat tat taa. \n Aga seal rongi peal, \n kas sa tead, kes olid seal? \n Rong see sõitis tuut tuut tuut, \n piilupart oli rongijuht. \n Rattad tegid kill koll koll, \n kill koll koll ja kill koll kill."
Suur=tekst.upper()
print(Suur)


#ülesanne 5
a="kill-koll ".capitalize()
b="killadi-koll ".capitalize()
print(a*2,b,a*2,b,a*4)


#Ülesanne 4
d=2.575 #диаметр монеты см
maaR=6378 #радиус земли км
maaR*=100000 #радиус земли см
Pmaa=2*pi*maaR #окружность земли
kogus=Pmaa / d
print(f"Meil on vaja {int(kogus):,d} mündi.")
print(f"Meil on vaja {int(kogus*2):,d} euro.")

#Ülesanne 3
try:
    R=float(input("R: "))
    Sruudu=(2*R)**2
    Sringi=pi*R**2
    Pruudu=8*R
    Pringi=2*pi*R
    print(f"Vastus:\n Ruudu pindala on {Sruudu}\n Ruudu on ümbermõõt on {Pruudu}\n Ringi pindala on {Sringi}\n Ringi pindala on {Pringi}.")
except:
    print("Sisesta ujukomaarvud!")

#Ülesanne 2
a=3 + 8 / (4 - 2) * 4
print(f"3 + 8 / (4 - 2) * 4 = {a}") #Оригинальнный пример
b=3 + 8 / 4 - 2 * 4
print(f"3 + 8 / 4 - 2 * 4 = {b}") #Убрала скобки
c=8 / 3 + (4 - 2) * 4
print(f"8 / 3 + (4 - 2) * 4 = {c}") #Сначала поделила 8 на 3 а после отняла результат в скобках умноженое на 4


#Ülesanne 1
tana=date.today()
print(f"Tere! Täna on {tana}")

# 27/12/2022
tana_ = tana.strftime("%d/%m/#Y")
print(f"Tere! Täna on {tana}")
paevadekodus=monthrange(2025,1)[1]
print(f"jaanuaris on {paevadekodus} päeva")
paevad=tana.day
onjäänud=paevadekodus-paevad
print(f"Jäänuaris on jäänud {onjäänud} on jäänud")
#1.V
aastalõpuni=onjäänud+monthrange(2025,2)[1]+monthrange(2025,3)[1]+monthrange(2025,4)[1]+monthrange(2025,5)[1]+monthrange(2025,6)[1]+monthrange(2025,7)[1]+monthrange(2025,8)[1]+monthrange(2025,9)[1]+monthrange(2025,10)[1]+monthrange(2025,11)[1]+monthrange(2025,12)[1]
print(f"Aasta lõpuni on Jäänud {aastalõpuni}")
#2.V
aastalõpuni=365-monthrange(2025,1)[1]+onjäänud

# # Decemder 27, 2022
# tana = tana.strftime("%B/%d/#Y")
# print(f"Tere! Täna on {tana}")

# # 12/27/22
# tana = tana.strftime("%m/%d/%y")
# print(f"Tere! Täna on {tana}")

# # Dec-27-2022
# tana = tana.strftime("%b-%d-%Y")
# print(f"Tere! Täna on {tana}")
