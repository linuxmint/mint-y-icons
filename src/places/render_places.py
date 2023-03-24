#!/usr/bin/python3
import os
import subprocess
import sys

sizes = ["16", "22", "24", "32", "48", "64", "96", "128"]

def generate_color(color):
    source = f"{color}.svg"
    green_dir = "../../usr/share/icons/Mint-Y"
    if color == "Green":
        theme_dir = green_dir
        os.system(f"mkdir -p {theme_dir}")
    else:
        theme_dir = "../../usr/share/icons/Mint-Y-%s" % color
        os.system(f"mkdir -p {theme_dir}")
        os.system(f"rm -rf {theme_dir}/*")
        os.system(f"cp -R {green_dir}/places {theme_dir}/")
        os.system(f"rm -rf {theme_dir}/places/symbolic")
        os.system(f"sed s/COLOR/{color}/g index.theme > {theme_dir}/index.theme ")

    for size in sizes:
        icon_dir = os.path.join(theme_dir, "places", size)
        icon_dir_2x = os.path.join(theme_dir, "places", size + "@2x")
        os.system("mkdir -p %s" % icon_dir)
        os.system("mkdir -p %s" % icon_dir_2x)
        names = subprocess.check_output("inkscape -S %s | grep -E \"_%s\" | sed 's/\,.*$//'" % (source, size), shell=True).decode("UTF-8")

        handles = []
        for name in names.split("\n"):

            if "_" in name:
                icon_name = name.replace("_%s" % size, "")
                icon_path = os.path.join(icon_dir, icon_name + ".png")
                print("Rendering %s" % icon_path)
                handle = subprocess.Popen("inkscape --export-id=%s \
                               --export-id-only \
                               --export-filename=%s %s >/dev/null \
                     && optipng -o7 --quiet %s" % (name, icon_path, source, icon_path), shell=True)
                handles.append(handle)

                icon_path = os.path.join(icon_dir_2x, icon_name + ".png")
                print("Rendering %s" % icon_path)
                handle = subprocess.Popen("inkscape --export-id=%s \
                               --export-id-only \
                               --export-dpi=192 \
                               --export-filename=%s %s >/dev/null \
                     && optipng -o7 --quiet %s" % (name, icon_path, source, icon_path), shell=True)
                handles.append(handle)

        n = len(handles)
        for handle in handles:
            print("waiting for processes.... %d" % n)
            n-=1
            handle.wait()

def parse_arg(arg):
    if arg == "All":
        os.system("rm -rf ../../usr/share/icons/Mint-Y-*")
        for filename in sorted(os.listdir(".")):
            if filename.endswith(".svg") and filename not in ["extra.svg", "src.svg"]:
                color = filename.replace(".svg", "")
                generate_color(color)
    else:
        generate_color(arg)

def usage():
    print ("Usage: render_places.py color \n\
    color can be a particular color or All.")
    sys.exit(1)

if len(sys.argv) != 2:
    usage()
else:
    parse_arg(sys.argv[1])
