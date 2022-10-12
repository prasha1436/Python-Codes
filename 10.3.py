fname= input('Enter your file choice:')
fhandle= open(fname, 'r')
count= dict()
for l in fhandle:
    l=l.rstrip()
    words= l.split()
    for k in words:
        count[k]= count.get(k,0)+1


#print(count)
tmp= list()
for k,v in count.items():
    tmp.append((v,k))

tmp= sorted(tmp, reverse=True)
print(tmp[0])
