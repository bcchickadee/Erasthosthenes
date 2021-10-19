print('소수 판별기\n제작자: 윤수민')
while True:
  try:
    n=int(input('판별하려는 자연수를 입력하십시오.\n자연수: '))
  except ValueError:
    print('에러: 자연수를 입력하십시오.\n')
  else:
    if n<=0:
      print('에러: 자연수를 입력하십시오.')
    else:
      break

nList=[]
for i in range(1, n):
  nList.append(i+1)

for p in nList:
  for q in nList:
    if p!=q and q%p==0:
      nList.remove(q)

if n in nList:
  print(str(n)+'은(는) 소수입니다.')
else:
  print(str(n)+'은(는) 합성수입니다.')