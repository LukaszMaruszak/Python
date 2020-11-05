# zad4.2 Lukasz Maruszak

def miarka(d):
    """Funkcja zwraca miarkę o zadanej długości."""
    miarka = "   |"
    for i in range(d):
        miarka = miarka + "...|"

    miarka += "\n"

    for i in range(d+1):
        miarka += str("{0:4}".format(i))

    return miarka


print("zad4.2 Miarka o długosci 12")
print( miarka(12) )

def kratka(w,k):
    """Funkcja wypisuje kratkę o zadanj liczbie wierszy i kolumn."""
    wiersz = "+"
    kolumna = "|"
    kratka = ""

    for i in range(k):
        wiersz = wiersz + "---+"
        kolumna = kolumna + "   |"
        kratka = (wiersz + "\n" + kolumna + "\n") * w + wiersz

    return kratka


print("\nzad4.2 Kratka o 4 kolumnach i 2 wierszach" )
print( kratka(2, 4) )

# zad 4.3


def factorial(n):
    """Finkcja oblicza silnie iteracyjnie."""
    if n == 0:
        return 0
    wynik = 1
    for i in range(1, n+1):
       wynik *= i
    return wynik


print("\nzad4.3 Iteracyjna wersja obliczania silni: 5! = " + str(factorial(5)))


#zad 4.4

def fibonacci(n):
    """Funkcja obliczająca n-ty wyraz ciagu fibinaciego."""
    n1 = 1
    n2 = 1
    if n == 1 or n == 2:
        return 1
    else:
        for i in range(n-2):
            nn = n1 + n2
            n2 = n1
            n1 = nn

    return nn


print("\nzad4.4 Iteracyjne obliczenie n-tego wyrazu ciągu fibonaciego np 15 element to: " + str(fibonacci(15)))


# zad 4.5


def odwracanie(L, left, right):
    """Funkcja do odwracania elementów w liście w zadanym przedziale."""
    if len(L)-1 < right:
        return -1
    else:
        while left < right:
            temp = L[left]
            L[left] = L[right]
            L[right] = temp
            left += 1
            right -= 1
    return L


def odwracanieRek(L, left, right):
    """Rekurencyjna Funkcja odwracania elementów w liście."""
    temp = L[left]
    L[left] = L[right]
    L[right] = temp

    if left < right:
        odwracanieRek(L, left+1, right-1)
    return L


L = [1, 3, 5, 8, 10]
print("\nzad4.5 Iteracyjne odwracanie listy przed: " + str(L) + " po: " + str(odwracanie(L, 0, 4)))
print("zad4.5 Rekurencyjne odwracanie listy przed: " + str(L) + " po: " + str(odwracanieRek(L, 0, 4)))

#zad 4.6


def sum_seq(sequence):
    """Funkcja obliczająca sumę elementów w sekwencji"""
    suma = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            suma += sum_seq(item)
        else:
            suma += item
    return suma


sekwencja = [1, (2, 3), [], [4, [5, 1, [10], 6]]]

print("\nzad4.6 Sekwencja z zagnieżgżonymi sekwencjami to: " + str(sekwencja))
print("\t\tSuma elementów w sekwencji to: " + str(sum_seq(sekwencja)))

#zad4.7


def flatten(sequence):
    """Funkcja spłaszczająca zagnieżdżone sekwencje."""
    splaszczonaSekwencja = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            splaszczonaSekwencja = splaszczonaSekwencja  + flatten(item)
        else:
            splaszczonaSekwencja.append(item)
    return splaszczonaSekwencja


seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print("\nzad4.7 Funkcja do spłaszczania zagnieżdzonych sekwencji.\n\t\tSekwencja do spłaczenia to: " + str(seq))
print("\t\tpo spłaszczeniu: " + str(flatten(seq)))
