def pozdrav(jmeno):
    text = f"Ahoj, {jmeno}!"
    return text

def vetsi_nez_tri(cislo):
    if cislo > 3:
        print(f"Cislo {cislo} je vetsi nez 3")
    else:
        print(f"Cislo {cislo} je mensi nebo rovno 3")

# tato funkce overi, zda je cislo delitelne 3,
# pokud ano vypise "je delitelne", pokud ne "neni delitelne"
def delitelne_tremi(cislo):
    if cislo % 3 == 0:
        print("Je delitelne")
    else:
        print("Neni delitelne")

if __name__ == "__main__":

    hodnota = int(input("Zadej cislo: "))
    delitelne_tremi(hodnota)
    
    
