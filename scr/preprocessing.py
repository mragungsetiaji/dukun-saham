import os, sys, csv
import math

def roundup(var):
    return float(format(var, '.6f'))

def main(dir_path, output_dir):
    files = os.listdir(dir_path)
    for file_name in files:
        with open(os.path.join(dir_path, file_name), mode='r') as testfile:
            