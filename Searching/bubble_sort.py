def bubble_sort(arr):
    for i in range(len(arr) - 1):
        flag = 0
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                flag = 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1
        
        if flag == 0:
            break
    print("Sorted array:", arr)

def main():
    arr = [1, 2, 3, 5, 4, 6, 7, 8]
    bubble_sort(arr)

if __name__ == "__main__":
    main() 