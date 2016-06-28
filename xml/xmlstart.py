import xml.etree.ElementTree as ET
import datetime as dt
import time
import csv

tree = ET.parse('June23/data1/CAPT00.XML')
root = tree.getroot()

def find_val(root, freq):
    for child in root[1]: # root[1] is the data child
        d = child.attrib # get a dict to easily access the x and y data
        if child.tag == 'DATA' and float(d['x']) == freq: #skip the intro info
            return d['y']

    print "error"
    return 0



if __name__ == '__main__':

    base_folder = 'June23'
    tree = ET.parse('{}/testgpx.gpx'.format(base_folder))
    root = tree.getroot()
    print root.tag + ":"
    
    locs = {}
    for pt in root.iter('trkpt'):
        temp_str = pt[1].text
        
        time_str = temp_str.split('.')[0]
        t = time.strptime(time_str, "%Y-%m-%dT%H:%M:%S")
        lats = pt.attrib
        un = time.mktime(t)
        td1 = dt.timedelta(hours=-3) 
        un += td1.total_seconds()
        if un in locs:
            print "ERROR"
        locs[un] = lats['lat'] + ',' + lats['lon']

    base_folder = 'June23'
    for i in xrange(1, 5):
        tree = ET.parse('{}/activity_{}.tcx'.format(base_folder, str(i)))
        root = tree.getroot()
        print root.tag + ':'
        
        for act in root.iter('Trackpoint'):
            temp_str = act[0].text
            
            time_str = temp_str.split('.')[0]
            t = time.strptime(time_str, "%Y-%m-%dT%H:%M:%S")

            lats = act[1]
            if lats.tag == 'Position':

                lat = lats[0].text
                lon = lats[1].text
                un = time.mktime(t)
                td1 = dt.timedelta(hours=-3) 
                un += td1.total_seconds()
                if un in locs:
                    continue
                locs[un] = lat + ',' + lon
    

    print "NEW TEST:"

    print locs

    csvfile = open('test.csv', 'w')
    names = ['latitude', 'longitude', 'val'] 
    writer = csv.DictWriter(csvfile, fieldnames=names)
    writer.writeheader()
    base_folder = 'June23'
    num_of_files = {'data1':83, 'data2':239}
    for data in ['data1', 'data2']:
        num = 0
        for i in xrange(0, num_of_files[data]):
            tree = ET.parse('{}/{}/CAPT{}.XML'.format(base_folder, data, str(i).zfill(2)))
            root = tree.getroot()
            
            time_str = root.attrib['date'] + ' ' + root.attrib['time']
            t = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
            #print time_str
            t1 = time.mktime(t)
        
            # basically, ignore the ones without locations
            if t1 in locs:
                num += 1
                power = find_val(root, 88.5)
                loc = locs[t1].split(',')
                lat = loc[0]
                lon = loc[1]
                writer.writerow({'val':power, 'latitude':lat, 'longitude':lon})

        print "{}: Found times:{} out of total:{}".format(data, num, num_of_files[data])





#print locs




