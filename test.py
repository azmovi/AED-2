def heap_sort(vector):
    heap_build(vector)
    for i in range(len(vector)-1, -1, -1):
        vector[i], vector[0] = vector[0], vector[i]
        heapify(vector[0:i])
    return

def heap_build(vector):
    for i in range(len(vector)//2 - 1, -1, -1):
        heapify(vector, i)
    print(vector)
    return
def heapify(vector, indice = 0):
    maior = indice
    left = 2*indice + 1
    right = 2*indice + 2

    if left < len(vector) and vector[left] > vector[maior]:
        maior = left 
    if right < len(vector) and vector[right] > vector[maior]:
        maior = right

    if maior != indice:
        vector[indice], vector[maior] = vector[maior], vector[indice]
        heapify(vector, maior)
    return

def main():
    vector = [7, 4, 15, 9, -1, 6, 17, 12, 3, 8]
    heap_sort(vector)
    print(vector)
    return


main()
