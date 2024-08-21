name=input()
lst={}
for i in name:
    if i in lst:
        lst[i]=lst[i]+1
        # print(lst[i])
    else:
        lst[i]=1
    out=max(lst,key=lst.get)
print(out)