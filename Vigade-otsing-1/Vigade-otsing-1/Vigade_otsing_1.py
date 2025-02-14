import math
print("Ruudu karakteristikud")
try:
    a=float(input("Sisesta ruudu külje pikkus => ")) 
    if a>0: 
        S=a**2 
        print(f"Ruudu pindala", S) 
        P=4*a 
        print(f"Ruudu ümbermõõt", P) 
        di=a*math.sqrt(2) 
        print(f"Ruudu diagonaal", round(di,2)) 
        print() 
    else:
        print("Error, negatiivne arv")
except:
    print("Error,vale tüüp")

print("Ristküliku karakteristikud")
try:
    b=float(input("Sisesta ristküliku 1. külje pikkus => ")) 
    c=float(input("Sisesta ristküliku 2. külje pikkus => "))
    if b>0 and c>0: 
        S=b*c 
        print("Ristküliku pindala", S) 
        P=2*(b+c) 
        print("Ristküliku ümbermõõt", P) 
        di=math.sqrt(b**2+c**2) 
        print("Ristküliku diagonaal", round(di,2)),  
        print()
    else:
        print("Error, negatiivne arv")
except:
    print("Error, vale tüüp")

print("Ringi karakteristikud")
try: 
    r=float(input("Sisesta ringi raadiusi pikkus => "))
    if r>0: 
        d=2*r 
        print("Ringi läbimõõt", d) 
        S=math.pi*r**2 
        print("Ringi pindala", round(S,2)) 
        C=2*math.pi*r 
        print("Ringjoone pikkus", round(C,2))
    else:
        print("Error, negativne arv")
except:
    print ("Error, vale tüüp")
