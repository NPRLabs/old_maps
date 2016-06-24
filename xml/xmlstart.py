import xml.etree.ElementTree as ET

tree = ET.parse('June23/data1/CAPT00.XML')
root = tree.getroot()

# from looking at the data, trial and error

for child in root[1]: # root[1] is the data child
    if child.tag == 'DATA': #skip the intro info
        d = child.attrib # get a dict to easily access the x and y data
        print "x:{}, y:{}".format(d['x'], d['y'])
