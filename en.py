import os

def main():
    oss = input(">>>")
    os.system(oss)
    print("kiiratás a konzolra")
    bekeres = input("bekerés a konzolról: ")
    print(f"bekért: {bekeres} ")
    szoveg = "blee"
    egészszám = 123
    egészszámStringbol = int("123")
    tortszam = 13.25
    tortszamstringbol = float("13.25")
    logikai = True
    logikaimasbol = bool([]) #ha üres, 0, none, => False
                             #minden más egyetben => True
                             #Ezzel lehet ellenőrizni hogy vmi. létezik-e
    
    
    bajt = bytes(5)
    print(bajt)

    #collections:
    lista = ["ez", "egy", "primitív", "lista"]
    print(lista)
    lista.append("!")
    print(lista)

    #tuple (csomag) => nem módosíthatóak, indexelhetők, rendezettek, lehet azonos
    csomag = ("elsőelem", "másodikelem", "harmadikelem")
    print(csomag)
    print(csomag[0])

    #halmazok: nem módosítható, indxelhető, rendezettek, lehet azonos

    segédlista = ["alma", "körte", "eper", "alma"]
    halmaz = set(segédlista)
    print(segédlista)
    print(halmaz)


    #dictionary (könyvtár): módosítható de nem indexelhető, nem rendezett, (ver: 3.7 <=) nem lehet azonos

    konyvtar = {
        "Bence" : "ben",
        "péter" : "peti",
        "Marcell" : "marci",
        "dániel" : "dani",
        "noé" : "tól menő a becenévhez",
        "dorián" : "dodo",
        "kirsztián" : "kiki"
    }

    print(f"\n\n{konyvtar} \n")
    print(konyvtar["dániel"])


    """print(egészszámStringbol)
    print(tortszamstringbol)
    print(logikaistringbol)"""




if __name__ == "__main__":
    main()