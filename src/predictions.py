def simple_prediction(similarity, neighbours):
    # Calcula la predicción simple
    numerator = 0
    denominator = 0
    for i in range(neighbours):
        numerator += (similarity[i][1] * similarity[i][2])
        denominator += abs(similarity[i][1])

    return round(numerator/denominator, 3)

def difference_with_average(similarity, neighbours, matrix, u_index):
    u_average = 0
    numerator = 0
    denominator = 0

    # Calculo de la media de u
    long = 0
    for i in range(len(matrix[u_index])):
        if matrix[u_index][j] >= 0:
            u_average += matrix[u_index][j]
            long += 1
    u_average = u_average / long

    for i in range(neighbours):
        # Calcula la media del vecino
        v_average = 0
        long = 0
        for j in range(len(matrix[similarity[i][0]])):
            if matrix[similarity[i][0]][j] >= 0:
                v_average += matrix[similarity[i][0]][j]
                long += 1
        v_average = v_average / long
        
        # Calcula la diferencia de la media
        numerator += (similarity[i][1] * (similarity[i][2] - v_average))
        denominator += abs(similarity[i][1])
    print()
    return round((u_average + numerator/denominator), 3)
