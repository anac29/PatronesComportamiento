import os
from collections import Counter

def standardizeD():
    directory='./intensOcupation'
    lengths=[]
    diccionario={}
    for filename in os.listdir(directory):
        lines=len(open(os.path.join(directory, filename)).readlines())

        lengths.append(lines)

    diccionario = dict(Counter(lengths))

    print(diccionario)

def names():
    directory='./intensOcupation'

    for filename in os.listdir(directory):
        if len(open(os.path.join(directory, filename)).readlines())<289:
            lines = len(open(os.path.join(directory, filename)).readlines())

            print(filename+': '+ str(lines))




if __name__ == '__main__':
   standardizeD()
   names()
