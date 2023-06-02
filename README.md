# jaszk-9a

import pandas

if __name__ == '__main__':
    eleresi_ut = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'
    borok = pandas.read_csv(eleresi_ut, header=None)
    print('hamutartalom: ', borok[2].values)
    print('alkoholtartalom: ', borok[0].values)
    #keresse meg a minimum és a max értékeket
    #állapítoson meg egy határértéket amely az intervallum 10%-a
    #gyűjtse ki az alkoholtartalmát azon boroknak amelyek hamutartalma
    #számoljon átlagot
    #alkoholatratlom átlagot keresünk az alsó 10%ban

