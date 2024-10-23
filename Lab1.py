# Zadanie 6
def zadanie6():
    x = int(input("Ile masz lat? "))
    print("Masz", x, "lat")


# Zadanie 7
def Zadanie7():
    kierunek_studiow = input("Podaj kierunek studiów: ")
    rok_studiow = input("Podaj rok studiow: ")
    srednia_z_poprzedniego_semestru = float(input("Podaj średnią uzyskaną w poprzednim semestrze studiów: "))
    print(f"Kierunek: {kierunek_studiow}, Rok studiów: {rok_studiow}, Średnia: {srednia_z_poprzedniego_semestru}")


# Zadanie 8
def Zadanie8():
    adres_zamieszkania = input("Podaj adres zamieszkania: ")
    kod_pocztowy = input("Podaj kod pocztowy: ")
    miasto = input("Podaj miasto: ")
    print(f"{adres_zamieszkania},{kod_pocztowy},{miasto}")


# Zadanie 9
def Zadanie9():
    wzrost = int(input("Podaj wzrost w centymetrach: "))
    waga = int(input("Podaj wagę w gramach: "))
    wzrost = wzrost / 100
    waga = waga / 1000
    bmi = waga / wzrost ** 2
    komunikat = ""
    if (bmi < 16):
        komunikat = "wygłodzenie"
    elif (16 <= bmi <= 16.99):
        komunikat = "wychudzenie"
    elif (17 <= bmi <= 18.49):
        komunikat = "niedowaga"
    elif (18.49 <= bmi <= 20.49):
        komunikat = "prawidłowa wartość"
    elif (25.0 <= bmi <= 29.99):
        komunikat = "nadwaga"
    elif (30 <= bmi <= 34.99):
        komunikat = "otyłość pierwszego stopnia"
    elif (35.0 <= bmi <= 39.99):
        komunikat = "otyłość drugiego stopnia"
    elif (bmi >= 40.0):
        komunikat = "otyłość trzeciego stopnia"
    print(f"{komunikat}, Twoje BMI wynosi: {bmi}")


def Zadanie10():
    num = int(input("Podaj liczbę: "))
    print(num > 10)


def Zadanie11():
    num = int(input("Podaj liczbę: "))
    print(10 < num < 20)
    print(num < 0 or num > 20)


if __name__ == '__main__':
    # Zadanie6()
    # Zadanie7()
    # Zadanie8()
    # Zadanie9()
    # Zadanie10()
    Zadanie11()
