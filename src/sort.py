import numpy as np

def bubble_sort(the_array_to_sort):

    temp_array = the_array_to_sort.copy()
    while sorted(test_array) != temp_array:
        temp_array.random.shuffle 
        for i in range(len(temp_array) - 1):
            if temp_array[i] > temp_array[i + 1]:
                temp_array[i], temp_array[i + 1] = temp_array[i + 1], temp_array[i]
    return temp_array
        

    return[]


if __name__ == "__main__":  # type: ignore
    test_array = np.array([5, 2, 9, 1, 5, 6])
    print(bubble_sort(test_array))