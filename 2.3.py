hours= input('no of hours:')
payr= input('pay rate:')
try:
    h= float(hours)
    p= float(payr)
except:
    print('Please enter only numericals')
    quit()

gpay= h*p
print('Gross pay is', gpay)
