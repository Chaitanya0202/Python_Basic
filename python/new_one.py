# list=[1,2,3,40,54,40,50,60,22,44,11]
# list1=[54,66665,78,2,"ddd","tt"]
# list.append(5.5)
# list.insert(2,"x")
# list.extend(list1)
# print(list.count(40))
# list.remove(60)
# list.pop()
# list.sort()
# list.reverse()
# list.clear()
# print(max(list))
# print(min(list))
# tup=tuple(list)
# print(list.index(54))
# print(tup)
N = int(input())
L=[]
for i in range(0,N):
    cmd=input().split()
    if cmd[0] == "insert":
        L.insert(int(cmd[1]),int(cmd[2]))
    elif cmd[0] == "append":
        L.append(int(cmd[1]))
    elif cmd[0] == "pop":
        L.pop()
    elif cmd[0] == "print":
        print(L)
    elif cmd[0] == "remove":
        L.remove(int(cmd[1]))
    elif cmd[0] == "sort":
        L.sort()
    else:
        L.reverse()

