print('입력한 자연수 이하의 모든 소수를 구해냅니다.')
while True:
  try:
    n=int(input('자연수를 입력하십시오: '))
  except ValueError:
    print('\n오류: 자연수를 입력하십시오.\n')
  if n<=0:
    print('\n오류: 자연수를 입력하십시오.\n')
  else:
    break

Nums=[]
for i in range(1, n):
  Nums.append(i+1)

for p in Nums:
  for q in Nums:
    if p!=q and q%p==0:
      Nums.remove(q)
      
print(str(n)+' 이하의 소수는:')
print(*Nums)
print('입니다.')