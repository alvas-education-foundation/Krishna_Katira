def modify(string):  
  final = ""   
  for i in range(len(string)):  
    if i % 2 == 0:  
      final = final + string[i]  
  return final
string=raw_input("Enter string:")
print("Modified string is:")
print(modify(string))
