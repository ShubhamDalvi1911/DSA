# Binary Search
def Binary_search(arr,low,high,item):
    if low <= high:
        #search
        mid = (low + high)//2

        if arr[mid] == item:    # compair the item 
            return mid
        elif arr[mid] > item:   # arr[mid] is big than item then it will go to the left side to search
            return Binary_search(arr,low,mid-1,item)
        else:   # arr[mid] is less than item then it will go to the right side to search
            return Binary_search(arr,mid+1,high,item)
    else:
        return -1

def main():
    arr = [11,22,33,44,55,66,77,88,99]
    print(Binary_search(arr,0,len(arr)-1,77))

if __name__ == "__main__":
    main()