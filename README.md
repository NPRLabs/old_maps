#Top-Level Repo

sqlite tools in [sql](sql)

Downloading and storing (plus querying!) tools in [downloader](downloader)

Downloading and storing (plus querying!) tools in [flask_testing](flask_testing)

TODO
Things to pay attention to:
membership in excel but not in fcc:
WNTI
WKCC
In org as parent but no member status:
KUSC


SWITCH TO USING ROW FACTORY



IDEAS:
Data is currently storing all value in comma separated:

filters and queries are implemented

We need multiple things:

updates:
    new entries: add line, super easy, connect with organization
        organization might just be an organization id, and then have a file that    
        lists the organizations or something like that. maybe too many orgs tho
    update entries: just write over the line in the file, might not work if length
        changes, might need to just rewrite over the file.
        
When we do precomputing (how will it be stored), the data is going to increase significantly, most likely the data will be stored as GeoJson or something similar
    will this be in a separate file? and how will it be linked?
    previous problem was the annoyance of loading a giant jpeg for each spot, but 
    now we are just storing a giant json file? seems inefficient for now, might
    need to think about this
    possibly use a database
        i think the easiest and best to use would be sqllite (under sqllite3 in
        python). its local, file based, and can handle our 'comma-separated + json 
        files structure'
        This is probably what we will end up doing
        need to research about this
        other than that, right now need to make sure python is extensible 
        to that and also work on more filtering and updating and what not
        
        what and HOW to store the information
        
                

Need to think about the flow of updating

1. at some predetermined time, redownload the data ->
2. filter it to contain the data we want this is going to be done on python->
3.1 if using database, then SELECT and UPDATE or INSERT is easy as pie. I think the database makes it really extensible and great
    so this means after the filtering we can select on the identifying information
    for updates and 
    
    
-   most likely the precomputing will be done in a separate module, 
    if not in python, then it can be linked or use process forking and files
    
    
    
Front end: what we do and show on the front endis going to drive what we need on the backend
I think this is where Model-View-Controller is important, but its kindof vague


FIX output of csv and drive parsing, maybe using branches



