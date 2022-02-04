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
    injaccept = input(
        "Would you like to inject files? (y/n) " + str(injector.inj)).lower()
    if injaccept == "y":
        injector.runinj()
    elif injaccept == "yes":
        injector.runinj()
    else:
        LHandler.warning("User denied injection permission.")
        print("Injection denied successfully.")


if __name__ == '__main__':
    LHandler.LogInit()
    injector.injinit()
    main()
