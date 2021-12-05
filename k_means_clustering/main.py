import random
import matplotlib.pyplot as plt
import math
import itertools as it



INT_N = "Introduce the number of points: "
INT_K = "Introduce the number of k-means: "

#Constants
N = 20
COLOR = ['green', 'red', 'yellow', 'blue', 'orange', 'black', 'purple']
MAR_SM = 8
MAR_LAR = 13





def gen_set():
    l = []
    axa = it.product(range(N), repeat = 2)
    axa = list(axa)
    return axa

def creat_p_list(n):
    l = random.choices(gen_set(), k=n)
    lx, ly = p_to_list(l)
    return lx, ly

def list_to_p(lx, ly):
    l = []
    for i in range(len(lx)):
        l.append([lx[i], ly[i]])
    return l

def p_to_list(l):
    lx = []
    ly = []
    for a in l:
        lx.append(a[0])
        ly.append(a[1])
    return lx, ly

def gen_r_p(n):
    r_lx = []
    r_ly = []
    for l in [r_lx, r_ly]:
        for i in range(n):
            rand = random.random()*N
            rand = round(rand, 2)
            l.append(rand)
    return r_lx, r_ly


def dist_p1_p2(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def dist_p1_to_rp(lx, ly, rlx, rly):
    l = []
    for i in range(len(lx)):
        l_aux = []
        pi = (lx[i], ly[i])
        for j in range(len(rlx)):
            rj = (rlx[j], rly[j])
            dis = dist_p1_p2(pi, rj)
            l_aux.append(round(dis, 3))
        m_d = min(l_aux)
        index = l_aux.index(m_d)
        l.append(index)
    return l


def associ_p_to_r(l_code, lx, ly, n):
    dct = {}
    for i in range(n):
        dct[i] = [[],[]]
    for a, px, py in zip(l_code, lx, ly):
        dct[a][0].append(px)
        dct[a][1].append(py)
    return dct

def average_list(l):
    return sum(l)/len(l)


def average_p(dit):
    rlx = []
    rly = []
    for a in dit:
        if dit[a] != [[], []]:
            averx = average_list(dit[a][0])
            avery = average_list(dit[a][1])
            rlx.append(round(averx, 3))
        else:
            rlx.append()
    return rlx, rly



def main():
    n = int(input(INT_N))
    k = int(input(INT_K))
    lx, ly = creat_p_list(n)
    rlx, rly = gen_r_p(k)
    a = plt.plot(lx, ly, 'o', color = 'black', markersize=MAR_SM)
    plt.show()
    a = plt.plot(lx, ly, 'o', color='black', markersize=MAR_SM)
    b = plt.plot(rlx, rly, 'o', markersize=MAR_LAR)
    plt.show()
    l_code = dist_p1_to_rp(lx, ly, rlx, rly)
    dit = associ_p_to_r(l_code, lx, ly, len(rlx))
    for a, co in zip(dit, COLOR[:len(dit)]):
        b = dit[a]
        plt.plot(b[0], b[1],'o' ,color=co, markersize=MAR_SM)
        plt.plot(rlx[a], rly[a], 'o', color=co, markersize=MAR_LAR, markeredgecolor = 'black')
    plt.show()
    """while True:
        rlx, rly = average(dit)

        pass"""


main()
