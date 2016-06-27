import xml.etree.ElementTree as ET

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
    num_of_files = {'data1':82, 'data2':238}
    for data in ['data1', 'data2']:
        for i in xrange(0, num_of_files[data] + 1):
            tree = ET.parse('{}/{}/CAPT{}.XML'.format(base_folder, data, str(i).zfill(2)))
            root = tree.getroot()

            print find_val(root, 88.5)

