def main():
    print("kiiratas a konzolra")
    bekeres = input("bekeres a konzolrol (a felhasznalotol): ")
    print(f"valtozo ertekenek hasznalata a stringen belul: {bekeres}")
    szoveg = "blee"
    egeszSzam = 123
    egeszSzamStringbol = int("123")
    tortSzam = 13.25
    tortSZamStringbol = float("13.25")
    logikai = True 
    logikaiMasbol = bool([]) # Ha ures, 0, False, vagy None, akkor Falset add vissza,
                             # minden mas esetben True-t
                             # ezzel lehet ellenorizni hogy valami letezik-e
    bajtok = bytes(5)
    # Collections:
    # Lista: modosithato, indexelheto, rendezett, lehetnek azonos elemei
    lista = ["ez", "egy", "primitiv", "lista"]
    # print(lista)
    lista.append("lista")
    # print(lista)
    # Tuple (csomagok): nem modosithatoak, indexelhetoek,
    #                   rendezettek, lehet azonos
    csomag = ("elsoelem", "masodikelem", "harmadikelem")
    # print(csomag)
    # print(csomag[0])
    # Set (halmazok): nem modosithatoak, nem indexelhetoek,
    #                 nem rendezettek, nem lehet azonos
    segedLista = ["alma", "korte", "eper", "alma"]
    halmaz = set(segedLista)
    print(segedLista)
    print(halmaz)
    # Dictionary (konyvtar) : modosithato, nem indexelheto,
    #                         "rendezett" (3.7 <=), nem lehet azonos elem
    konyvtar = {
        "Bence" : "Ben",
        "Péter" : "Peti",
        "Marcell" : "Marci",
        "Dániel" : "Dani",
        "Noé" : "túl menő a becenévhez",
        "Dorián" : "Dodó",
        "Krisztián" : "Krisz"
    }
    print(konyvtar)
    print(konyvtar["Marcell"])
if __name__ == "__main__":
    main()