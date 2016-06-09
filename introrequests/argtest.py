import argparse



parser = argparse.ArgumentParser(description='small tool')


parser.add_argument('which', choices=['tv', 'am', 'fm'])

group = parser.add_mutually_exclusive_group()
group.add_argument('-r', '--reload_from_source', action='store_true')
group.add_argument('-f', '--load_file', default='', dest='filename')

parser.add_argument('-c', '--call_sign', default='', dest='call_sign')

# Tests
failed_count = 0
expected_failed_count = 3

print '\nsuper basic test'
test = parser.parse_args('fm'.split())
print test


print '\nbasic test'
test = parser.parse_args('tv -f my_file'.split())
print test


print '\nmissing which test'
try:
  test = parser.parse_args('-f my_file'.split())
  print test
# this is magic hand wavy catching of a hard exit, blame the argparse api
except SystemExit as err:
  print 'Failed as expected'
  failed_count += 1
  

print '\nchanged order'
test = parser.parse_args('-r tv -c my_callsign'.split())
print test


print '\nchanged order'
test = parser.parse_args('-r -c my_callsign tv'.split())
print test


print '\nall'
test = parser.parse_args('-f my_file --call_sign KFSAD tv'.split())
print test


print '\nno reload, different type'
test = parser.parse_args('-f my_file am --call_sign KFSAD '.split())
print test


print '\nincorrect type'
try:
  test = parser.parse_args('-r -f my_file askd --call_sign KFSAD '.split())
  print test
# this is magic hand wavy catching of a hard exit, blame the argparse api
except SystemExit as err:
  print 'Failed as expected'
  failed_count += 1


print '\nfinal test, need to make sure that -r and -f arent both in use'

try:
  test = parser.parse_args('-r -f my_file tv --call_sign KFSAD '.split())
  print test
# this is magic hand wavy catching of a hard exit, blame the argparse api
except SystemExit as err:
  print 'Failed as expected'
  failed_count += 1




print '\n\nTotal fails {}, Expected:{}'.format(failed_count, expected_failed_count)
print 'Correct' if failed_count == expected_failed_count else 'incorrect'




