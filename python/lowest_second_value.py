res=[]
score=[]
score_list=[]
for i in range(int(input())):
    name = input()
    score = float(input())
    res=res+[[name,score]]
    score_list+=[score]
    # sortedd=sorted(score_list)
b=sorted(list(set(score_list)))[1] 
print(sorted(res))

for a,c in sorted(res):
    print(a,c)
    if c==b:
        print(a)

# print(res)
# print(score_list)
# print(sortedd)
# print(sortedd[1])

        