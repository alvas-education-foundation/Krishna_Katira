y=[('a','16CS045'),('b','16CS320'),('c','16CS057'),('d','16CS100')]
low=int(input("Enter lower roll number (starting with 16CS):"))
up=int(input("Enter upper roll number (starting with 16CS):"))
l='16CS0'+str(low)
u='16CS'+str(up)
p=[x for x in y if x[1]>l and x[1]<u]
print(p)