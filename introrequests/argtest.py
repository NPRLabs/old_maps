import argparse



parser = argparse.ArgumentParser(description='small tool')


parser.add_argument('which', choices=['tv', 'am', 'fm'])
parser.add_argument('-r', '--reload_from_source', action='store_true')
parser.add_argument('-f', '--load_file', default='', dest='filename')

parser.add_argument('-c', '--call_sign', default='', dest='call_sign')

# Tests

# basic test
test = parser.parse_args('tv -r -f my_file'.split())
print test

















