op,nm=map(int,input().split())
op=op*pi
for j in range(0,op+1):
 if(j**2==0):
  print("yes")
  break
else:
 print("no")
