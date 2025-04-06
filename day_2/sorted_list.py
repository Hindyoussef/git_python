elements = [] 
for i in range (5):
  num = int(input(f"enter elments{i+1}" ))
  elements.append(num)

ascending = sorted(elements) 
print(ascending)
descending = sorted(elements,reverse=True)
print(descending)