arr1 = [1, 4, 7, 8, 10]
arr2 = [2, 3, 9]
res=[]
# res.extend(arr1)
# res.extend(arr2)
# ans = list(set(res))
# print(ans)

#or

for num in arr1:
  if num not in res:
    res.append(num)
for num in arr2:
  if num not in res:
    res.append(num)
print(sorted(res))