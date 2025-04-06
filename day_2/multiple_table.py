# multiplication table lists  
num = int(input("enter a number: "))
output_list=[]
for i in range(1, num+ 1):
  output_list.append([i*j for j in range(1,i+1)])
print(output_list)