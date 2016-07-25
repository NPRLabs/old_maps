import xml.etree.ElementTree as ET
import time
import csv
import json
import sys



def parse_kml_to_dict(string, infile):
    root = None
    if not string and not infile:
        print "NEED FILE OR STRING OF KML"
        return
    if not string:
        tree = ET.parse(infile)
        root = tree.getroot()
    elif not infile:
        try:
            root = ET.fromstring(string)
        except:
            return None

    lis = []
    center = root[0][3]
    lon, lat, z = center[2][0].text.split(',')
    lis.append({"type":"Feature", "id":1, 
                "properties":{"name":center[0].text, "description":center[1].text},
                "geometry":{"type":"Point",
                "coordinates":[float(lon),float(lat), float(z)]}})


    linemark = root[0][5]
    cs = []
    for coords in linemark[3][2].text.splitlines():
        if not coords:
            continue
        splitup = coords.split(',') 
        if len(splitup) < 3:
            continue
        lon, lat, z = splitup
        cs.append([float(lon), float(lat), float(z)])

    lis.append({"type":"Feature", "id":2, 
                "properties":{"name":center[0].text},
                "geometry":{"type":"LineString",
                "coordinates":cs}})

    return {"type":"FeatureCollection", "features":lis}

def write_to_file(d, js_name, outfile, indent=None):

    with open(outfile, 'w') as jfile:
        jfile.write('var {} = \n'.format(js_name))

    with open(outfile, 'a') as jfile:
        json.dump(d, jfile, indent=indent)
        
def write_to_string(d, js_name, indent=None):
    if not d:
        return None

    # if you want to be able to open it
    s = ''
    if js_name:
        s = 'var {} = \n'.format(js_name)

    s += json.dumps(d, indent=indent)
    return s

if __name__ == '__main__':
    write_to_file(parse_kml_to_dict(None, sys.argv[1]), 'main_test', 'main_test_file.js', indent=2)

