fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
count = 0
fhandle= open(fname)
for line in fhandle:
    if not line.startswith('From '):
        continue
    words= line.split()
#    print(line)
    if len(words)< 2:
#        print('skipped 1 line')
        continue
    print(words[1])
    count= count+1


print("There were", count, "lines in the file with From as the first word")
