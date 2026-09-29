import numpy as np
import matplotlib.pyplot as plt

# FUNCTIONS
def model(X, U):
    x, v = X.flatten()

    dx = v
    dv = U[0, 0] - 0.5 * v

    return np.array([[dx], [dv]])

def h(X):
    return np.array([[X[0, 0]]])

def guidance(X, Xd):
    x, v = X.flatten()

    ur = 2 * (Xd - x)

    return np.array([[ur]])

def ctrl(X, ur, k_v):
    x, v = X.flatten()

    u = ur[0, 0] - k_v * v

    return np.array([[u]])

# INITIALISATION
# Time variables
tf = 10
dt = 0.01
times = np.arange(0, tf, dt)

# System variables
X = np.array([[0.0], [1.0]])
Y = np.array([[0.0]])
k_v = 2

# Storage vectors
X_vec = np.zeros((2, 0))
Y_d_vec = np.zeros((1, 0))
Y_vec = np.zeros((1, 0))
U_vec = np.zeros((1, 0))


# SIMULATION LOOP
for t in times:

    # Consigne
    Xd = 5.0
    Y_d = np.array([[Xd]])

    # Guidance
    ur = guidance(X, Xd)

    # Control
    U = ctrl(X, ur, k_v)

    # Model
    dX = model(X, U)

    # Explicite Euler integration
    X += dX * dt

    # Output
    Y = h(X)

    # Data storage
    X_vec = np.hstack((X_vec, X))
    Y_vec = np.hstack((Y_vec, Y))
    U_vec = np.hstack((U_vec, U))
    Y_d_vec = np.hstack((Y_d_vec, Y_d))

# PLOTTING RESULTS
# Simulation figure initialization
fig, ax = plt.subplots()

# Position
ax.plot(times, Y_vec[0, :], label='Position')
ax.plot(times, Y_d_vec[0, :], '--', label='Consigne')

ax.set_xlabel('Time (s)')
ax.set_ylabel('Position (m)')
ax.legend()
ax.grid(True)

# Velocity
fig2, ax2 = plt.subplots()

ax2.plot(times, X_vec[1, :], label='Velocity')

ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Velocity (m/s)')
ax2.legend()
ax2.grid(True)

# Control
fig3, ax3 = plt.subplots()

ax3.plot(times, U_vec[0, :], label='Control', color='green')

ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Control input')
ax3.legend()
ax3.grid(True)

plt.show()