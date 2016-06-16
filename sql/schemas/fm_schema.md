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

#####POSSIBLE Uniqueness:
appid is UNIQUE. There are a few (2) instances where appid is NOT unique among 
entries, but these are FS services in similar areas. Currently ON CONFLICT is set to ignore, as FM services are listed first













