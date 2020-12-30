# (a) różne liczby int od 0 do N-1 w kolejności losowej,
import random
import numpy as np


def random_array(n):
    numbers = []
    for i in range(n):
        numbers.append(i)

    random.shuffle(numbers)
    return numbers


def swap(L, left, right):
    """Zamiana miejscami dwóch elementów."""
    L[left], L[right] = L[right], L[left]

# (b) różne liczby int od 0 do N-1 prawie posortowane
# (liczby są blisko swojej prawidłowej pozycji),


def almost_sorted_array(n):
    numbers = []
    for i in range(n):
        numbers.append(i)

    for z in range(5):
        j = random.randint(0, 5)
        for k in range(n):
            left = j
            right = j + random.randint(1, 3)
            if right < n:
                swap(numbers, left, right)
                j += 2

    return numbers


# (c) różne liczby int od 0 do N-1 prawie posortowane w odwrotnej kolejności,


def reversed_almost_sorted_array(n):
    numbers = almost_sorted_array(n)
    numbers.reverse()
    return numbers


# (d) N liczb float w kolejności losowej o rozkładzie gaussowskim,


def random_gaussian_array(n):
    numbers = np.random.normal(0, 0.1, n)
    return numbers


# (e) N liczb int w kolejności losowej, o wartościach powtarzających się,
# należących do zbioru k elementowego (k < N, np. k*k = N).


def random_array_k(n):
    k = np.sqrt(n)
    k = round(k)
    k_array = random_array(k)
    numbers = []

    for i in range(n):
        numbers.append(k_array[random.randint(0, k-1)])
    return numbers


if __name__ == "__main__":
    print(random_array(15))
    print(almost_sorted_array(15))
    print(reversed_almost_sorted_array(15))
    print(random_gaussian_array(15))
    print(random_array_k(15))




