import os
import pandas
from pathlib import Path
import datetime
import time





def csvFormatter():
    file = './statisticsIMD/1388_22_1_EVOLUCION_INTENSIDAD_OCUPACION.csv'


    lines=open(file).readlines()
    day=123
    for f in lines[1:]:

        parts=f.replace(',','.').split(';')
        date=parts[0].split(' ')[0]


        formDate=datetime.datetime.strptime(date, '%Y-%m-%d')
        formDateString=formDate.strftime('%Y.%m.%d')


        if formDate.day==day:

            fileOld = open('./intensOcupation/evolucion_diaria_intensidad.'+formDateString+'.csv', "a+")



            fileOld.write(parts[2]+','+parts[3]+'\n')


        else:
            newfile=open('./intensOcupation/evolucion_diaria_intensidad.'+formDateString+'.csv','w+')
            newfile.write('intensidad,ocupacion'+'\n')
            newfile.write(parts[2]+','+parts[3]+'\n')
            day=formDate.day
            print(newfile.readlines())
            newfile.close()





if __name__ == '__main__':
    tic = time.perf_counter()

    csvFormatter()
    toc = time.perf_counter()
    print(f"Formated in {toc - tic:0.4f} seconds")
