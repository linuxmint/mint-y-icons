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
COLORS["brown"] = "7f542b"
COLORS["grey"] = "767676"
COLORS["orange"] = "ef6410"
COLORS["pink"] = "e54980"
COLORS["purple"] = "951595"
COLORS["red"] = "df2121"
COLORS["sand"] = "cb8600"
COLORS["teal"] = "008670"

GREEN_COLOR = "8bb158"

for color in COLORS:
    value = COLORS[color]
    os.system("sed 's/%s/%s/g' green.svg > %s.svg" % (GREEN_COLOR, value, color))
