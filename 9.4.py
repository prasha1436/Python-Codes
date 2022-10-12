name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fhandle= open(name)
count= dict()
for l in fhandle:
    l=l.rstrip()
    if not l.startswith('From '):
        continue
    words= l.split()
#    print(line)
    if len(words)< 2:
#        print('skipped 1 line')
        continue
    k= words[1]
    count[k]= count.get(k,0)+1


#print(count)
tmp= list()
for k,v in count.items():
    tmp.append((v,k))

tmp= sorted(tmp, reverse=True)
max= tmp[0]
print(max[1], max[0])
