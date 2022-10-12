fname= input('Enter a file name:')
fhandle= open(fname)
for line in fhandle:
    words= line.split()
    if not line.startswith('From'):
        continue
    print(line)
    if len(words)< 3:
        print('skipped 1 line')
        continue
    print(words[2])
