servers = int(input())
i=0
ai = []
mul=[]
bi=[]

while i< servers:
	a = int(input())
	b = int(input())
	ai.append(a)
	bi.append(b)
	rr=a*b
	mul.append(rr)
	i+=1

print(mul)
print()
result=sum(mul)

for d in range(servers):
	tmp = bi[d]*ai[d]/result
	print('сервер', d+1, tmp)
