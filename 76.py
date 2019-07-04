mi=int(input())
if(mi>1):
 for i in range(2,mi):
  if(mi%i==0):
   print("yes")
   break
 else:
  print("no")
