import argparse
import fill
import create_table
import os
import csv_reader
import org_reader

def setup_args():
    parser = argparse.ArgumentParser(description='small tool')


    parser.add_argument('-s', '--load_file', default='', dest='filename')
    group = parser.add_mutually_exclusive_group()
    parser.add_argument('-r', '--restart', action='store_true')
    return parser

if __name__ == '__main__':
    parser = setup_args()
    args = parser.parse_args()



    if args.restart:
        os.remove('fcc.db')
        create_table.create_table()
        outfile = 'fcc.db'
        fill.fill_file('data/fm_data.txt', outfile, 'fm')
        fill.fill_file('data/am_data.txt', outfile, 'am')
        fill.fill_file('data/tv_data.txt', outfile, 'tv')

    csv_reader.cread()
    org_reader.set_orgs()



