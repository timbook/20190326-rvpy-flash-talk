import rvpy
import matplotlib.pyplot as plt

X = rvpy.Laplace(0, 1)
Y = X + 5

n = 10000

plt.hist(
    X.sample(n),
    bins=50,
    edgecolor='#204A87',
    color='#204A87',
    alpha=0.9,
    label="X = Laplace(0, 1)"
)

plt.hist(
    Y.sample(n),
    bins=50,
    edgecolor='#CE5C00',
    color='#CE5C00',
    alpha=0.9,
    label="Y = X + 5"
)

plt.legend()

plt.savefig('./laplace-hists.png', dpi=192)
