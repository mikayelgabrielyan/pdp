first = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

second = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]


for i in range(len(first)):
   for j in range(len(second[0])):
       for k in range(len(second)):
           result[i][j] += first[i][k] * second[k][j]

for r in result:
   print(r)