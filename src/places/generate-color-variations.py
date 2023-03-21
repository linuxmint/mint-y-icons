#!/usr/bin/python3
import os

# This script uses src.svg and generates svg files for each defined color
# It uses the following color table to do so:

SRC = {"folder":"eeca8f","backfolder":"c89e6b","paper":"e4e4e4","line":"92b372","emblem":"575757"}
VARIANTS = []
VARIANTS.append({"name":"Green","folder":"f9c470","backfolder":"e0a84f","paper":"e4e4e4","line":"35a854","emblem":"4a4a4a"})
VARIANTS.append({"name":"Aqua","folder":"f9c470","backfolder":"e0a84f","paper":"e4e4e4","line":"1f9ede","emblem":"4a4a4a"})
VARIANTS.append({"name":"Blue","folder":"f9c470","backfolder":"e0a84f","paper":"e4e4e4","line":"1f9ede","emblem":"4a4a4a"})
VARIANTS.append({"name": "Brown","folder":"f9c470","backfolder":"e0a84f","paper":"e4e4e4","line":"aa876a","emblem":"4a4a4a"})
VARIANTS.append({"name":"Grey","folder":"f9c470","backfolder":"e0a84f","paper":"e4e4e4","line":"70737a","emblem":"4a4a4a"})
VARIANTS.append({"name":"Orange","folder":"f9c470","backfolder":"e0a84f","paper":"e4e4e4","line":"ff7139","emblem":"4a4a4a"})
VARIANTS.append({"name":"Pink","folder":"f06292","backfolder":"ec407a","paper":"e4e4e4","line":"ec407a","emblem":"542233"})
VARIANTS.append({"name":"Purple","folder":"f9c470","backfolder":"e0a84f","paper":"e4e4e4","line":"8c5dd9","emblem":"4a4a4a"})
VARIANTS.append({"name":"Red","folder":"f9c470","backfolder":"e0a84f","paper":"e4e4e4","line":"e82127","emblem":"4a4a4a"})
VARIANTS.append({"name":"Sand","folder":"f9c470","backfolder":"e0a84f","paper":"e4e4e4","line":"c5a07c","emblem":"4a4a4a"})
VARIANTS.append({"name":"Teal","folder":"f9c470","backfolder":"e0a84f","paper":"e4e4e4","line":"199ca8","emblem":"4a4a4a"})

for variant in VARIANTS:
    name = variant["name"]
    os.system(f"cp src.svg {name}.svg")
    for key in SRC.keys():
        src_color = SRC[key]
        color = variant[key]
        if src_color != color:
            os.system("sed -i 's/%s/%s/g' %s.svg" % (src_color, color, name))
