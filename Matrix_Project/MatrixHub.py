from Matrix_Class import Matrix


class MatrixHub:

    def __init__(self):
        self.matrix_dict = {}
        self.temp_dict = []

    def add_matrix(self, name, l_matrix):
        self.matrix_dict[name] = Matrix(name, l_matrix)

    def get_names(self):
        return self.matrix_dict.keys()

    def add_temp_matrix(self, l_matrix):
        name = len(self.temp_dict)
        self.temp_dict.append(Matrix(name, l_matrix))

    def get_n_temp_mtx(self, n):
        return self.temp_dict[-n]

    def get_len_list(self):
        return len(self.temp_dict)