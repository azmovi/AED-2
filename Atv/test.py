from math import floor
def bucket_sort(vetor):
    menor = min(vetor)
    maior = max(vetor)
    amplitude = maior - menor
    size_bucket = round(amplitude/len(vetor))
    baldes = [[] for i in range(len(vetor))]
    for valor in vetor:
        indice = int((((valor - menor) / size_bucket)))
        print(indice)
        baldes[indice].append(valor)
        print(baldes)

    resultado = []
    for balde in baldes:
        resultado += sorted(balde)

    return resultado
vetor = [7, 4, 15, 9, -1, 6, 17, 12, 3, 8]
print(bucket_sort(vetor))
