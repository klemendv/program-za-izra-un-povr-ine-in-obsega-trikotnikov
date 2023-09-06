def izracun_povrsine():
    a = float(input("Vnesite dolžino prve stranice trikotnika: "))
    b = float(input("Vnesite dolžino druge stranice trikotnika: "))
    h = float(input("Vnesite višino trikotnika: "))

    povrsina = 0.5 * a * h
    return povrsina

def izracun_obsega():
    a = float(input("Vnesite dolžino prve stranice trikotnika: "))
    b = float(input("Vnesite dolžino druge stranice trikotnika: "))
    c = float(input("Vnesite dolžino tretje stranice trikotnika: "))

    obseg = a + b + c
    return obseg

while True:
    print("Izberite eno od možnosti:")
    print("1. Izračun površine trikotnika")
    print("2. Izračun obsega trikotnika")
    print("3. Izhod")
    
    izbira = input("Vaša izbira (1/2/3): ")
    
    if izbira == "1":
        povrsina = izracun_povrsine()
        print(f"Površina trikotnika je {povrsina}")
    elif izbira == "2":
        obseg = izracun_obsega()
        print(f"Obseg trikotnika je {obseg}")
    elif izbira == "3":
        break
    else:
        print("Neveljavna izbira. Prosimo, izberite 1, 2 ali 3.")
