import xml.etree.ElementTree as ET
import datetime as dt
import time
import csv

def find_val(root, freq):
    for child in root.iter('LEVEL'): # root[1] is the data child
        return child.attrib['value']
    for child in root.iter('POWER'): # root[1] is the data child
        return child.attrib['value']

    return 0



if __name__ == '__main__':

    base_folder = 'June29_data'
    tree = ET.parse('{}/1.gpx'.format(base_folder))
    root = tree.getroot()
    print root.tag + ":"
    
    locs = {}
    for pt in root.iter('trkpt'):
        temp_str = pt[1].text
        
        time_str = temp_str.split('.')[0]
        t = time.strptime(time_str, "%Y-%m-%dT%H:%M:%S")
        lats = pt.attrib
        un = time.mktime(t)
        td1 = dt.timedelta(hours=0, seconds=-(t.tm_sec % 3)) 
        un += td1.total_seconds()
        print time.ctime(un)
        print un
        #if un in locs:
        #    print "ERROR"
        locs[un] = lats['lat'] + ',' + lats['lon']

    tree = ET.parse('{}/2.gpx'.format(base_folder))
    root = tree.getroot()
    print root.tag + ":"
    
    for pt in root.iter('trkpt'):
        temp_str = pt[1].text
        
        time_str = temp_str.split('.')[0]
        t = time.strptime(time_str, "%Y-%m-%dT%H:%M:%S")
        lats = pt.attrib
        un = time.mktime(t)
        td1 = dt.timedelta(hours=0, seconds=-(t.tm_sec % 3)) 
        
        un += td1.total_seconds()
        print time.ctime(un)
        print un
        #if un in locs:
        #    print "ERROR"
        locs[un] = lats['lat'] + ',' + lats['lon']


    print "NEW TEST:"


    csvfile = open('june29.csv', 'w')
    names = ['latitude', 'longitude', 'val'] 
    writer = csv.DictWriter(csvfile, fieldnames=names)
    writer.writeheader()
    base_folder = 'June29_data'
    num = 0
    for i in xrange(0, 40):
        tree = ET.parse('{}/{}/CAPT{}.XML'.format(base_folder, 'datas', str(i).zfill(2)))
        root = tree.getroot()
        
        time_str = root.attrib['date'] + ' ' + root.attrib['time']
        t = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        #print time_str
        t1 = time.mktime(t)
        td1 = dt.timedelta(hours=13, seconds=-(t.tm_sec % 3))
        
        t1 += td1.total_seconds()
        print time.ctime(t1)
        print t1

    
        # basically, ignore the ones without locations
        if t1 in locs:
            print "good"
            #print "Good" + time_str
            num += 1
            power = find_val(root, 88.5)
            loc = locs[t1].split(',')
            lat = loc[0]
            lon = loc[1]
            writer.writerow({'val':power, 'latitude':lat, 'longitude':lon})
        else:
            pass
            #print "Bad" + time_str


    print "{}: Found times:{} out of total:{}".format("datas", num, 40)




#print locs




