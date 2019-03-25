import rvpy

n = 10
p = 3

X = rvpy.Normal(0, 5)
b = rvpy.CUniform(-10, 10)
e = rvpy.StandardNormal()

Y = X.sample(n, p) @ b.sample(p) + e.sample(n)

print(Y)
