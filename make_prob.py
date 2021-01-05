#!/usr/bin/env python3
import argparse
import os
import subprocess
import shutil

# set up this in order to point to proper directory.
setup_dir = "/Users/junikim/Desktop/setup"
os.environ["CP_SETUP_DIR"] = setup_dir

parser = argparse.ArgumentParser()

def file_option(s:str):
    global parser
    parser.add_argument(s, default=[], type=str, nargs="*")

def add_download():
    global setup_dir
    os.chdir(file)
    shutil.copyfile(setup_dir+"/download.py", "download.py")
    os.system("chmod +x download.py")
    os.chdir("..")


"""
in order to make a new template, add it to file_option,
create a new script in prob_maker, and then call as below.
"""

file_option("-py")
file_option("-std")
file_option("-java")
file_option("-minjava")
file_option("-rust")
problems = parser.parse_args()


for file in problems.std:
    subprocess.call(["bash", setup_dir +"/prob_maker/std.sh", file])
    add_download()
    
for file in problems.java:
    subprocess.call(["bash", setup_dir +"/prob_maker/java.sh", file])
    add_download()

for file in problems.minjava:
    subprocess.call(["bash", setup_dir +"/prob_maker/minjava.sh", file])
    add_download()

for file in problems.py:
    subprocess.call(["bash", setup_dir +"/prob_maker/py.sh", file])
    add_download()

for file in problems.rust:
    subprocess.call(["bash", setup_dir +"/prob_maker/rust.sh", file])
    os.chdir(file + "/src")
    shutil.copyfile(setup_dir+"/download.py", "download.py")
    os.system("chmod +x download.py")
    os.chdir("../..")
