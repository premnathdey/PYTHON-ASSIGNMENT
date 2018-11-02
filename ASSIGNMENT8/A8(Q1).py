import xml.sax
class DetailHandler( xml.sax.ContentHandler ):
    def __init__(self):
        self.CurrentData = ""
        self.Class = ""
        self.section = ""
        self.age = ""
        self.roll = ""
        self.avg_marks = ""

        # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "student":
            print "***Student details*** "
            name = attributes["name"]
            print "Name: ", name
        # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == "Class":
            print "Class:", self.Class
        elif self.CurrentData == "section":
            print "section:", self.section
        elif self.CurrentData == "age":
            print "age:", self.age
        elif self.CurrentData == "roll":
            print "roll:", self.roll
        elif self.CurrentData == "avg_marks":
            print "avg_marks:", self.avg_marks
        self.CurrentData = ""
    # Call when a character is read
    def characters(self, content):
        if self.CurrentData == "Class":
            self.Class = content
        elif self.CurrentData == "section":
            self.section = content
        elif self.CurrentData == "age":
            self.age = content
        elif self.CurrentData == "roll":
            self.roll = content
        elif self.CurrentData == "avg_marks":
            self.avg_marks = content
if ( __name__ == "__main__"):
    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    # override the default ContextHandler
    Handler = DetailHandler()
    parser.setContentHandler( Handler )
    parser.parse("sample.xml")

