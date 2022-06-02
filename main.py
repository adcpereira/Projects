import numpy as np

import matplotlib.pyplot as plt


N_H = 10   #Rank of Hilbert Matrix

N = 14   # Number of Iterative Steps

EPSILON = 1 #Perturbation in the Aproximation of A_-1

N_G = 10**3


def hilbert(n): #Create a Hilbert Matrix based on the Rank desired
    H_0 = []
    for i in range(1, n+1):
        lista = [1 / (i + j - 1) for j in range(1, n + 1)]
        H_0.append(lista)
    return np.array(H_0, dtype= np.float64)


def norm(M): #Calculate the infinity norm of an Matrix or Vector
    return np.linalg.norm(M, np.inf)

def norm2(M):
    return np.linalg.norm(M)


def cond(M): #Calculate the Condition Number (infinity) of an Matrix
    return norm(M) * norm(np.linalg.inv(M))




def spec_ray(M): #Calculate the spectral ray of a Matrix
    abs_m = np.vectorize(lambda a: abs(a))
    return max(abs_m(np.linalg.eigvals(M)))


def offset_m(M, error): #Return an Matrix (M') that is M'[i, j] = M[i, j] + error
    round_m = np.vectorize(lambda a: a + error)
    return round_m(M)


def r_error(y, x):
    return norm(y - x) / norm(y)

def vec_prod(v, u):
    u = np.transpose(u)
    return np.dot(u, v)



#Base Matrix's


A = hilbert(N_H) #Rank 10 Hilbert Matrix



A_1 = np.linalg.inv(A) #Best direct Aproximation that python is able for the inverse

B = offset_m(A_1, EPSILON)



b = np.ones((N_H, 1))

I = np.identity(N_H, dtype="int")


x = np.array([[-10], [990], [-23760], [240240], [-1261260], [3783780], [-6726720], [7001280], [-3938220], [923780]])
#Solution obtained from Maxima
x_5 = np.array([[5],[-120],[630],[-1120],[630]])

T = I - np.dot(B, A)  # iteractive matrix

#print(spec_ray(I - np.dot(B, A)))

c = np.dot(B, b)



def y_n(n):
    y = np.dot(B, b) #y_0
    if n != 0:
        for k in range(n):
            y = np.dot(T, y) + c
    return y



def plot_y():
    y = np.dot(B, b)  # y_0
    data = []
    data.append(r_error(y, x))
    print(spec_ray(T))
    for k in range(1, N):
        y = np.dot(T, y) + c
        error_r = r_error(y, x)
        data.append(error_r)
        print(error_r)
    plt.title('Relative Error by Iteration')
    plt.xlabel('Iteration Number')
    plt.ylabel('Relative Error')
    plt.plot(range(N), data, 'o', color='blue', label='Initial Points')
    x_ticks = range(N + 1)
    x_labels = range(N + 1)
    plt.xticks(ticks=x_ticks, labels=x_labels)
    plt.yscale('log')
    plt.show()



def plot_cond():
    data = []
    for n in range(1, N_H + 2):
        cond_numb = cond(hilbert(n))
        if n == N_H:
            color_c = 'red'
        else:
            color_c = 'blue'
        plt.xlabel('Hilbert Rank')
        plt.ylabel('Condition Number')
        plt.xticks(ticks=range(1, N_H + 2), labels=range(1, N_H + 2))
        plt.plot(n, cond_numb, 'o', color = color_c)
        plt.yscale('log')
        plt.title("Condition Number of a Hilbert Matrix of Various Ranks")
    plt.show()

def gauss_seidel(A, b):
    U = np.triu(A, k = 1)
    L = np.tril(A, k = 1)
    T_G = -1 * np.dot(np.linalg.inv(L), U)
    C_G = np.dot(np.linalg.inv(L), b)
    y = b
    for k in range(1, 30):
        y = np.dot(T_G, y) + C_G
        print(r_error(y, x))


def gradient_descent(A,b):
    y = b
    data = []
    for k in range(N_G):
        d = -1 * (np.dot(A, y) - b)
        y = y + ((norm2(d) ** 2) / (vec_prod(np.dot(A, d), d))) * d
        if k % 100 == 0:
            error_r = r_error(y, x)
            data.append(error_r)
            print(error_r)
    plt.title('Relative Error by Iteration')
    plt.xlabel('Iteration Number')
    plt.ylabel('Relative Error')
    plt.plot(range(10), data, 'o', color='blue', label='Initial Points')
    x_ticks = range(10)
    x_labels = [100 * i for i in range(10)]
    plt.xticks(ticks=x_ticks, labels=x_labels)
    plt.yscale('log')
    plt.show()


def conjugated_descent(A,b):
    y = b
    data = []
    for k in range(N_H):
        r = -(np.dot(A, y) - b)
        if k == 0:
            d = r
        else:
            d = r - (vec_prod(np.dot(A, r), d)  / vec_prod(np.dot(A, d), d) ) * d
        t = vec_prod(r, d) / vec_prod(np.dot(A, d), d)
        y = y + t * d
        error_r = r_error(y, x)
        data.append(error_r)
        print(error_r)
    plt.title('Relative Error by Iteration')
    plt.xlabel('Iteration Number')
    plt.ylabel('Relative Error')
    plt.plot(range(N_H), data, 'o', color='blue', label='Initial Points')
    x_ticks = range(N_H + 1)
    x_labels = range(N_H + 1)
    plt.xticks(ticks=x_ticks, labels=x_labels)
    plt.yscale('log')
    plt.show()



#gauss_seidel(A, b)

#plot_y()

#plot_cond()

#gradient_descent(A, b)


#conjugated_descent(A, b)