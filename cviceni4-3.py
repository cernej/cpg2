class BankovniUcet:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.__zustatek = 0
    
    def __str__(self):
        return f"Účet({self.jmeno}): {self.__zustatek} kč"

    @property
    def zustatek(self):
        return self.__zustatek

    @zustatek.setter
    def zustatek(self, novy_zustatek):
        if novy_zustatek >= 0:
            self.__zustatek = novy_zustatek

if __name__ == "__main__":
    u = BankovniUcet("spořící")
    print(u.zustatek)
    u.zustatek = -100
    print(u.zustatek)