import xml.etree.ElementTree as ET
import datetime as dt
import time
import csv
import sys

def find_val(root, freq):
    for child in root.iter('LEVEL'): # root[1] is the data child
        return child.attrib['value']
    for child in root.iter('POWER'): # root[1] is the data child
        return child.attrib['value']

    return 0



if __name__ == '__main__':

    print "NEW TEST:"

    csvfile = open(sys.argv[2], 'w')
    names = ['latitude', 'longitude', 'val', 'unixtime'] 
    writer = csv.DictWriter(csvfile, fieldnames=names)
    writer.writeheader()
    tree = ET.parse(sys.argv[1])
    root = tree.getroot()
    
    for cp in root.iter('CPOINT'):
        attribs = cp.attrib
        time_str = attribs['date'] + ' ' + attribs['time']
        t = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        #print time_str
        utime = time.mktime(t)
        lat = cp[0].attrib['latitude']
        lon = cp[0].attrib['longitude']
        power = cp[2][0].attrib['value']

        writer.writerow({'val':power, 'latitude':lat, 'longitude':lon, 'unixtime':utime})






#print locs




