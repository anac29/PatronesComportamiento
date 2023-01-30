import os

import numpy as np
import pandas
from pathlib import Path
import datetime
import time





def csvFormatter():
    file = './statisticsIMD/1388_22_1_EVOLUCION_INTENSIDAD_OCUPACION.csv'


    lines=open(file).readlines()
    lines.reverse()
    day=123
    contMnowEx=0

    previousTime=datetime.datetime.strptime('12:21:02.300', '%H:%M:%S.%f')
    for f in lines[0:-1]:

        parts=f.replace(',','.').split(';')
        date=parts[0].split(' ')[0]
        time=parts[0].split(' ')[1]
        nowTime=datetime.datetime.strptime(time, '%H:%M:%S.%f')



        formDate=datetime.datetime.strptime(date, '%Y-%m-%d')
        formDateString=formDate.strftime('%Y.%m.%d')

        add12=False
        diff = 0
        diffPre=0

        #si la nueva hora dista en más de 1 entra en el if
        if nowTime.hour-previousTime.hour>1:

            add12=True
            diff=(nowTime.hour-previousTime.hour-1)*11
            contM=0
            #si la últma hora no llegó a y 56 se suma lo que falte
            if 56-int(previousTime.minute)>1:
                difM=int(previousTime.minute)-1
                preM=56-1
                contM=(preM-difM)//5

                diff=diff+contM
            contMnow=0
            #lo mismo pero si no empieza en 1
            if int(nowTime.minute)>1:
                difMnow = int(nowTime.minute)-1
                contMnow=difMnow//5


                diff = diff + contMnow
        #puede darse el caso de que no se salte una hora si no minutos
        elif nowTime.hour-previousTime.hour==1:
            add12=True
            contMnowEx=0
            if 56 - int(previousTime.minute) > 1:
                difM = int(previousTime.minute) - 1
                preM = 56 - 1
                contMnowEx = (preM - difM) // 5
                diff = diff + contMnowEx
            contMnowEx=0
            if int(nowTime.minute)>1:
                difMnow = int(nowTime.minute)-1
                contMnowEx=difMnow//5


                diff = diff + contMnowEx


        if formDate.day==day:

            fileOld = open('./intensOcupation/evolucion_diaria_intensidad.'+formDateString+'.csv', "a+")
            #se añaden las muestras que hagan falta
            if (add12):
                for i in range(diff):
                    fileOld.write(str(np.NaN) + ',' + str(np.NaN) + '\n')


            fileOld.write(parts[0]+','+parts[2]+','+parts[3]+'\n')
            cont=cont+1
            previousTime=nowTime


        else:
            newfile=open('./intensOcupation/evolucion_diaria_intensidad.'+formDateString+'.csv','w+')
            newfile.write('fecha,intensidad,ocupacion' + '\n')


            newfile.write(parts[0]+','+parts[2]+','+parts[3]+'\n')
            day=formDate.day
            newfile.close()
            cont=1
            previousTime=nowTime





if __name__ == '__main__':
    tic = time.perf_counter()

    csvFormatter()
    toc = time.perf_counter()
    print(f"Formated in {toc - tic:0.4f} seconds")
