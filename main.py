import time
import random
import sys
from util.variaveis import pessoas, destino, voos

if __name__ == '__main__':
    for indice in voos:
        print(indice)
        for infos in voos[indice]:
            print(infos)