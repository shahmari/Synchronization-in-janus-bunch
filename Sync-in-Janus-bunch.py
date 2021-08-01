import numpy as np
import matplotlib.pyplot as plt
import math
from numpy import random


def diff_eqs(f, n):
    Y = np.zeros(2)
    if n != N-1:
        Y[0] = omega[0] + beta * \
            math.sin(f[n][1]-f[n][0]) + sigma * math.sin(f[n+1][1] - f[n][0])
        Y[1] = omega[1] + beta * \
            math.sin(f[n][0]-f[n][1]) + sigma * math.sin(f[n-1][0] - f[n][1])
    else:
        Y[0] = omega[0] + beta * \
            math.sin(f[n][1]-f[n][0]) + sigma * math.sin(f[0][1] - f[n][0])
        Y[1] = omega[1] + beta * \
            math.sin(f[n][0]-f[n][1]) + sigma * math.sin(f[n-1][0] - f[n][1])
    return Y


def solve_diffeqs(N, sigma, beta, omega, ND, dt):
    NT = int(ND/dt)
    INP = random.uniform(low=0, high=2*np.pi, size=(N, 2))
    RES = np.zeros((NT, N, 2))
    Phase = np.zeros((NT, N, 2))
    for i in range(NT):
        INP_Copy = INP
        for j in range(N):
            INP[j] += dt*diff_eqs(INP_Copy, j)
            Phase[i][j] = diff_eqs(INP_Copy, j)
        RES[i] = INP_Copy

    return (RES, Phase)


omega = np.array([-1/2, 1/2])
beta = 1/4
sigma = 1
N = 16
ND = 30
dt = 0.01
T_list = np.linspace(0, ND, num=int(ND/dt))
(res, phase) = solve_diffeqs(N, sigma, beta, omega, ND, dt)

plt.figure(figsize=(10, 7), dpi=100)
plt.grid(color='k', linestyle='--', linewidth=0.5)
for i in range(N):
    plt.plot(T_list, res[:, i, 0], label='Oscillator Number={i}')
plt.xlabel('Time(sec)')
plt.ylabel('θ(t)')
#plt.legend(loc=1)
plt.savefig('1')
plt.show()

plt.figure(figsize=(10, 7), dpi=100)
plt.grid(color='k', linestyle='--', linewidth=0.5)
for i in range(N):
    plt.plot(T_list, res[:, i, 1], label='Oscillator Number={i}')
plt.xlabel('Time(sec)')
plt.ylabel('φ(t)')
plt.savefig('2')
#plt.legend(loc=1)
plt.show()

plt.figure(figsize=(10, 7), dpi=100)
plt.grid(color='k', linestyle='--', linewidth=0.5)
for i in range(N):
    plt.plot(T_list, phase[:, i, 0], label='Oscillator Number={i}')
plt.xlabel('Time(sec)')
plt.ylabel("θ'(t)")
#plt.legend(loc=0)
plt.savefig('3')
plt.show()

plt.figure(figsize=(10, 7), dpi=100)
plt.grid(color='k', linestyle='--', linewidth=0.5)
for i in range(N):
    plt.plot(T_list, phase[:, i, 1], label='Oscillator Number={i}')
plt.xlabel('Time(sec)')
plt.ylabel("φ'(t)")
#plt.legend(loc=0)
plt.savefig('4')
plt.show()
