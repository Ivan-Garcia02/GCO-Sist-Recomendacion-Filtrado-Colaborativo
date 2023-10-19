import math

def remove_non_common_scores(u_values, v_values):
    u_filtered_values = []
    v_filtered_values = []
    for i in range(len(u_values)):
        if u_values[i] >= 0 and v_values[i] >= 0:
            u_filtered_values.append(u_values[i])
            v_filtered_values.append(v_values[i])

    return u_filtered_values, v_filtered_values

def pearson(u_values, v_values):
    u_values, v_values = remove_non_common_scores(u_values, v_values)

    # Calcula el coeficiente de correlación de Pearson
    u_average = sum(u_values) / len(u_values)
    v_average = sum(v_values) / len(v_values)
    numerator = 0
    u_denominator = 0
    v_denominator = 0
    for i in range(len(u_values)):
        numerator += (u_values[i] - u_average) * (v_values[i] - v_average)
        u_denominator += math.pow((u_values[i] - u_average), 2)
        v_denominator += math.pow((v_values[i] - v_average), 2)

    return round(numerator / (math.sqrt(u_denominator) * math.sqrt(v_denominator)), 10)

def cosine_similarity(u_values, v_values):
    u_values, v_values = remove_non_common_scores(u_values, v_values)

    # Calcula la distancia coseno
    numerator = 0
    u_denominator = 0
    v_denominator = 0
    for i in range(len(u_values)):
        numerator += u_values[i] * v_values[i]
        u_denominator += math.pow((u_values[i]), 2)
        v_denominator += math.pow((v_values[i]), 2)

    return round(numerator / (math.sqrt(u_denominator) * math.sqrt(v_denominator)), 10)

def euclidean_distance(u_values, v_values):
    u_values, v_values = remove_non_common_scores(u_values, v_values)

    # Calcula la distancia euclídea
    summatory = 0
    for i in range(len(u_values)):
        summatory += math.pow(u_values[i] - v_values[i], 2)

    return round(1 / math.sqrt(summatory), 10)