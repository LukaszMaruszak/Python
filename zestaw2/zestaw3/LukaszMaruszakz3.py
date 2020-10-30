# zestaw 3 Autor: Lukasz Maruszak
# zad 3.3

print("zad 3.3 Liczby od 0 do 30 bez liczb podzielnych przez 3")
lista = []
for number in range(31):
    if number % 3 == 0:
        continue
    lista.append(number)

print(lista)

#zad 3.4
print("\nzad 3.4")
print("Wpisz 'stop' żeby przerwać")
while True:
    x = input("Podaj liczę reczywistą: ")

    if x == "stop":
        break

    try:
        float(x)
        print("{} {}".format(x, pow(float(x), 3)))
    except ValueError:
        print("Coś poszło nie tak!!!")

#zad 3.5
print("\nzad 3.5")
dlugosc = int(input("Podaj długość miarki: "))
miarka = "   |"

for i in range(dlugosc):
    miarka = miarka + "...|"

print(miarka)

for x in range(dlugosc+1):
    print("{0:4}".format(x), end="")

#zad 3.6
print("\nzad 3.6")
w = int(input("Podaj ilość wierszy: "))
k = int(input("Podaj ilość kolumn: "))

wiersz = "+"
kolumna = "|"
kratka = ""

for i in range(w):
    wiersz = wiersz + "---+"
    kolumna = kolumna + "   |"
    kratka = (wiersz + "\n" + kolumna + "\n") * k + wiersz

print(kratka)

#zad 3.8

print("\nzad 3.8 ")

sekwencja1 = "programowanie"
sekwencja2 = "modelowanie"

print("Sekwencja pierwsza: " + sekwencja1)
print("Sekwencja druga: " + sekwencja2)
alist = []
listSek = []

for item in sekwencja1:
    if item in sekwencja2:
        if item not in alist:
            alist.append(item)

for item in sekwencja1:
    if item not in listSek:
        listSek.append(item)

for item in sekwencja2:
    if item not in listSek:
        listSek.append(item)

print("Lista elementów występujących jednocześnie w obu sekwencjach to: " + str(alist))
print("Lista wszystkich elementów w obu listach " + str(listSek))

# zad 3.9
list = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
excepted_result = [0, 4, 3, 7, 18]
result = []

for item in list:
    result.append(sum(item))

assert result == excepted_result, "Nie dziala"
print("\nzad 3.9 Lista zawierająca sumę liczb z sekwencji: " + str(result))

# zad 3.10
slownik = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def roman2int(liczbaRzymska):
    return slownik.get(liczbaRzymska)


liczba = input("Podaj liczbę w systemie rzymskim składająca się z jednego znaku: ")
print("Twoja liczba to = " + str(roman2int(liczba)))


def moreroman2int(nRzymska):
    wartosc = 0
    wczesniejszyZnak = 0
    for znak in nRzymska:
        wartosc += slownik.get(znak)
        if slownik.get(znak) > wczesniejszyZnak:
            wartosc = wartosc - wczesniejszyZnak * 2
        wczesniejszyZnak = slownik.get(znak)
    return wartosc


liczba2 = input("\nPodaj liczbę w systemie rzymskim składająca się z wielu znaków: ")
print("Twoja liczba to = " + str(moreroman2int(liczba2)))
