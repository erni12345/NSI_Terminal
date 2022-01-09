def power_dac(x, n):
    if n == 1:
        return x
    if n%2 == 0:
        h = power_dac(x, n//2)
        return h * h
    else:
        return x * power_dac(x, n-1)


def power_dac_bad(x, n):
    if n == 1:
        return x
    if n%2 == 0:
        return power_dac_bad(x, n//2) * power_dac_bad(x, n//2)
    else:
        return x * power_dac(x, n-1)


def power_force(x, n):

    for x in range(n):
        x *= x
    return x


import time
import matplotlib.pyplot as plt

def comparaison_temps():
    tps_fb = []
    x = []

    for k in range(5000, 10000):
        x.append(k)
        t0 = time.time()
        power_force(2, k)
        t1 = time.time()
        tps_fb.append(t1-t0)

    tps_dpr = []
    for k in range(5000, 10000):
        t0 = time.time()
        power_dac(2, k)
        t1 = time.time()
        tps_dpr.append(t1-t0)

    plt.plot(x, tps_fb, label = "Force Brute")
    plt.plot(x, tps_dpr, label = "DPR")
    plt.xlabel("exposant")
    plt.legend()
    plt.show()


comparaison_temps()