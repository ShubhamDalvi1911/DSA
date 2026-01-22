# Linear Search
def linear_search(arr,item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return -1

def main():
    arr = [12, 33, 22, 5, 89, 44]
    print(linear_search(arr, 44))

if __name__ == "__main__":
    main()