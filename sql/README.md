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

#####FM
| Name     | TYPE    | Description
| -------- | ------- | --------------------------------------------------------
| id       | INTEGER | unique id, consequence of database design
| callsign | TEXT    | **Mostly** unique sign, some lack a callsign
| freq     | REAL    | Real valued frequency
| service  | TEXT    | type of service, likely only "FM" will matter
| channel  | TEXT    | related to frequency
| da       | TEXT    | whether it is directional, DA or ND are the most common values
| class    | TEXT    | type of station
| status   | TEXT    | status of license
| city, state, country    | TEXT's  | location
| fn       | TEXT    | full station id
| erp[v,h] | REAL    | vertical and horizontal Effective Radiated Power
| haat[v,t]| REAL    | vertical and horizontal HAAT
| fid      | INTEGER | id, many stations have multiple entries
| lat      | REAL    | latitude (in dd form)
| long     | REAL    | latitude (in dd form)
| name     | TEXT    | name of owner
| dmi      | REAL    | TODO AND NEED TO REORDER
| dkm      | REAL    | TODO AND NEED TO REORDER
| ddeg     | REAL    | TODO AND NEED TO REORDER
| rcamsl[v,h]| REAL  | RCAMSL
| daid     | REAL    | directional antenna diagram id, often null
| dapr     | REAL    | see above
| dapr     | REAL    | see above
| h        | REAL    | TODO
| appid    | INTEGER | application id, often same as other stations in one org
| org      | INTEGER | used to mark similar orgs, unused now

TODO UNIQUENESS


#####AM
| Name     | TYPE    | Description
| -------- | ------- | --------------------------------------------------------
| id       | INTEGER | unique id, consequence of database design
| callsign | TEXT    | **Mostly** unique sign, some lack a callsign
| freq     | REAL    | Real valued frequency
| service  | TEXT    | type of service, likely only "FM" will matter
| da       | TEXT    | whether it is directional, DA or ND are the most common values
| hours    | TEXT    | When it operates, DAYTIME/NIGHTIME/?
| usclass  | TEXT    | type of station, US
| iclass   | TEXT    | type of station, International
| status   | TEXT    | status of license
| city, state, country    | TEXT's  | location
| fn       | TEXT    | full station id
| power    | REAL    | Effective Radiated Power
| fid      | INTEGER | id, many stations have multiple entries
| lat      | REAL    | latitude (in dd form)
| long     | REAL    | latitude (in dd form)
| name     | TEXT    | name of owner
| dmi      | REAL    | TODO AND NEED TO REORDER
| dkm      | REAL    | TODO AND NEED TO REORDER
| ddeg     | REAL    | TODO AND NEED TO REORDER
| appid    | INTEGER | application id, often same as other stations in one org
| org      | INTEGER | used to mark similar orgs, unused now

TODO UNIQUENESS

#####TV
| Name     | TYPE    | Description
| -------- | ------- | --------------------------------------------------------
| id       | INTEGER | unique id, consequence of database design
| callsign | TEXT    | **Mostly** unique sign, some lack a callsign
| service  | TEXT    | type of service, likely only "FM" will matter
| channel  | TEXT    | related to frequency
| da       | TEXT    | whether it is directional, DA or ND are the most common values
| freqoff  | REAL    | frequency offset, often null
| tvclass  | TEXT    | tv class
| tvstatus | TEXT    | status of license
| city, state, country    | TEXT's  | location
| fn       | TEXT    | full station id
| erp      | REAL    | Effective Radiated Power
| haat     | REAL    | HAAT
| fid      | INTEGER | id, many stations have multiple entries
| lat      | REAL    | latitude (in dd form)
| long     | REAL    | latitude (in dd form)
| name     | TEXT    | name of owner
| dmi      | REAL    | TODO AND NEED TO REORDER
| dkm      | REAL    | TODO AND NEED TO REORDER
| ddeg     | REAL    | TODO AND NEED TO REORDER
| rcamsl[v,h]| REAL  | RCAMSL
| daid     | REAL    | directional antenna diagram id, often null
| dapr     | REAL    | see above
| dapr     | REAL    | see above
| h        | REAL    | TODO
| appid    | INTEGER | application id, often same as other stations in one org
| virtchan | INTEGER | channel the user sees
| org      | INTEGER | used to mark similar orgs, unused now

TODO UNIQUENESS














