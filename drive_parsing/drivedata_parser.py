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

def zero_sec(t):
    return 0

def mod2_sec(t):
    return -(t%2)

def parse_tcx(filename, hour_shift, sec_func):
    tree = ET.parse(filename)
    root = tree.getroot()
    locs = {}

    for act in root.iter('Trackpoint'):
        temp_str = act[0].text
        time_str = temp_str.split('.')[0]
        t = time.strptime(time_str, "%Y-%m-%dT%H:%M:%S")
        lats = act[1]
        if lats.tag == 'Position':
            lat = lats[0].text
            lon = lats[1].text
            un = time.mktime(t)
            td1 = dt.timedelta(hours=hour_shift, seconds=sec_func(t.tm_sec))
            un += td1.total_seconds()
            if un in locs:
                continue
            locs[un] = lat + ',' + lon
    return locs

def parse_gpx(filename, hour_shift, sec_func):
    tree = ET.parse(filename)
    root = tree.getroot()

    locs = {}
    for pt in root.iter('trkpt'):
        temp_str = pt[1].text

        time_str = temp_str.split('.')[0]
        t = time.strptime(time_str, "%Y-%m-%dT%H:%M:%S")
        lats = pt.attrib
        un = time.mktime(t)
        td1 = dt.timedelta(hours=hour_shift, seconds=sec_func(t.tm_sec))
        un += td1.total_seconds()
        locs[un] = lats['lat'] + ',' + lats['lon']

    return locs

def parse_capt(filename, writer, test_callsign):
    pass

def parse_mon(filename, writer, test_callsign):
    tree = ET.parse(filename)
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
        writer.writerow({'power':power, 'latitude':lat, 'longitude':lon, 'unixtime':utime, 'callsign':test_callsign})


if __name__ == '__main__':

    with open(sys.argv[1], 'w') as csvfile:
        names = ['latitude', 'longitude', 'val', 'unixtime']
        writer = csv.DictWriter(csvfile, fieldnames=names)
        writer.writeheader()
        if sys.argv[2] == '-c':
            # Capture Data
            locs = {}
            xmls = []
            for filename in sys.argv[4:]:
                if filename.split('.')[1] == '.gpx':
                    locs.update(parse_gpx(filename, 0, mod2_sec))
                elif filename.split('.')[1] == '.tcx':
                    locs.update(parse_tcx(filename, 0, mod2_sec))
                elif filename.split('.')[1].lower() == '.xml':
                    xml.append(filename)
                else:
                    print 'Invalid file extension'
            # now read captures
            for xml_file in xmls:
                parse_capt(xml_file, writer,sys.argv[3])

        elif sys.argv[2] == '-m':
            for filename in sys.argv[4:]:
                parse_mon(filename, writer)

        elif sys.argv[2] == '--combine':
            for filename in sys.argv[3:]:
                with open(filename, 'r') as read_csv:
                    reader = csv.DictReader(read_csv)
                    for row in reader:
                        writer.writerow(row)
