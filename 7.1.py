fname= input('Enter a file name:')
fhandle= open(fname)
for line in fhandle:
    line= line.rstrip()
    print(line.upper())
