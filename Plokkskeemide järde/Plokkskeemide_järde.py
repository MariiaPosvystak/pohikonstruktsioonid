from time import sleep
#V5, 3. Группа из 20 студентов сдала три экзамена за одну сессию. Напишите алгоритм заполнения экзаменационной ведомости.

for õ in range(20):
    print (f"soritab eksamit {õ+1}. õpilane")
    for e in range(3):
        print(f"{e+1}. eksam")

#V4, 2. Составьте блок-схему программы для вычисления суммы только отрицательных значений P.

vastus=0
P=int(input("Mitu korda kordame? "))
while True:
    arv=float(input("Sisesta arv: "))
    if arv<0: vastus +=arv
    P-=1
    if P==0: break
print (f"Summa on {vastus}")


#V1, 4. Напишите блок-схему робота, который жарит котлеты.

kokku=int(input("Kokku kotlete: "))
panni_maht=int(input("Panni maht: "))
aeg=1
lahenemine=kokku//panni_maht
jaak=kokku%panni_maht
if jaak>0: lahenemine+=1
print(f"Kottletid pannil")
for l in range (lahenemine):
    if jaak>0 and l==lahenemine-1:
        print(f"Panni peal on {jaak} kotlet.")
    else:
        print(f"Panni peal on {panni_maht} kotlet.")
    print(f"{l+1}. lahetamine. Praeme esimene pool")
    sleep(aeg)
    print("Ümberpööramine")
    print(f"{l+1}. lahetamine. Praeme teine pool")
    sleep(aeg)
    print("Kotleti valmis")
print("Kõik kotletid on praetud")

#V2, 3. Начав тренировки, спортсмен в первый день пробежал 10 км. Каждый день он увеличивал свою дневную норму на 10 % от нормы предыдущего дня. Какое общее расстояние преодолеет спортсмен за 7 дней?

k_km=0
km=10
for päev in range (1, 8):
    print(f"{päev}. päev: {km} km")
    k_km+=km
    km=km*0.1+km
    print(f"Kokku jooksed {k_km} km")

#V2 4. Имеется кусок ткани длиной M метров. От него последовательно отрезают куски разной длины. Все данные об использовании ткани вводятся в компьютер. Компьютер должен выдать сообщение о том, что материала недостаточно, если необходимо использовать более длинный кусок ткани, чем тот, который имеется в наличии.

M=float(input("Sisesta konda pikkus:"))
while True:
    k=float(input("Sisesta kuski pikkus:"))
    if k<M:
        print("")
    if k>M:
        print("Materjali ei piisa")
        break
    M-=k
    print(f"Emaaltud kuski pikkus on {k} m. Järel on {M} m materjalid")
    if M==0:
        print ("Materjalid on ostas")
        break
    else:
        print("Jätkame lõikamist")
