def read_file(file_path):
    matrix = []
    with open(file_path) as file:
        min_value = float(file.readline())
        max_value = float(file.readline())
        if max_value <= min_value:
            print("El valor mínimo debe ser menor al valor máximo")
            return

        while True:
            line = file.readline()
            if not line:
                break
            splitted_line = line.split()
            values = []
            for value in splitted_line:
                if value == '-':
                    values.append(-1.0)
                else:
                    value = float(value)
                    if value < min_value:
                        print("Se ha detectado un valor en la matriz inferior a", min_value)
                        return
                    if value > max_value:
                        print("Se ha detectado un valor en la matriz superior a", max_value)
                        return
                    values.append(value - min_value)
            matrix.append(values)
    file.close()
    return matrix