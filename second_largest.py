arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)

arr = list(set(arr))

if len(arr) < 2:
    print("No second largest element")
else:
    arr.sort()
    print("Second largest element is:", arr[-2])