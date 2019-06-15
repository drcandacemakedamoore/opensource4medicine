

import pandas as pd
import os
import shutil
import math
import matplotlib.pyplot as plt
import numpy


def graph_the_lines(file):
    df = pd.read_csv(file)
    df.drop(labels='Observation', axis=1, inplace=True)
    for cname in ['x1', 'y1']:
        df[cname] = df[cname].astype(float)

    #df.dropna(inplace=True)

    df.sort_values('x1', inplace=True)
    #df = df.reset_index(drop=True)

    # import pdb
    # pdb.set_trace()
    mygraph = df.plot(
        yticks=range(0, 30, 5),
        style='.',
        figsize=(30, 20),
        grid=True,
        color= ((0,1,1),(0,1,0), (1,0,0)),
        markersize= 25
    )

    fig = mygraph.get_figure()
 #here it saves into a png; change png title as you wish
    fig.savefig('manasco1.png')

def newkindofplot(file):
    df = pd.read_csv(file)
    ax = df.plot( x='x2', y='y2', style='.', color='olive', markersize=12,)
    df.plot(ax=ax, x='x3', y='y3', style='.', color='blue',  markersize=12, )
    df.plot(ax=ax, x='x4', y='y4', style='.', color='purple',  markersize=12, )
    df.plot(ax=ax, x='x5', y='y5', style='-', color='black',  markersize=12, linewidth=1)
    fig = ax.get_figure()
    fig.savefig('manascombe2r.png')
#here it runs on csv files in the same directory; modify to any csv files set up as example files (to be added)
graph_the_lines('manascomber2.csv')
newkindofplot('manascomber2.csv')
