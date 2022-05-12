from DataStructures.array import DynamicArray

a = DynamicArray()
for i in range(10):
    a.append(i)
print(a)

b = DynamicArray()
for i in range(10):
    b.append((i+1)*(-1))
print(b)

a.extend(b)
print(a)