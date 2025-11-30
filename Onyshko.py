def bubble_sort(array):
   
    n = len(array)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if array[j + 1] < array[j]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def selection_sort(array):

    n = len(array)
    for i in range(n - 1, 0, -1):
        maxpos = 0
        for j in range(1, i + 1):
            if array[maxpos] < array[j]:
                maxpos = j
        array[i], array[maxpos] = array[maxpos], array[i]
    return array

def insertion_sort(array):
  
    n = len(array)
    for index in range(1, n):
        currentValue = array[index]
        position = index
        while position > 0:
            if array[position - 1] > currentValue:
                array[position] = array[position - 1]
            else:
                break
            position -= 1
        array[position] = currentValue
    return array
if __name__ == "__main__":
    print (bubble_sort ([5, 3, 1, 4, 2]))