import rvpy

X = rvpy.Normal(3, 5)
print(X)

# Normal allows some transformations
print(X - 3) 

Z = (X - 3) / 5

# Also includes a few well-known distribution-to-distribution transformations
print(Z**2) 

# Sampling of an arbitrary number of dimensions allowed
print((Z**2).sample(3, 4))
