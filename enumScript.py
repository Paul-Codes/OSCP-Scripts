
#!/usr/bin/env python
import subprocess
import multiprocessing
from multiprocessing import Process, Queue
import os
import time
import fileinput
import atexit
import sys
import socket

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if __name__ == '__main__':

    #Set Up the targets
    targets = sys.argv
    targets.pop(0)

    dirs = os.listdir("./oscp/lab")
    for scanip in targets:
        scanip = scanip.rstrip()
        if not scanip in dirs:
            print bcolors.HEADER + "INFO: No folder was found for " + scanip + ". Setting up folder." + bcolors.ENDC
            subprocess.check_output("mkdir oscp/lab/" + scanip, shell=True)
            subprocess.check_output("mkdir oscp/lab/" + scanip + "/exploits", shell=True)
            subprocess.check_output("mkdir oscp/lab/" + scanip + "/privesc", shell=True)
            print bcolors.OKGREEN + "INFO: Folder created here: " + "oscp/lab" + scanip + bcolors.ENDC
            subprocess.check_output(
                "cp windows-template.md oscp/lab/" + scanip + "/mapping-windows.md",
                shell=True)
            subprocess.check_output(
                "cp linux-template.md oscp/lab/" + scanip + "/mapping-linux.md", shell=True)
            print bcolors.OKGREEN + "INFO: Added pentesting templates: " + "oscp/lab/" + scanip + bcolors.ENDC
            subprocess.check_output(
                "sed -i -e 's/INSERTIPADDRESS/" + scanip + "/g' oscp/lab/" + scanip + "/mapping-windows.md",
                shell=True)
            subprocess.check_output(
                "sed -i -e 's/INSERTIPADDRESS/" + scanip + "/g' oscp/lab/" + scanip + "/mapping-linux.md",
                shell=True)