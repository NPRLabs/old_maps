import argparse



parser = argparse.ArgumentParser(description='small tool')


parser.add_argument('which', choices=['tv', 'am', 'fm'])
parser.add_argument('-r', '--reload_from_source', action='store_true')
parser.add_argument('-f', '--load_file', default='', dest='filename')

parser.add_argument('-c', '--call_sign', default='', dest='call_sign')

# Tests

# basic test
test = parser.parse_args('tv -f my_file'.split())
print test


# missing which test
try:
  test = parser.parse_args('-f my_file'.split())
  print test
# this is magic hand wavy catching of a hard exit, blame the argparse api
except SystemExit as err:
  print 'Failed as expected'
  

# changed order
test = parser.parse_args('-r tv -c my_callsign'.split())
print test


# changed order
test = parser.parse_args('-r -c my_callsign tv'.split())
print test


# all 
test = parser.parse_args('-f my_file --call_sign KFSAD tv'.split())
print test


# no reload, different type
test = parser.parse_args('-r -f my_file am --call_sign KFSAD '.split())
print test


# incorrect type
try:
  test = parser.parse_args('-r -f my_file askd --call_sign KFSAD '.split())
  print test
# this is magic hand wavy catching of a hard exit, blame the argparse api
except SystemExit as err:
  print 'Failed as expected'


# final test, need to make sure that -r and -f aren't both use

try:
  test = parser.parse_args('-r -f my_file tv --call_sign KFSAD '.split())
  print test
# this is magic hand wavy catching of a hard exit, blame the argparse api
except SystemExit as err:
  print 'Failed as expected'

