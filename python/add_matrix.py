x=[[2,3,4],[6,8,6],[2,7,4]]
y=[[9,3,5],[7,3,7],[2,7,5]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j]=x[i][j]+y[i][j]

for r in result:
    print(r)