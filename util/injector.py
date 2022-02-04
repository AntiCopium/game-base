import sys
import os
import time
from logger import LHandler
import subprocess as sb

try:    
    inj = os.listdir("Inject")
except Exception:
    print("Inject folder not found. Creating it.")
    LHandler.warning("Inject folder not found. Creating it.")
    os.mkdir("Inject")
    time.sleep(2)
    LHandler.warning("Inject folder created.")
    print("Restarting injector.py")
    os.system("python util/injector.py")

def injinit():
    try:
        LHandler.warning("Inject folder found. Injecting... " + str(inj))
    except Exception as e:
        LHandler.error("Inject folder not found. Please create it.")
        sys.exit()


def runinj():
    
    print("injector.py is starting. Injecting... \n")
    time.sleep(1)
    for i in inj:
        if i.endswith(".exe"):
            LHandler.warning("Injecting " + i)
            os.startfile("Inject\\" + i)
            time.sleep(1)
            LHandler.warning("Injected " + i)

        elif i.endswith(".py"):
            LHandler.warning("Injecting " + i)
            os.startfile("Inject\\" + i)
            time.sleep(1)
            LHandler.warning("Injected " + i)

        elif i.endswith(".lua"):
            LHandler.warning("Injecting " + i)
            os.system("lua Inject/" + i)
            time.sleep(1)
            LHandler.warning("Injected " + i)
        else:
            LHandler.warning("Skipping " + i + " unrecognized file type.")
            print(" \nFailed to inject " + i + " unrecognized file type.")
