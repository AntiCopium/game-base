import sys
import os
import time
from logger import LHandler
import subprocess as sb

def exception():
        print("Inject folder not found. Creating it.")
        os.mkdir("Inject")
        time.sleep(1)
        print("Restarting Sky.py")
        os.system("Sky.py")
        time.sleep(2)


def injinit():
    try:
        inj = os.listdir("Inject")
    except Exception:
        exception()


def runinj():
    inj = os.listdir("Inject")
    LHandler.warning("Inject folder found. Injecting... " + str(inj))

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
            

