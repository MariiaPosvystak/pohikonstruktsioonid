# #15
# print("Ülesanne 15")
# for i in range(10):
#     for i in range(10):
#         print(i, end=" ")
#     print()
# print()

# #10
# print("Ülesanne 10")
# for j in range(10):
#     a1=float(input("Esimene arv: "))
#     a2=float(input("Teine arv: "))
#     if a1>a2:
#         print(f"Suurem on {a1}")
#     elif a2>a1:
#         print(f"Suurem on {a2}")
# print()

#7
print("Ülesanne 7")
A=int(input("Sisesta A:"))
B=int(input("Sisesta B:"))
K=float(input("Sisesta K:"))
for i in range(A,B):
    print(f"{i}")


# #6
# print("Ülesanne 6")
# positiivsed=0
# negatiivsed=0
# null=0
# N=int(input("Sisesta N:"))
# for i in range(N):
#     while True:
#         try:
#             arv=float(input(f"Sisesta {i+1}. arv "))
#             if arv>0:
#                 positiivsed+=1
#             elif arv<0:
#                 negatiivsed+=1
#             elif arv==0:
#                 null+=1
#             else:
#                 print("Kirjuta number")
#             break
#         except:
#             print("Vale formaat")
# print(f"Positiivsed = {positiivsed}")
# print(f"Negatiivsed = {negatiivsed}")
# print(f"Null = {null}")

# #5
# print("Ülesanne 5")
# summa=0
# while True:
#     try:
#         N=int(input("Sisesta N:"))
#         if N>=1:
#             for i in range(1,N+1):
#                 arv=float(input(f"Sisesta {i}. arv: "))
#                 if arv<0:
#                     summa+=arv
#             print(f"Summa võrdub {summa}-ga")
#             break
#         else:
#             print("Arv N peab olema rohkem kui 1")
#     except:
#         print("Vale formaat")

# #4
# print("Ülesanne 4")
# for i in range(10,21,1):
#     print(f"Number ruutu {i} võrdub {i**2}")

# #3
# print("Ülesanne 3")
# kor=1
# for i in range(8):
#     while True:
#         try:
#             arv=float(input(f"Sisesta {i+1} arv "))
#             if arv>=1:
#                kor *= arv
#                print(f"Kor võrdub {kor}-ga")
#                break
#             else:
#                print("Arv A peab olla rohkem kui 1")
#         except:
#              print("Vale formaat")
# print(f"kor kogus: {kor}")
        


# #2
# print("Ülesanne 2")
# summa=0
# while True: 
#     try:
#         A=int(input("Sisesta A: "))
#         if A>1:
#             for i in range(A):
#                 summa+=i
#             print(f"Summa võrdub {summa}-ga")
#             break
#         else:
#             print("Arv A peab olla rohkem kui 1")
#     except:
#         print("Vale formaat")

# #1
# print("Ülesanne 1")
# täisarvud=0
# for i in range(15):
#     while True:
#         try:
#             arv=float(input(f"Sisesta {i+1}. arv "))
#             break
#         except:
#             print("Kirjuta ainult numbrid")
#     if arv==int(arv): täisarvud+=1
# print(f"Täisarvude kogus: {täisarvud}")
