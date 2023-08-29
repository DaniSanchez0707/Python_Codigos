import requests
from os import path
import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument('-t', '--target', help='Indica el dominio de la victima')

parser = parser.parse_args()
print(parser.target)
def main():
    if parser.target:
        if path.exists('subdominios.txt'):
            wordlist = open('subdominios.txt','r')
            wordlist = wordlist.read().split('\n')

            for subdominio in wordlist:
                url = 'http://'+subdominio+'.'+parser.target
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    pass
                else:
                    print('(+) subdominio encontrado '+ url)

            for subdominio in wordlist:
                url = 'https://'+subdominio+'.'+parser.target
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    pass
                else:
                    print('(+) subdominio encontrado '+ url)
    else:
        print('(-) ingresa un dominio')     


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()