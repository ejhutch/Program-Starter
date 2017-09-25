import subprocess
import psutil
import time
import sys
import re
import os

def get_opera_dir():
    """
    Need to do this because the Opera install dir keeps moving
    """
    my_dir = "C:/Program Files/Opera/"
    find_dir = re.compile(r"^[0-9]", re.IGNORECASE)
    last_opera_dir = ""

    for root, dirs, files in os.walk(my_dir, topdown=False):
        for d in dirs:
            if find_dir.match(d):
                last_opera_dir = d

    my_dir+=last_opera_dir
    my_dir+="/opera.exe"

    return(my_dir)



def countdown(count):

    while (count > 0):
        msg = 'Closing in: ' + str(count)
        print(msg, end="\r")
        count -= 1
        time.sleep(1)


def start_programs():

    programs = {
        'chrome.exe': r'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe',
        'EmEditor.exe': r'C:/Users/erh/AppData/Local/Programs/EmEditor/EmEditor.exe',
        'mintty.exe': r'C:/cygwin64/bin/mintty.exe -i /Cygwin-Terminal.ico -',
        'dsNetworkConnect.exe': r'"C:/Program Files (x86)/Juniper Networks/Network Connect 8.1/dsNetworkConnect.exe"',
        'MultiCommander.exe': r'C:/Users/erh/MultiCommander_x64_Portable/MultiCommander.exe',
        'procexp.exe': r'C:/Users/erh/SysinternalsSuite/procexp.exe',
        'opera.exe': r''}
        
    programs["opera.exe"] = get_opera_dir()
    
    print(programs["opera.exe"])

    try:
        # store all process names in a list
        process_list = []
        for p in psutil.process_iter():
            process_list.append(p.name())

        # start programs in the programs dict but not in process_list
        for program in programs:
            if program in process_list:
                print(program + " is running")
            else:
                print(program + " is being started")
                subprocess.Popen(programs[program])

        countdown(5)

    except BaseException:
        print("Unexpected error:", sys.exc_info()[0])
        input("Press Enter to continue...")


if __name__ == "__main__":
    start_programs()
