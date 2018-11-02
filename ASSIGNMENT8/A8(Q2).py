from xml.dom import minidom
from prettytable import PrettyTable
x=PrettyTable()
x.field_names=["Name","Class","Section","Age","Roll","Avg_marks"]
doc = minidom.parse("sample.xml")
collection = doc.getElementsByTagName("collection")
for s in collection:
        shelf=s.getAttribute("shelf")
        print shelf
student = doc.getElementsByTagName("student")
for s in student:
        name = s.getAttribute("name")
        Class = s.getElementsByTagName("Class")[0]
        section= s.getElementsByTagName("section")[0]
        age= s.getElementsByTagName("age")[0]
        roll= s.getElementsByTagName("roll")[0]
        avg=s.getElementsByTagName("avg_marks")[0]
        x.add_row([name, Class.firstChild.data, section.firstChild.data,age.firstChild.data,roll.firstChild.data,avg.firstChild.data])
print x
