boy=input().lower()
girl=input().lower()
boy=boy.replace(' ','')
girl=girl.replace(' ','')
for i in boy:
  for j in girl:
    if i==j:
      boy=boy.replace(i,'',1)
      girl=girl.replace(j,'',1)
      break
count=len(boy+girl)
if count>0:
  arr=['Friends','Lovers','Affection','Marraige',"Enemies",'Sibilings']
  while len(arr)>1:
    a=count%len(arr)
    a_index=a-1
    if(a_index>=0):
      left=arr[:a_index]
      right=arr[a_index+1:]
      arr=right+left
    else:
      arr=arr[:len(arr)-1]
print(*arr)
