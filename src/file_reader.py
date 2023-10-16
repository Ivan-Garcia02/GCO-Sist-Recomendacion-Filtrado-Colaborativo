def read_file(file_path):
    with open(file_path) as file:
        min_value = float(file.readline())
        max_value = float(file.readline())
        if max_value <= min_value:
            print("El valor máximo debe ser mayor al valor mínimo")
            return

        while True:
            line = file.readline()
            if not line:
                break
    file.close()