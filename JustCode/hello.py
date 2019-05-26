import numpy as np

x = ['k', 'a', 's', 'h', 'i', 'f']
print(x)
y = np.array(x)
print(y[1])

print(np.array([True, 1, 2]) + np.array([3, 4, False]))

myVar = "family"
for c in myVar:
    print(c)

fam = [1.73, 1.68, 1.71, 1.89]
for index, height in enumerate(fam):
    print("person " + str(index) + ": " + str(height))
