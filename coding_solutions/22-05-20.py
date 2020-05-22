list1 = [int(i) for i in input("Enter list").split()] 
print("Missing Number :", sum(range(min(list1),max(list1)+1)) - sum(list1))