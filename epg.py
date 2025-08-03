#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import pathlib
import glob

FOLTIA_DIR = '/mnt/foltia'

# EPG
for p in glob.glob('{}/03-EPG録画/*'.format(FOLTIA_DIR)):
    path = pathlib.Path(p)
    pname = path.name

    ldir = "links/epg/{}".format(pname)
    try:
        os.makedirs(ldir)
    except FileExistsError as e:
        pass

    try:
        os.makedirs("lists/epg")
    except FileExistsError as e:
        pass
    listfilepath = "lists/epg/{}.txt".format(pname)
    listfile = open(listfilepath, "w")
    for f in path.glob('*/MP4-HD/*.MP4'):
        lpname = os.path.join(ldir, os.path.basename(f))
        try:
            os.symlink(f, lpname)
        except FileExistsError as e:
            os.remove(lpname)
            os.symlink(f, lpname)
        listfile.write("{}\n".format(os.path.basename(f)))

    print('rclone copy -L --size-only --files-from="{}" "{}" "365g:/foltia/epg/{}/"'.format(listfilepath, os.path.join(os.getcwd(), ldir), pname))

