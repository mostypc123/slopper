import os
import sys


def execute(cmd: str):
    if os.system(cmd) != 0:
        print(f"\033[91mAn error occured while running '{cmd}'.\033[0m")
        sys.exit(1)
