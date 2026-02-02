import random
from sorting import is_sorted

def mokey_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
        print(arr)
    print("Sorted array:", arr)

a = [5, 3, 2, 8, 1, 4]
mokey_sort(a)