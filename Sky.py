# ECHO is on.
# Import Sky.py
# Main file for program : Author: CapThat

import sys
import math
import time
import json
import os
from logger import LHandler
from util import injector


def main():
    try:
        inj = os.listdir("Inject")
    except Exception as e:
        print(e)

    injaccept = input(
        "Would you like to inject files? (y/n) " + str(inj)).lower()
    if injaccept == "y":
        injector.runinj()
    elif injaccept == "yes":
        injector.runinj()
    else:
        print("Injection denied successfully.")
        LHandler.warning("User denied injection permission.")


if __name__ == '__main__':
    LHandler.LogInit()
    injector.injinit()
    main()
