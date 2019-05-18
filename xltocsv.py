
# convert xl files to csv by command line code of "xltpcsvconvert.py folderwithexcels -o filertoputcsvin"
import pandas as pd
import os

from argparse import ArgumentParser

parser = ArgumentParser('   Converts a list of directories containing MS Excel files into CSV files')
parser.add_argument(
    'xls',
    nargs='+',
    help='Directories containing MS Excel files',
)
parser.add_argument(
    '-o',
    '--output',
    default='.',
    help='Where should the resulting CSV be stored',
)

args = parser.parse_args()
for d in args.xls:
    for f in os.listdir(d):
        res = pd.read_excel(os.path.join(d, f), sheet_name=None)
        if not isinstance(res, dict):
            res = {os.path.splitext(f)[0]: res}
        for k, v in res.items():
            v.to_csv(os.path.join(args.output, k + '.csv'))
