from DataStructures.array import DynamicArray

a = DynamicArray()
for i in range(10):
    a.append(i)
print(a)
for i in range(3):
    print(a.remove(i), a)