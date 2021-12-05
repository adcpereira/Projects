from MatrixHub import MatrixHub
from fractions import Fraction as Frac

#Commands
EXIT = "exit"
SUM = "sum"
TIMES = "times"


#Print Statments
COMMAND            = "Command: "
HEIGHT             = "Height: "
LENGHT             = "Lenght: "
WRITING_IN_LINE    = "Line {}"
WRITING_IN_COLLUMN = "Collumn {}: "
SAVE_MATRIX        = "Do you wish to save the matrix?"
YER_OR_NO          = "[0] - NO\n[1] - YES"
NAME               = "Name: "
NAME_IN_USE        = "Name {} already in use."
MATRIX_SAVED       = "Matrix \"{}\" saved."
ERROR_DIMENSIONS   = "Matrixes have diferent dimensions."
USE_PREVIOUS_MX    = "Do you wish to use previous matrixes?"
ARROW              = "------> "
MULT_IMPOSSIBLE    = "It's not possible to multiply these two matrixes."


#Main Functions
def sum(m_hub):
    matrix1 = new_matrix(m_hub)
    matrix2 = new_matrix(m_hub)
    if get_dimensions(matrix1) != get_dimensions(matrix2):
        print(ERROR_DIMENSIONS)
    else:
        matrix_soma = []
        for i in range(get_dimensions(matrix1)[0]):
            line = []
            for j in range(get_dimensions(matrix1)[1]):
                line.append(matrix1[i][j] + matrix2[i][j])
            matrix_soma.append(line)
        mtx_print(matrix_soma)
        m_hub.add_temp_matrix(matrix1)
        m_hub.add_temp_matrix(matrix2)
        return matrix_soma

def times(m_hub):
    if m_hub.get_len_list() > 1:
        print(USE_PREVIOUS_MX)
        print(YER_OR_NO)
        option = input(ARROW)
        if option == "1":
            matrix1 = m_hub.get_n_temp_mtx(2)
            matrix2 = m_hub.get_n_temp_mtx(1)
        else:
            matrix1 = new_matrix(m_hub)
            matrix2 = new_matrix(m_hub)
    else:
        """matrix1 = new_matrix(m_hub)
        matrix2 = new_matrix(m_hub)"""
        matrix1 = [[1, 0], [0, 1]]
        matrix2 = [[1, 2], [3, 4]]
    if get_dimensions(matrix1)[1] != get_dimensions(matrix2)[0]:
        print(MULT_IMPOSSIBLE)
    else:
        mtx_mult = []
        h1, l1 = get_dimensions(matrix1)
        h2, l2 = get_dimensions(matrix2)
        for i in range(h1):
            line = []
            for k in range(l1):
                line_matrix1 = matrix1[i]
                line_matrix2 = matrix2[i + k]
                print("oi, 1")
                n = multiply_lists(h1, line_matrix1, line_matrix2)
                print("oi, 2")
                line.append(n)
            mtx_mult.append(line)
        mtx_print(mtx_mult)



def next_command():
    return input(COMMAND)

#Auxiliary Functions

def new_matrix(m_hub):
    h, l = sizes_matrix()
    matrix = []
    for i in range(h):
        line = []
        print(WRITING_IN_LINE.format(i + 1))
        for j in range(l):
            n = input(WRITING_IN_COLLUMN.format(j + 1))
            if "/" in n:
                n, d = process_fraction(n)
                k = Frac(n, d)
            else:
                k = int(n)
            line.append(k)
        matrix.append(line)
    mtx_print(matrix)
    save_matrix(m_hub, matrix, h, l)
    return matrix

def process_fraction(k):
    n = k.index("/")
    return int(k[:n]), int(k[n + 1:])


def sizes_matrix():
    h = int(input(HEIGHT))
    l = int(input(LENGHT))
    return h, l

def save_matrix(m_hub, m, h, l):
    print(SAVE_MATRIX)
    print(YER_OR_NO)
    response = int(input("------->"))
    if response == 0:
        name = input(NAME)
        while name in m_hub.get_names():
            print(NAME_IN_USE.format(name))
            name = input(NAME)
        m_hub.add_matrix(name, m, h, l)
        print(MATRIX_SAVED.format(name))

def mtx_print(l_matrix):
    print("")
    h, l = get_dimensions(l_matrix)
    for i in range(l):
        if i == 0:
            text = "    1"
        else:
            text += "   " + str(i + 1)
    print(text)
    print("  ","-" * l * 4)
    for i in range(h):
        text = ""
        for j in range(l):
            text += str(l_matrix[i][j])
            if j != (l - 1):
                text += "   "
        print(i + 1, "|", text)
    print("")

def get_dimensions(l_matrix):
    h = len(l_matrix)
    l = len(l_matrix[0])
    return h, l

def multiply_lists(n, l1, l2):
    mult_list = []
    for i in range(n):
        mult_list.append(l1[i] * l2[i])
    return sum(mult_list)

def main():
    m_hub = MatrixHub()
    print("What operation do you want to make: ")
    times(m_hub)
    command = next_command()
    while command != EXIT:
        if command == SUM:
            sum(m_hub)
        if command == TIMES:
            times(m_hub)
        command = next_command()

main()