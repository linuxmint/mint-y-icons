#!/usr/bin/python3
import os

# This script uses src.svg and generates svg files for each defined color
# It uses the following color table to do so:

SRC = {"folder":"eeca8f","backfolder":"c89e6b","paper":"e8e8e8","line":"92b372","emblem":"575757"}
VARIANTS = []

# Blue
VARIANTS.append({"name":"Blue","folder":"5294e2","backfolder":"4877b1","paper":"e4e4e4","line":"5294e2","emblem":"1d344f"})

# Aqua
VARIANTS.append({"name":"AquaVera","folder":"f9c470","backfolder":"e0a84f","paper":"e4e4e4","line":"f9c470","emblem":"4a4a4a"})
VARIANTS.append({"name":"Aqua","folder":"f9c470","backfolder":"e0a84f","paper":"e4e4e4","line":"1f9ede","emblem":"4a4a4a"})
VARIANTS.append({"name":"AquaBreeze","folder":"57b8ec","backfolder":"147eb8","paper":"e4e4e4","line":"57b8ec","emblem":"106796"})
VARIANTS.append({"name":"AquaGulf","folder":"b8d8eb","backfolder":"004988","paper":"f4f4f4","line":"ff671d","emblem":"081f2d"})

# Teal
VARIANTS.append({"name":"TealCyan","folder":"00bcd4","backfolder":"0096aa","paper":"e4e4e4","line":"00bcd4","emblem":"00424a"})
VARIANTS.append({"name":"TealDarkcyan","folder":"45abb7","backfolder":"35818a","paper":"e4e4e4","line":"45abb7","emblem":"eaeaea"})
VARIANTS.append({"name":"TealNordic","folder":"82abaa","backfolder":"6c9b9a","paper":"e4e4e4","line":"82abaa","emblem":"4e6766"})
VARIANTS.append({"name":"Teal","folder":"35b9ab","backfolder":"12806a","paper":"e4e4e4","line":"35b9ab","emblem":"173e4f"})
VARIANTS.append({"name":"TealSuse","folder":"183f50","backfolder":"00a489","paper":"e4e4e4","line":"183f50","emblem":"73b924"})

# Green bof
VARIANTS.append({"name":"Green","folder":"87b158","backfolder":"00a388","paper":"e4e4e4","line":"87b158","emblem":"2f3e1f"})

# Sand
VARIANTS.append({"name":"Sand","folder":"aa876a","backfolder":"957552","paper":"e4e4e4","line":"aa876a","emblem":"3d3226"})

# Grey
VARIANTS.append({"name":"Grey","folder":"8e8e8e","backfolder":"727272","paper":"e4e4e4","line":"8e8e8e","emblem":"323232"})
VARIANTS.append({"name":"Black","folder":"4f4f4f","backfolder":"3f3f3f","paper":"dcdcdc","line":"4f4f4f","emblem":"c2c2c2"})

# Orange
VARIANTS.append({"name":"Yaru","folder":"676767","backfolder":"973552","paper":"ff7446","line":"676767","emblem":"e4e4e4"})
VARIANTS.append({"name":"Orange","folder":"FF6639","backfolder":"FF5B39","paper":"e4e4e4","line":"FF6639","emblem":"4a4a4a"})


# Red
VARIANTS.append({"name": "Red","folder":"e25252","backfolder":"bf4b4b","paper":"e4e4e4","line":"e25252","emblem":"4d1c1c"})

# Pink bof...
VARIANTS.append({"name":"Pink","folder":"f06292","backfolder":"ec407a","paper":"e4e4e4","line":"f06292","emblem":"542233"})
VARIANTS.append({"name":"White","folder":"e4e4e4","backfolder":"cccccc","paper":"ffffff","line":"e4e4e4","emblem":"4f4f4f"})

# Purple
VARIANTS.append({"name":"Purple","folder":"7e57c2","backfolder":"5d399b","paper":"e4e4e4","line":"7e57c2","emblem":"2c1e44"})

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
