import os
from collections import Counter

def eliminateDate():
    directory='./insOcuFinal'
    for filename in os.listdir(directory):

        newfile = open('./dataINSOCU/'+filename, 'w+')
        newfile.write('intensidad,ocupacion' + '\n')
        lines=(open(os.path.join(directory, filename)).readlines())
        for l in lines[1:]:
            l=l.replace('nan','NaN')
            parts = l.split(',')

            if(len(parts)>2):

                newfile.write(parts[1]+','+parts[2])
            else:
                newfile.write(parts[0]+','+parts[1])






if __name__ == '__main__':
   eliminateDate()

