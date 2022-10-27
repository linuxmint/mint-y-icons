#!/usr/bin/python3
import os

# This script uses green.svg and generates the following files from it:
#
# aqua.svg
# blue.svg
# brown.svg
# grey.svg
# orange.svg
# pink.svg
# purple.svg
# red.svg
# sand.svg
# teal.svg

# It uses the following color table to do so:
COLORS = {}
COLORS["aqua"] = "66a8cb"
COLORS["blue"] = "5972c3"
COLORS["brown"] = "997052"
COLORS["grey"] = "999999"
COLORS["orange"] = "ff7139"
COLORS["pink"] = "e54980"
COLORS["purple"] = "8c5dd9"
COLORS["red"] = "da281e"
COLORS["sand"] = "c5a07c"
COLORS["teal"] = "199ca8"
COLORS["yellow"] = "ffc107"

GREEN_COLOR = "8bb158"

for color in COLORS:
    value = COLORS[color]
    os.system("sed 's/%s/%s/g' green.svg > %s.svg" % (GREEN_COLOR, value, color))
