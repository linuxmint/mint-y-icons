#!/usr/bin/python3

import os
import subprocess
import sys

MINTY_DIR = os.path.join(os.getcwd(), "..", "usr", "share", "icons")
DEADLINK_DIR = os.path.join(os.getcwd(), "..")

def check_symbolic_links_list():
    with open(SYMBOLIC_APPS_FILE, "r") as symbolic_apps_file:
        line_no = 0
        for symbolic_link_ref in symbolic_apps_file:
            line_no = line_no+1
            if " <- " not in symbolic_link_ref:
                print("Wrong symbolic link reference in line " + str(line_no) + ": " + symbolic_link_ref)
            else:
                target, symlink = symbolic_link_ref.split(" <- ")
                # check if target.svg exists
                target_svg = target.rsplit(".", 1)[0] + ".svg"
                CHECK_DIR = SRC_DIR
                if sys.argv[1] == "mimetypes":
                    CHECK_DIR += "/64"
                if not os.path.exists(os.path.join(CHECK_DIR, target_svg)):
                    print(target_svg + " does not exist (line " + str(line_no) + ")")
                    #pass

                create_symbolic_link(target, symlink)

def create_symbolic_link(target, symlink):
    for apps_pixel in os.listdir(APPS_DIR):
        if apps_pixel != "symbolic":
            target_path = os.path.join(APPS_DIR, apps_pixel, target).rstrip()
            symlink_path = os.path.join(APPS_DIR, apps_pixel, symlink).rstrip()
            if not os.path.islink(symlink_path):
                subprocess.call(['ln', '-s', '-r', target_path, symlink_path])
                print(symlink_path + " created")

def delete_symbolic_links():
    subprocess.call(['find', APPS_DIR, '-type', 'l', '-delete'])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Pass argument: ")
        print("    apps")
        print("    categories")
        print("    mimetypes")
        print(" ")
        print("    show-deadlinks")
        print("    delete-deadlinks")
        print("    delete-symbolic-apps")
        print("    delete-symbolic-categories")
    else:
        if sys.argv[1] in ["apps", "categories", "mimetypes"]:
            SYMBOLIC_APPS_FILE = os.path.join(os.getcwd(), "symbolic-" + sys.argv[1] + "-list")
            SRC_DIR = os.path.join(os.getcwd(), sys.argv[1])
            APPS_DIR = os.path.join(os.getcwd(), "..", "usr", "share", "icons", "Mint-Y", sys.argv[1])

            print("Creating symbolic links in " + sys.argv[1] + " directories...")
            check_symbolic_links_list()
            print("Done!")
        elif sys.argv[1] in ['delete-symbolic-apps']:
            APPS_DIR = os.path.join(os.getcwd(), "..", "usr", "share", "icons", "Mint-Y", "apps")
            delete_symbolic_links()
        elif sys.argv[1] in ['delete-symbolic-categories']:
            APPS_DIR = os.path.join(os.getcwd(), "..", "usr", "share", "icons", "Mint-Y", "categories")
            delete_symbolic_links()
        elif sys.argv[1] == 'show-deadlinks':
            os.chdir(DEADLINK_DIR)
            subprocess.call(DEADLINK_DIR + "/deadlinks")
        elif sys.argv[1] == 'delete-deadlinks':
            subprocess.call(['find', '-L', MINTY_DIR, '-type', 'l', '-delete'])
        else:
            print("Wrong argument! Valid arguments are:")
            print("    apps")
            print("    categories")
            print("    mimetypes")
            print(" ")
            print("    show-deadlinks")
            print("    delete-deadlinks")
            print("    delete-symbolic-apps")
            print("    delete-symbolic-categories")
