#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import pathlib
import glob

FOLTIA_DIR = '/mnt/foltia'

print("set -x")

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

    print('set -x')
    print('echo "{}"'.format(listfilepath))
    print('rclone -v copy -L --checkers 4 --transfers 1 --inplace --size-only --files-from="{}" "{}" "/mnt/xblk/video/keyword/{}/"'.format(listfilepath, os.path.join(os.getcwd(), ldir), gpname))
#    print('rclone -v copy -L --checkers 4 --transfers 1 --inplace --size-only --files-from="{}" "{}" "/mnt/cache/foltia/video/keyword/{}/"'.format(listfilepath, os.path.join(os.getcwd(), ldir), gpname))

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

    print('set -x')
    print('echo "{}"'.format(listfilepath))
    print('rclone -v copy -L --checkers 4 --transfers 1 --inplace --size-only --files-from="{}" "{}" "/mnt/xblk/video/anime/{}/"'.format(listfilepath, path / "MP4-HD", pname))
#    print('rclone -v copy -L --checkers 4 --transfers 1 --inplace --size-only --files-from="{}" "{}" "/mnt/cache/foltia/video/anime/{}/"'.format(listfilepath, path / "MP4-HD", pname))

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

    print('set -x')
    print('echo "{}"'.format(listfilepath))
    print('rclone -v copy -L --checkers 4 --transfers 1 --inplace --size-only --files-from="{}" "{}" "/mnt/xblk/video/epg/{}/"'.format(listfilepath, os.path.join(os.getcwd(), ldir), pname))
#    print('rclone -v copy -L --checkers 4 --transfers 1 --inplace --size-only --files-from="{}" "{}" "/mnt/cache/foltia/video/epg/{}/"'.format(listfilepath, os.path.join(os.getcwd(), ldir), pname))
