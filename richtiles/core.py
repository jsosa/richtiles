#!/usr/bin/env python

# inst: university of bristol
# auth: jeison sosa
# mail: sosa.jeison@gmail.com / j.sosa@bristol.ac.uk

from glob import glob
import gdalutils as gu
import numpy as np


def get_tiles_by_extent(xmin, ymin, xmax, ymax, tilesdir):

    # Reading tiles filenames, assuming they are tif files
    mylist = sorted(glob(tilesdir + '/*.tif'))

    mylist_area = []
    for tile in mylist:
        geo = gu.get_geo(tile)
        if (geo[0] >= xmin) & (geo[1] >= ymin) & (geo[2] <= xmax) & (geo[3] <= ymax):
            mylist_area.append(tile)
    return mylist_area


def write_tiles_layout(mylist, outfile):

    codes = []
    xmins = []
    ymins = []
    for tile in mylist:

        geo = gu.get_geo(tile)
        xmin = np.round(geo[0])
        ymin = np.round(geo[1])
        xmins.append(xmin)
        ymins.append(ymin)
        codes.append(return_code(xmin, ymin))

    xmins = np.unique(np.round(xmins)).astype(int)
    ymins = np.unique(np.round(ymins)).astype(int)
    resx = abs(xmins[0]-xmins[1])
    resy = abs(ymins[1]-ymins[0])

    with open(outfile, 'w') as fout:
        for y in reversed(range(min(ymins), max(ymins)+resy, resy)):
            for x in range(min(xmins), max(xmins)+resx, resx):

                if return_code(x, y) in codes:
                    fout.write(return_code(x, y)+',')
                else:
                    fout.write(' '*7+',')
                    
            fout.write('\n')


def return_code(x, y):

    if x < 0:
        lonstr = 'w%03d' % abs(x)
    elif x >= 0:
        lonstr = 'e%03d' % x

    if y < 0:
        latstr = 's%02d' % abs(y)
    elif y >= 0:
        latstr = 'n%02d' % y

    return latstr+lonstr
