import re

name = input("Enter file:")
if len(name) < 1:
    name= "actuald_webdata.txt"
fhandle= open(name)
sum= 0
for l in fhandle:
    l = l.rstrip()
    nums= re.findall('[0-9]+', l)
    if len(nums)<1:
        continue
    for num in nums:
        try:
            no= int(num)
            sum= sum + no
            print(nums)
        except:
            continue
print(sum)
