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

#####POSSIBLE Uniqueness:
(appid, hours, da, power) is UNIQUE. There are a few (2) instances where this tuple is NOT unique among entries, but these are errors in the fcc database. Currently, there is only one conflict for (appid, hours, da), but they have different power. Currently ON CONFLICT is set to ignore, as FM services are listed first












