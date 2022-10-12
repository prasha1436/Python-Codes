name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fhandle= open(name)
count= dict()
for l in fhandle:
    if not l.startswith('From '):
        continue
    l=l.rstrip()
    words= l.split()
#    print(line)
    if len(words)< 2:
#        print('skipped 1 line')
        continue
    k= words[5]
    time= k.split(':')
    count[time[0]]= count.get(time[0],0)+1


#print(count)
tmp= list()
for k,v in count.items():
    tmp.append((k,v))

tmp= sorted(tmp)
for i in tmp:
    print(i[0], i[1])
