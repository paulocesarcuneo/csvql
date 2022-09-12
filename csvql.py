#!/usr/bin/env python
import stat, os, re, sys, argparse
import pandas as pd
import duckdb

parser = argparse.ArgumentParser(description= "Run sql query over csv files in current working directory",
                                 epilog='''
Example:
 $ ls -1 # given csv file in folder
  jobs.csv
  persons.csv
 $ csvql 'select * from persons p join jobs j on j.email = p.email'

''',
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('query', type=str, help='sql query')
parser.add_argument('-i', nargs='?', help='print index',const=True)


args = parser.parse_args()

con = duckdb.connect(database=':memory:')
tables = {};
for file in os.listdir():
    csv = re.search("^([^.]+).csv$",file)
    if csv is not None:
        df = pd.read_csv(csv.group(0))
        tables[csv.group(1)]= df 
        con.register(csv.group(1), df)

# con.execute('select * from persons p join jobs j on j.email = p.email ')
con.execute(args.query)
res = con.fetchdf()

if stat.S_ISFIFO(os.fstat(sys.stdout.fileno()).st_mode):
    res.to_csv(sys.stdout, index=args.i)
else:
    print(res.to_string(index=args.i))
