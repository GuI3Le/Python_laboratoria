import collections
import copy
import random

# Przykłady
prosta = collections.namedtuple("prosta", ["x1", "y1", "x2", "y2"])
p1 = (prosta(2, 3, 4, 5))
p2 = prosta(x1=2, x2=3, y1=4, y2=5)


def zad1():
    print("Zadanie 1")

    def analizujProstokat(x1, y1, x2, y2):
        a = abs(x2 - x1)
        b = abs(y2 - y1)
        pole = a * b
        obwod = 2 * (a + b)
        return pole, obwod

    x1 = 1
    y1 = 2
    x2 = 3
    y2 = 4
    print(analizujProstokat(x1, y1, x2, y2))


def zad2():
    print("Zadanie 2")
    def analizujProstokat(prostokat):
        a = abs(prostokat.x2 - prostokat.x1)
        b = abs(prostokat.y2 - prostokat.y1)
        pole = a * b
        obwod = 2 * (a + b)
        return pole, obwod

    prostokat = collections.namedtuple("prostokat", ["x1", "y1", "x2", "y2"])
    x1 = 1
    y1 = 2
    x2 = 3
    y2 = 4
    prostokat1 = prostokat(x1, y1, x2, y2)

    print(analizujProstokat(prostokat1))

def zad3():
    list1 = list(range(1,1001,2))
    print(list1)

def zad4():
    list1 = list(range(1,10))
    list2 = list1
    # list2[0]=100
    print("Lista1",list1)
    print("Lista2",list2)
    list3 = list1[:]
    list3[0]=100
    print("Lista3",list3)

    list4 = list(list1)
    list4[0] = 100
    list5 = copy.copy(list1)
    list6 = copy.deepcopy(list1)

def zad5():
    list1 = [random.randint(1,10) for _ in range(10)]
    print(list1)
    list2 = [random.random() for _ in range(10)]
    print(list2)
    list3 = list1 +list2
    print(list3)
    print(random.sample(list3,3))
    print(random.choices(list3,k=3))

def zad6():
    print("Zadanie 6")
    # wyświetlanie macierzy print(*d,sep="\n")
    text1 = input("Podaj pierwszy napis: ")
    text2 = input("Podaj drugi napis: ")
    def lavenshtein_distance(text1, text2):
        len1 = len(text1)
        len2 = len(text2)
        d = []
        for i in range(len1+1):
            d.append([0]*(len2+1))
        for i in range(len1+1):
            d[i][0] = i
        for i in range(len2+1):
            d[0][i] = i

        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if text1[i-1] == text2[j-1]:
                    cost = 0
                else:
                    cost = 1
                d[i][j] = min(d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1]+cost )
        return d[len1][len2]


    print(lavenshtein_distance(text1, text2))

if __name__ == '__main__':
    zad1()
    zad2()
    zad3()
    zad4()
    zad5()
    zad6()