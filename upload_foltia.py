#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import pathlib
import glob

FOLTIA_DIR = '/mnt/foltia'

# キーワード録画
for p in glob.glob('{}/04-キーワード録画/*'.format(FOLTIA_DIR)):
    path = pathlib.Path(p)
    pname = path.name
    # ／はgoogle driveでうまく扱えない？
    gpname = pname.replace("／", "-")

    ldir = "links/keyword/{}".format(gpname)
    try:
        os.makedirs(ldir)
    except FileExistsError as e:
        pass

    try:
        os.makedirs("lists/keyword")
    except FileExistsError as e:
        pass
    listfilepath = "lists/keyword/{}.txt".format(gpname)
    listfile = open(listfilepath, "w")
    for f in path.glob('*/*/MP4-HD/*.MP4'):
        lpname = os.path.join(ldir, os.path.basename(f))
        try:
            os.symlink(f, lpname)
        except FileExistsError as e:
            os.remove(lpname)
            os.symlink(f, lpname)
        listfile.write("{}\n".format(os.path.basename(f)))

    print('rclone -v copy -L --size-only --files-from="{}" "{}" "365g:/foltia/keyword/{}/"'.format(listfilepath, os.path.join(os.getcwd(), ldir), gpname))

# アニメ自動録画
for p in glob.glob('{}/02-アニメ自動録画/*/*/*'.format(FOLTIA_DIR)):
    path = pathlib.Path(p)
    pname = path.name

    try:
        os.makedirs("lists/anime")
    except FileExistsError as e:
        pass
    listfilepath = "lists/anime/{}.txt".format(pname)
    listfile = open(listfilepath, "w")
    for f in path.glob('MP4-HD/*.MP4'):
        listfile.write("{}\n".format(pathlib.Path(f).name))

    print('rclone -v copy --size-only --files-from="{}" "{}" "365g:/foltia/anime/{}/"'.format(listfilepath, path / "MP4-HD", pname))
