def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid_index = 0
    upper_bound = arr[-1]

    if len(arr) < 3 or upper_bound < x:
        return None

    steps = 1
    while low <= high:
        mid_index = (high + low) // 2

        if x <= arr[mid_index] and x > arr[mid_index - 1]:
            return (steps, arr[mid_index])

        steps += 1

        if x < arr[mid_index]:
            high = mid_index - 1
        elif x > arr[mid_index]:
            low = mid_index + 1        

        
    return None


if __name__ == '__main__':
    arr = [-23, -11.5, -4.3, 1.1, 3.2, 4.9, 5.5, 7.4, 10.1, 12.3, 13, 14.6, 16.9, 16.98, 17.05, 20.1, 22.5, 25.25]
    x = -4.2

    result = binary_search(arr, x)

    if result is None:
        print("Element is not present in array")
    else:
        print("Element is present at index", str(result))
