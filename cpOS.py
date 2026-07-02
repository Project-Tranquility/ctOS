#!/usr/bin/env python3
import requests
from test import demo
from src.start.start import start
from src.help import help
import sys

def main():
    nb = len(sys.argv)
    
    if nb <= 1:
        help()
        return
    if sys.argv[1] == "--help" or "-h":
        help()
    if sys.argv[1] == "hello":
        demo()
        start()
    else:
        return 84

main()