import os

arr = os.listdir("../data")

print("\n".join(arr))

for (root, dirs, file) in os.walk("C:../data"):
    for f in file:
        print(f)