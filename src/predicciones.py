def prediccion_simple(similarity, neighbours):
    numerator = 0
    denominator = 0
    for i in range(neighbours):
        numerator += (similarity[i][1] * similarity[i][2])
        denominator += abs(similarity[i][1])

    return round(numerator/denominator, 3)

def diferencia_con_media(similarity, neighbours, matrix, u_index):
    u_filtered_values = []
    v_filtered_values = []
    numerator = 0
    denominator = 0

    for i in range(neighbours):
        # Elimina las columnas con incognita
        for j in range(len(matrix[u_index])):
            if matrix[u_index][j] >= 0 and matrix[similarity[i][0]][j] >= 0:
                u_filtered_values.append(matrix[u_index][j])
                v_filtered_values.append(matrix[similarity[i][0]][j])

        # Calcula las medias
        u_average = sum(u_filtered_values) / len(u_filtered_values)
        v_average = sum(v_filtered_values) / len(v_filtered_values)

        # Calcula la diferencia de la media
        numerator += (similarity[i][1] * (similarity[i][2] - v_average))
        denominator += abs(similarity[i][1])
    print()
    return round((u_average + numerator/denominator), 3)
