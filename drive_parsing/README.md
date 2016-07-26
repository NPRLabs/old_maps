#drivedata_parser.py


###There are 3 ways (two types of files and combination) to use this tool:
```
####MONITOR.XML files
$ python drivedata_parser.py outputfile.csv -m frequency [all files to combine]
#####example:
$ python drivedata_parser.py july29csvs/july29capt.csv -m 88.5 july29/**/MONITOR.XML
```

```
####CAPT*.XML files
$ python drivedata_parser.py outputfile.csv -c frequency [all files to combine]
#####example:
$ python drivedata_parser.py july29csvs/july29capt.csv -c 88.5 july29/**/CAPT*.XML
```

```
####combining csv files (must have same structure)
$ python drivedata_parser.py outputfile.csv --combine [all csv files to combine]
#####example:
$ python drivedata_parser.py fulljuly29.csv --combine july29csvs/*.csv
```
