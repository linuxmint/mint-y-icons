#!/usr/bin/python3
import os

# This script uses src.svg and generates svg files for each defined color
# It uses the following color table to do so:

SRC = {"folder":"eeca8f","backfolder":"c89e6b","paper":"e8e8e8","emblem":"575757"}
VARIANTS = []

# Blue
VARIANTS.append({"name":"Blue","folder":"5294e2","backfolder":"4877b1","paper":"e4e4e4","emblem":"1d344f"})
VARIANTS.append({"name":"Aqua","folder":"57b8ec","backfolder":"147eb8","paper":"e4e4e4","emblem":"106796"})
VARIANTS.append({"name":"Teal","folder":"45abb7","backfolder":"35818a","paper":"e4e4e4","emblem":"eaeaea"})
VARIANTS.append({"name":"Green","folder":"50c16f","backfolder":"1f953f","paper":"e4e4e4","emblem":"2f3e1f"})
VARIANTS.append({"name":"Sand","folder":"f9c470","backfolder":"e0a84f","paper":"e4e4e4","emblem":"55524c"})
VARIANTS.append({"name":"Grey","folder":"aaaaaa","backfolder":"727272","paper":"ffffff","emblem":"4f4f4f"})
VARIANTS.append({"name":"Orange","folder":"ff804f","backfolder":"f2632a","paper":"e4e4e4","emblem":"4a4a4a"})
VARIANTS.append({"name": "Red","folder":"f54f54","backfolder":"ca0f14","paper":"e4e4e4","emblem":"4d1c1c"})
VARIANTS.append({"name":"Pink","folder":"f26a9a","backfolder":"cf2f67","paper":"e4e4e4","emblem":"542233"})
VARIANTS.append({"name":"Purple","folder":"a27ae4","backfolder":"7240c3","paper":"e4e4e4","emblem":"2c1e44"})
VARIANTS.append({"name":"Cyan","folder":"00bcd4","backfolder":"0096aa","paper":"e4e4e4","emblem":"00424a"})
VARIANTS.append({"name":"Navy","folder":"b8d8eb","backfolder":"004988","paper":"f4f4f4","emblem":"081f2d"})
VARIANTS.append({"name":"Yaru","folder":"676767","backfolder":"973552","paper":"ff7446","emblem":"e4e4e4"})

for filename in os.listdir("."):
    if filename.endswith(".svg"):
        if filename not in ["extra.svg", "src.svg"]:
            os.remove(filename)

for variant in VARIANTS:
    name = variant["name"]
    os.system(f"cp src.svg {name}.svg")
    for key in SRC.keys():
        src_color = SRC[key]
        color = variant[key]
        if src_color != color:
            os.system("sed -i 's/%s/%s/g' %s.svg" % (src_color, color, name))
