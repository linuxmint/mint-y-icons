#!/usr/bin/python3

import os

for size in [16, 24, 32, 48]:
    source_path = "emblems/%s" % size
    dest_path = "../usr/share/icons/Mint-Y/emblems/%s" % size
    dest2x_path = "../usr/share/icons/Mint-Y/emblems/%s@2x" % size

    for filename in sorted(os.listdir(source_path)):
        png_filename = filename.replace(".svg", ".png")
        source_file = os.path.join(source_path, filename)
        dest_file = os.path.join(dest_path, png_filename)
        dest2x_file = os.path.join(dest2x_path, png_filename)

        if not os.path.exists(dest_file):
            print ("Rendering %s" % dest_file)
            os.system("inkscape --export-png=%s -f %s >/dev/null && optipng -o7 --quiet %s" % (dest_file, source_file, dest_file))

        if not os.path.exists(dest2x_file):
            print ("Rendering %s" % dest2x_file)
            os.system("inkscape --export-dpi=192 --export-png=%s -f %s >/dev/null && optipng -o7 --quiet %s" % (dest2x_file, source_file, dest2x_file))
