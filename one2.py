'''
для проверки:
oone
ooke
oofe
oosq
'''
lines = []
it=[]

while True:
    line = input()
    if line.strip() == "":
        break
    lines.append(line)

for i in range(len(lines)):
    if i != len(lines)-1:
        for ii in range(len(lines)-1):
            if ii !=len(lines):
                kek = lines[i+1:len(lines)]

        for iii in kek:
            dad =  [(first, second) for first,second in zip(lines[i],iii) if first==second]

            if len(dad) == len(lines[i])-1:
                tmp=''.join(map(''.join,dad))
                mas = list(map(str,tmp))

    else:
        break

for m in range(len(mas)-1):
    if m%2==0:
        it.append(mas[m])
print(''.join(map(str,it)))


























