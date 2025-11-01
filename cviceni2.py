def my_range(start, stop, step=1):
    vysledek = []
    hodnota = start
    while hodnota < stop:
        vysledek.append(hodnota)
        hodnota += step
    return vysledek

def my_enumerate(seznam, start=0):
    vysledek = []
    i = 0
    while i < len(seznam):
        vysledek.append((start+i, seznam[i]))
        i += 1
    return vysledek

if __name__ == "__main__":
    print(list(range(1, 10)))
    print(list(range(1, 10, 2)))

    print(my_range(1, 10))
    print(my_range(1, 10, 2))

    print(list(enumerate(["a", "b", "c"])))
    print(list(enumerate(["a", "b", "c"], 1)))

    print(my_enumerate(["a", "b", "c"]))
    print(my_enumerate(["a", "b", "c"], 1))