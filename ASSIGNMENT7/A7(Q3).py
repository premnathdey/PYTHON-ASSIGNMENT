import re
mylist=[]
print sorted([entry for entry in dir(re) if re.search('find', entry)])