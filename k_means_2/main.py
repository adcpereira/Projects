import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import math
import copy

RANDOM_DATA = True

#Constants

N = 10000 # Number of points
K = 25 # Number of clusters

X = 1000 # X Axis Length
Y = 1000 # Y Axis Length

P = 10 # Iteration number



FIXED_C_LIST = ['red', 'darkgreen', 'purple', 'darkorange', 'hotpink', 'black', 'yellow']


def color_map():
    n_extra = max(0, K - len(FIXED_C_LIST))
    extra = list(np.random.choice(list(colors.cnames.keys()), size= n_extra))
    return FIXED_C_LIST + extra

COLOR = color_map()

def generate_data():
    if RANDOM_DATA:
        return gen_rand_data(N)


def gen_rand_data(n):
    l_x = np.random.choice((range(X + 1)), size=n)
    l_y = np.random.choice((range(Y + 1)), size=n)
    l   = np.array([l_x, l_y])
    return l


def gen_k_rand():
    return gen_rand_data(K)


def first_plot(data, rand):
    plt.plot(data[0], data[1], 'o', color='blue', label='Initial Points')
    plt.show()
    plt.plot(data[0], data[1], 'o', color = 'blue', label = 'Initial Points')
    for i in range(K):
        plt.plot(rand[0][i], rand[1][i], 'o', c = COLOR[i], ms = 10, markeredgecolor = 'black')
    plt.legend(loc = 0)
    plt.show()

def distance(x1, x2, y1, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def main():
    data_list = generate_data()
    k_points = gen_k_rand()
    first_plot(data_list, k_points)
    data_groups = {}
    r_point_l = []
    for j in range(K):
        point = [k_points[0][j], k_points[1][j]]
        r_point_l.append(point)
        data_groups[j] = [[], []]

    for n in range(P):
        if n != 0:
            l = list(data_groups.values())
            r_point_l_old = copy.copy(r_point_l)
            r_point_l = []
            for j in range(K):
                if len(l[j][0]) != 0:
                    x = np.sum(l[j][0]) / len(l[j][0])
                    y = np.sum(l[j][1]) / len(l[j][1])
                else:
                    x = r_point_l_old[j][0]
                    y = r_point_l_old[j][1]
                point = [x, y]
                r_point_l.append(point)
                data_groups[j] = [[], []]
        for j in range(N): #Associate points with closest r_point
            point_N = np.array([data_list[0][j], data_list[1][j]])
            s = min(r_point_l, key = lambda p: distance(point_N[0], p[0], point_N[1], p[1]))
            s = r_point_l.index(s)
            if n != 0:
                pass
                #print(f"R points - {r_point_l}, Index escolhido - {s}, grupo com as classes {data_groups}")
            list_x_y = data_groups[s]
            list_x_y[0] = np.append(list_x_y[0], point_N[0])
            list_x_y[1] = np.append(list_x_y[1], point_N[1])
            data_groups[s] = list_x_y


        l = list(data_groups.values())
        if n != P - 1:
            for j in range(K):
                if len(l[j][0]) != 0:
                    plt.plot(l[j][0], l[j][1], 'o', c=COLOR[j])
                plt.plot(r_point_l[j][0], r_point_l[j][1], 'o', c=COLOR[j], ms = 10, markeredgecolor = 'black')
        else:
            for j in range(K):
                if len(l[j][0]) != 0:
                    plt.plot(l[j][0], l[j][1], 'o', c=COLOR[j])
        plt.show()







main()