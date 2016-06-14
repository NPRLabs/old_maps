Quick tests on the sqlite3 api for python

a commit is a transaction so, even if you don't use executemany, you still get "free time"

##Usage:

###First setup an emtpy db
```
python setup.py
```
###Then run the tests
```
time python tests.py onecommit

real  0m0.102s
user  0m0.076s
sys 0m0.004s
```
```
time python tests.py execmany

real  0m0.094s
user  0m0.068s
sys 0m0.004s
```
```
time python tests.py multcommits
# Takes too long
```
