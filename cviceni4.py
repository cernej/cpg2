class Zvire:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.navstevy = 0

    def __str__(self):
        return f"Zvire(jmeno={self.jmeno}, navstevy={self.navstevy})"

    def inc_navstevy(self):
        self.navstevy += 1

class Pes(Zvire):
    def __init__(self, jmeno, rasa):
        super().__init__(jmeno)
        self.rasa = rasa

    def __str__(self):
        return f"Pes(jmeno={self.jmeno}, rasa={self.rasa}, navstevy={self.navstevy})"

class Kocka(Zvire):
    def __init__(self, jmeno, barva):
        super().__init__(jmeno)
        self.barva = barva
        self.pocet_zivotu = 7

    def __str__(self):
        return f"Kocka(jmeno={self.jmeno}, barva={self.barva}, navstevy={self.navstevy}, zivoty={self.pocet_zivotu})"

    def uber_zivot(self):
        self.pocet_zivotu -= 1

if __name__ == "__main__":
    pes1 = Pes("Alik", "jezevcik")
    pes2 = Pes("Brok", "buldog")
    pes2 = Pes("Max", "vlcak")
    pes1.inc_navstevy()
    print(pes1)
    kocka = Kocka("Mourek", "zrzek")
    kocka.uber_zivot()
    kocka.inc_navstevy()
    print(kocka)