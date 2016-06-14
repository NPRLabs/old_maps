##Python Tools for making and maintaining and fcc sqlite(3) databases

###Tools and Usage|

####First setup an emtpy db, filaname is fcc.db
```
$ python create_table.py
```

####NEW TOOL HERE

####Filling a table with entries
Can use -o \<filename> to specify a non-'fcc.db' database and
-s \<filename> to specify a non-'data/*_data.txt' downloaded terms
```
$ python fill.py fm
Attempting to insert up to 10000
Attempting to insert up to 20000
Attempting to insert up to 30000
```

####Counting the number of entries in a single table
```
$ python count.py fm
[(37491,)]
```

###Schema Description|

The database consists of three tables, fm, am, and tv, corresponding to each of the 
3 types of signals.

Because there is a difference between data available for each type of signal, each 
one has different columns.

######Links to the full desciption of each table:
[fm](fm_schema.md)

[am](am_schema.md)

[tv](tv_schema.md)













