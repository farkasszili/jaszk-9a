import pandas as pd

if __name__ == '__main__':
    diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
    ##print(diamonds)

    ##print(diamonds['carat'])
    sum = 0

    for i in diamonds['carat']:
        sum += i
    ##print(sum)
    ##print(diamonds['carat'].count())
    darabszam = diamonds['carat'].count()
    atlag = sum / darabszam

    print("Átlag: " + str(atlag))
