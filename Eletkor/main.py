def feladat(probalkozas):

    eletkor_szoveg = "Kérem adja meg az életkorát:"

    print("Ez a(z) " + str(probalkozas) + ". próbálkozásod")
    print("")

    print(eletkor_szoveg)

    ## Egész szám ellenőrzése
    try:
        eletkor = int(input())
    except:
        print("\nEz nem szám vagy nem egész szám!")
        return False

    print("")    ## Egy sor kihagyás, hogy átláthatóbb legyen a felhasználó számára a kimenet.


    ## Életkor ellenőrzése a kritériumok szerint
    if eletkor < 0:
        print("Nem lehet az életkorod 0 év alatt!")
        return False

    if eletkor > 110:
        print("Nem lehet az életkorod 110 év felett!")
        return False



    ## Életkor kiírása
    print("Ön " + str(eletkor) + " éves.")

    return True



if __name__ == '__main__':
    probalkozas = 1   ## Ez a beviteli próbálkozások száma
    while not feladat(probalkozas):
        print("")
        probalkozas += 1   ## Növeli a próbálkozások számát
        if (probalkozas > 3):   ## Maximális próbálkozások ellenőrzése
            print("Meghaladtad a maximális próbálkozások számát!")
            break