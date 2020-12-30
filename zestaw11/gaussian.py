import zbior_danych as dane
from animate import camera
import matplotlib.pyplot as plt
from insertion_sort import insertsort

if __name__ == "__main__":
    n = 40

    array = dane.random_gaussian_array(n)
    print("random gaussian dist numbers array: ", array)
    print("sorted: ", insertsort(array, 0, n - 1))

    data_size = n

    interval_time = 100
    animation = camera.animate(interval=interval_time)

    plt.show()

