str = 'X-DSPAM- Confidence: 0.8475'
loc = str.find(':')
obj = str[loc+1:]
fobj= float(obj)
print(fobj)