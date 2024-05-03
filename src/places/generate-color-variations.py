#!/usr/bin/python3
import os

# This script uses src.svg and generates svg files for each defined color
# It uses the following color table to do so:

SRC = {"folder":"eeca8f","backfolder":"c89e6b","paper":"e8e8e8","emblem":"575757", "system-file-manager-back": "eab768"}

VARIANTS = []
VARIANTS.append({"name":"Blue","folder":"5294e2","backfolder":"4877b1","paper":"e4e4e4","emblem":"1d344f", "system-file-manager-back": "3f4756"})
VARIANTS.append({"name":"Aqua","folder":"57b8ec","backfolder":"147eb8","paper":"e4e4e4","emblem":"106796", "system-file-manager-back": "374955"})
VARIANTS.append({"name":"Teal","folder":"45abb7","backfolder":"35818a","paper":"e4e4e4","emblem":"eaeaea", "system-file-manager-back": "324b4e"})
VARIANTS.append({"name":"Green","folder":"50c16f","backfolder":"1f953f","paper":"e4e4e4","emblem":"2f3e1f", "system-file-manager-back": "3c4a3e"})
VARIANTS.append({"name":"Sand","folder":"f9c470","backfolder":"e0a84f","paper":"e4e4e4","emblem":"4a4a4a", "system-file-manager-back": "4f4538"})
VARIANTS.append({"name":"Grey","folder":"aaaaaa","backfolder":"727272","paper":"ffffff","emblem":"4f4f4f", "system-file-manager-back": "474554"})
VARIANTS.append({"name":"Orange","folder":"ff804f","backfolder":"f2632a","paper":"e4e4e4","emblem":"4a4a4a", "system-file-manager-back": "55433c"})
VARIANTS.append({"name": "Red","folder":"f54f54","backfolder":"ca0f14","paper":"e4e4e4","emblem":"4d1c1c", "system-file-manager-back": "574240"})
VARIANTS.append({"name":"Pink","folder":"f26a9a","backfolder":"cf2f67","paper":"e4e4e4","emblem":"542233", "system-file-manager-back": "564147"})
VARIANTS.append({"name":"Purple","folder":"a27ae4","backfolder":"7240c3","paper":"e4e4e4","emblem":"2c1e44", "system-file-manager-back": "4b4453"})
VARIANTS.append({"name":"Cyan","folder":"00bcd4","backfolder":"0096aa","paper":"e4e4e4","emblem":"00424a", "system-file-manager-back": "324b50"})
VARIANTS.append({"name":"Navy","folder":"b8d8eb","backfolder":"004988","paper":"f4f4f4","emblem":"081f2d", "system-file-manager-back": "364954"})
VARIANTS.append({"name":"Yaru","folder":"676767","backfolder":"973552","paper":"ff7446","emblem":"e4e4e4", "system-file-manager-back": "474554"})

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
