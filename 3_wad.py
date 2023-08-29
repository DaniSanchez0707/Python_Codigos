import subprocess
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help='Indica la URL')
parser = parser.parse_args()

def main():
    if parser.target:
        subprocess.call("wad -u" +parser.target+"> tecnologias2.txt", shell=True)
    else:
        print('(-) Ingresa una URL')




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()