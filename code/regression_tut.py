import numpy as np, matplotlib
matplotlib.use('qt4Agg')
mport matplotlib.pyplot as plt

# Straight line
m = np.random.random() * 10
c = np.random.random() * 10

x = np.linspace(1, 100, 120)
y = m * x + c

plt.axis((0, 100, 0, 100))
plt.plot(x, y, 'r.')
plt.show()


# Let's add some noise to the data

w = np.mean(y/x)

plt.axis((-10, 100, -10, 100))
plt.plot(x, y, 'r.')
plt.axis((-10, 100, -10, 100))
plt.plot(x, w*x, 'b.')
plt.show()

y = m * x + c
x = np.linspace(1, 100, 120)
y += 10 * np.random.randn(len(y))

w = 5 * np.random.random()
b = 5 * np.random.random()

x_ = np.asarray(list(zip(x, np.ones_like(x))))
beta = np.asarray([w, b])

deltas = np.ones_like(x)
plt.axis((-10, 100, -10, 100))
plt.plot(x, y, 'r.')
plt.axis((-10, 100, -10, 100))
plt.plot(x, w*x, 'b-')
plt.show()

while(np.abs(np.mean(deltas)) > 1e-03):
    for i in zip(y, x_):
        deltas[j] = 0.0001 * (i[0] - i[1] * beta[0]) * i[1]
    beta[0] += np.mean(deltas)
    print(w, np.mean(deltas))
    plt.axis((-10, 100, -10, 100))
    plt.plot(x, y, 'r.')
    plt.axis((-10, 100, -10, 100))
    plt.plot(x, w*x, 'b.')
    plt.show()

print(np.sum(1/2 * (y - w*x) ** 2))


# vector notation
deltas = np.ones((2,))
lr = 0.0001

# w = 5 * np.random.random()
# b = 5 * np.random.random()

# beta = np.asarray([w, b])
beta = np.asarray([2, 1])
x_ = np.asarray(list(zip(x, np.ones_like(x))))

while(np.abs(np.mean(deltas)) > 0.0001):
    deltas[0] = lr * np.mean((y - np.dot(x_, beta)) * x_[:,0])
    deltas[1] = lr * np.mean(y - np.dot(x_, beta))
    beta += deltas
    print(deltas)
    plt.axis((-10, 100, -10, 100))
    plt.plot(x, y, 'r.')
    plt.axis((-10, 100, -10, 100))
    plt.plot(x, np.dot(x_, beta), 'b-')
    plt.show()
