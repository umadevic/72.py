kl,pi=map(int,input().split())
nm=kl*pi
for j in range(0,nm+1):
 if(j**2==0):
  print("yes")
  break
else:
 print("no")
