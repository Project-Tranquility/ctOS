from test import demo
from src.start.start import start
from src.help import help
import sys
from dotenv import load_dotenv
from src.music.music import music_command

load_dotenv()

def main():
    nb = len(sys.argv)
    
    if nb <= 1:
        help()
        return
    if sys.argv[1] == "--music":
        music_command()
        return
    if sys.argv[1] == "--help" or "-h":
        help()
    if sys.argv[1] == "hello":
        demo()
        start()
    else:
        return 84
main()