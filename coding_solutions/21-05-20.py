array = input("Enter array:").split()
k = int(input("Enter K value:"))
print(array[len(array)-k:]+array[:len(array)-k])