hours= input('no of hours:')
payr= input('pay rate:')
try:
    h= float(hours)
    p= float(payr)
except:
    print('Please enter only numericals')
    quit()

if h < 40:
        gpay= h*p
elif h > 40:
        gpay= 40*p+(h-40)*1.5*p

print('Gross pay is', gpay)
