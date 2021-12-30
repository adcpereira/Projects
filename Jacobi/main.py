# Initial Setup

JACOBI = TRUE

ERROR = 10 ** (-3)
x01 = 0
x02 = 0
x03 = 0
x04 = 0

T11, T12, T13, T14 = (0, 1 / 3, 0, 0)
T21, T22, T23, T24 = (1 / 3, 0, 1 / 3, 0)
T31, T32, T33, T34 = (0, 1 / 3, 0, 1 / 3)
T41, T42, T43, T44 = (0, 0, 1 / 3, 0)
C1, C2, C3, C4 = (1 / 3, 0, 1 / 3, 1 / 3)

f1 = lambda x1, x2, x3, x4: T11 * x1 + T12 * x2 + T13 * x3 + T14 * x4 + C1
f2 = lambda x1, x2, x3, x4: T21 * x1 + T22 * x2 + T23 * x3 + T24 * x4 + C2
f3 = lambda x1, x2, x3, x4: T31 * x1 + T32 * x2 + T33 * x3 + T34 * x4 + C3
f4 = lambda x1, x2, x3, x4: T41 * x1 + T42 * x2 + T43 * x3 + T44 * x4 + C4


def error(x1, x2, x3, x4, d):
    m = max(abs(x1), abs(x2), abs(x3), abs(x4))
    return d / m


x1 = x2 = x3 = x4 = d = i = 1

while error(x1, x2, x3, x4, d) >= ERROR:
       
    x1 = f1(x01, x02, x03, x04)
    
    if JACOBI:
        x2 = f2(x01, x02, x03, x04)
        x3 = f3(x01, x02, x03, x04)
        x4 = f4(x01, x02, x03, x04)
    
    else:
        x2 = f2(x1, x02, x03, x04)
        x3 = f3(x1, x2, x03, x04)
        x4 = f4(x1, x2, x3, x04)

    d = max(abs(x1 - x01), abs(x2 - x02), abs(x3 - x03), abs(x4 - x04))
    print(f"{i} {x1:.5f} {x2:.5f} {x3:.5f} {x4:.5f} {error(x1, x2, x3, x4, d):.5f}")

    x01, x02, x03, x04 = (x1, x2, x3, x4)
    i += 1
    a = input()
    # if i == 5:
    #   break
