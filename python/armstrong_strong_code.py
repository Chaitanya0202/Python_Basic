# One Of The Best Till Now
num=int(input())
order=len(str(num))
temp=num
sum=0
for i in range(1,temp):
  digit=temp%10
  sum+=digit**order
  temp//=10
if sum==num:
  print("Armstrong")
else:
  print("Not Armstrong")
# Find The Armstrong Number In Interval 900 to 1000
# Uncomplete
# sum=0
# for num in range(104,154):
#   temp=num
#   while temp > 0 :
#     order=len(str(num))
#     digit=temp%10
#     sum+=digit**order
#     temp//=10
#     if sum==num:
#       print(num)
    # else:
    #   continue



