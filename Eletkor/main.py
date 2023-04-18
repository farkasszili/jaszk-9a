import tkinter

def feladat(probalkozas):
    eletkor_szoveg = "Adja meg az életkorát:"
    print("Ez a(z) "+str(probalkozas)+". próbálkozásod")
    print(eletkor_szoveg)
    try:
        eletkor = int(input())
    except:
        print("Ez nem szám vagy nem egész szám.")
        return False


    if eletkor < 0:
        print("Ez így nem lesz jó")
        return False

    if eletkor > 110:
        print("Ez így nem lesz jó")
        return False


    print("Ön " + str(eletkor) + " éves.")

    return True

if __name__ == '__main__':
    probalkozas = 0   ##Ez a beviteli próbálkozások száma
    while not feladat(probalkozas):
        probalkozas += 1   ##Növeli a próbálkozások számát
        if (probalkozas > 3):
            print("Inkább hagyjuk.")
            break