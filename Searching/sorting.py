# Binary Search
def is_sorted(arr):
    sorted = True

    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            sorted = False
    return sorted
   

def main():
    arr = [11,22,33,44,55,66,101,88,99]
    print(is_sorted(arr))

if __name__ == "__main__":
    main()