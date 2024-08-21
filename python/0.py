def factorial():
   n=int(input("Enter a number:"))
   res=1
   for i in range(n,0,-1):
    res*=i
   print('factorial of',n,'is',res)
s=input("For Exit - 0 /n For continuo - 1")
while(s!=0):

   if(s==1):
      factorial()

factorial() 