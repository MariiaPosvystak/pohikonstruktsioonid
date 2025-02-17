#3
summa=1
while True: 
    try:
        A=int(input("Sisesta A: "))
        if A>1:
            for i in range(A):
                summa+=i
            print(f"Summa võrdub {summa}-ga")
            break
        else:
            print("Arv A peab olla rohkem kui 1")
    except:
        print("Vale formaat")


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
