def main():
    print("Aritmetikai müveletek:")
    a = 8
    b = 3
    print(f"a: {a}, b: {b}")
    print(f"Osszeadas (a+b):{a+b}")
    print(f"Kivonas (a-b):{a-b}")
    print(f"Szorzás (a*b):{a*b}")
    print(f"Osztás (a/b):{a/b}")
    print(f"LeKerekitett osztás (a//b): {a//b}") # KIHAGYTAM
    print(f"Maradékos osztás (a%b): {a%b}")
    print(f"Hatványozás (a**b): {a**b}")
    print(f"b.-dik gyök (a**(1/b)): {a**(1/b)}")
    
    print("\nLogikai müveletek:")
    c = True
    d = False
    print(f"c: {c}, d: {d}")
    print(f"Nem C (not c): {not c}")
    print(f"C és D (c and d): {c and d}")
    print(f"C vagy D (c or d): {c or d}")

    print("\nÖsszehasonlitó müveletek:")
    print(f"A egyenlő B-vel (a == b): {a == b}")
    print(f"A nem egyenlő B-vel (a != b): {a != b}")
    print(f"A nagyobb B-nél (a > b): {a > b}")
    print(f"A nagyobb vagy egyenlő B-vel  (a >= b): {a >= b}")
    print(f"A kisebb B-nél (a < b): {a < b}")
    print(f"A kisebb vagy egyenlő B-vel  (a <= b): {a <= b}")
    
    print("\nAzonossági műveletek:")
    print(f"A UGYAN AZ MINT B (a is b): {a is b}")
    print(f"A MÁS MINT B (a is not b): {a is not b}")

    # Elágazások:
    if a > b:
        print("A nagyobb mint b")
    elif (a < b):
        print("A kisebb mint b")
    else:
        print("A egyenlő b-vel")
        
if __name__ == "__main__":
    main()