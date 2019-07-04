kl,pi=map(int,input().split())
as=kl*pi
for j in range(0,as+1):
 if(j**2==0):
  print("yes")
  break
else:
 print("no")
