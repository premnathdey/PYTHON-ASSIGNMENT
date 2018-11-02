import re
line =raw_input()
match0bj=re.match(r'(.*) are (.*?) .*', line, re.M|re.I)
if match0bj:
    print "match0bj.groups():", match0bj.group()
    print "match0bj.groups():", match0bj.group()
    print "match0bj.groups():", match0bj.group(1)
    print "match0bj.groups():", match0bj.group(2)
else:
    print "No match!"

search0bj = re.search(r'(.*) are (.*?)..', line, re.M|re.I)

if match0bj:
    print "search0bj.groups():", search0bj.group()
    print "search0bj.groups():", search0bj.group()
    print "search0bj.groups():", search0bj.group(1)
    print "search0bj.groups():", search0bj.group(2)
else:
    print "No match!"

