
def selection_sort(arr):
    for fill_slot in range(len(arr) - 1, 0, -1):
        position_of_max = 0
        for location in range(1, fill_slot + 1):
            if arr[location] > arr [position_of_max]:
              position_of_max = location

        temp = arr[fill_slot]
        arr[fill_slot] = arr[position_of_max]
        arr[position_of_max] = temp

    return arr

my_array = [4, 92, 1, 39, 19, 93, 49, 10, 99, 103, 13, 102, 32, 345, 145, 4590, 111, 56, 167, 2101]

print(selection_sort(my_array))
