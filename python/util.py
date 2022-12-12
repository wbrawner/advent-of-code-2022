def read_input(path):
    with open(path + '.txt', 'r') as input_file:
        return list(map(lambda x: x.strip(), input_file.readlines()))
