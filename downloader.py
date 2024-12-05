#!/usr/bin/python3

 ##
 # @file    downloader_ghibli.py
 # @brief   
 # @project ghibli wallpaper downloader
 # 
 # @author  Niccolò Pieretti
 # @date    24 set 2020
 # 
 ############################################################################-
 #                                              
 #             _  _   o   __  __   __    _  o   _   ,_    _  
 #            / |/ |  |  /   /    /  \_|/ \_|  |/  /  |  |/  
 #              |  |_/|_/\__/\___/\__/ |__/ |_/|__/   |_/|__/
 #                                    /|                     
 #                                    \|     
 ############################################################################/

import os.path
import urllib.request
from threading import Thread

# Url example:
# http://www.ghibli.jp/gallery/baron007.jpg

basepath = "http://www.ghibli.jp/gallery/"

galleriesData = [
    # gallery name, image name, number of images
    ["redturtle", "redturtle", 50],
    ["onyourmark", "onyourmark", 28],
    ["omoide", "omoide", 50],
    ["laputa", "laputa", 50],
    ["nausicaa", "nausicaa", 50],
    ["tanuki", "tanuki", 50],
    ["umi", "umi", 50],
    ["porco", "porco", 50],
    ["majo", "majo", 50],
    ["totoro", "totoro", 50],
    ["howl", "howl", 50],
    ["baron", "baron", 50],
    ["ghiblies", "ghiblies", 50],
    ["yamada", "yamada", 50],
    ["mononoke", "mononoke", 50],
    ["mimi", "mimi", 50],
    ["marnie", "marnie", 50],
    ["kaguyahime", "kaguyahime", 50],
    ["kazetachinu", "kazetachinu", 50],
    ["kokurikozaka", "kokurikozaka", 50],
    ["karigurashi", "karigurashi", 50],
    ["ponyo", "ponyo", 50],
    ["ged", "ged", 50],
    ["chihiro", "chihiro", 50],
    ["aya", "aya", 50],
    ["kimitachi", "kimitachi", 26],
]

def downloadGallery(gallery):
    for id in range(1, gallery[2] + 1):
        filename = gallery[1] + str(id).zfill(3) + '.jpg'
        if not os.path.exists(filename):
            url = basepath + gallery[0] + str(id).zfill(3) + '.jpg'
            print (url)
            urllib.request.urlretrieve(url, filename)

# Url example:
# http://www.ghibli.jp/images/park1.jpg

wallpaperData = [
    # image name
    "umi1",
    "yamada1",
    "kaze1",
    "red1",
    "omohide1",
    "on-your-mark1",
    "ghiblies1",
    "gedo1",
    "buta1",
    "ponpoko1",
    "neko1",
    "marnie1",
    "totoro1",
    "majyo1",
    "mimi1",
    "kokuriko1",
    "nausicaa1",
    "laputa1",
    "mononoke1",
    "chihiro1",
    "howl1",
    "ponyo1",
    "arietty1",
    "kaguya1",
    "omake1",
    "omake2",
    "park1",
    "park2",
]

def downloadWallpaper():
    basepath = "https://www.ghibli.jp/images/"
    for name in wallpaperData:
        filename = name + '.jpg'
        if not os.path.exists(filename):
            url = basepath + name + '.jpg'
            print (url)
            urllib.request.urlretrieve(url, filename)

for gallery in galleriesData:
    Thread(target=downloadGallery, args=[gallery]).start()
    downloadWallpaper()

