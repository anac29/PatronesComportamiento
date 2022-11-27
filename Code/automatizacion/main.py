# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from pathlib import Path

directory = './cropped'

files = os.listdir(directory)
path=Path.cwd()


def first(image):
    options = Options()
    #Opción True para que salga la ventana
    options.headless = True

    driver = webdriver.Firefox(options=options)
    #Accedemos la página de estracción de datos
    driver.get("https://apps.automeris.io/wpd/")

    #Buscamos el botón Cargar Imagen y pulsamos
    element = driver.find_element(By.CSS_SELECTOR, "input[value*='Load Image']")
    action = ActionChains(driver)
    action.perform()

    action.click(on_element=element)
    action.perform()
    #Buscamos en botón de de subir archivo
    elegir_arc = driver.find_element(By.ID, "fileLoadBox")


    parts=image.split("/")
    #Mandamos la imagen por medio de la ruta global más la de la imagen a analizar
    elegir_arc.send_keys(str(path)+"/cropped/"+parts[2])
    #Pulsamos en alinear ejes
    align = driver.find_element(By.CSS_SELECTOR,"input[value*='Align Axes']")
    action.click(on_element = align)
    #Pulsamos en proceder
    proce = driver.find_element(By.CSS_SELECTOR,"input[value*='Proceed']")

    action.click(on_element = proce)
    canva = driver.find_element(By.CLASS_NAME,"canvasLayers")

    #Para cada punto pulsamos en una coordenada de la imagen
    action.move_to_element_with_offset(canva, -354, 216).click().perform()

    action.move_to_element_with_offset(canva, 378, 216).click().perform()
    action.move_to_element_with_offset(canva, -389, 147).click().perform()
    action.move_to_element_with_offset(canva, -389, -196).click().perform()

    #Pulsamos en complete.
    comple = driver.find_element(By.CSS_SELECTOR, "input[value*='Complete!']")

    action.click(on_element=comple).perform()
    x1=driver.find_element(By.ID,"xmin")
    x1.clear()
    #Introducimos para cada casilla el valor del eje
    x1.send_keys("01:00")
    x2=driver.find_element(By.ID,"xmax")
    x2.clear()
    x2.send_keys("22:00")
    y1=driver.find_element(By.ID,"ymin")
    y1.clear()
    y1.send_keys("10")
    y2=driver.find_element(By.ID,"ymax")
    y2.clear()
    y2.send_keys("60")


    ok = driver.find_element(By.ID,"xybtn")
    action.click(on_element=ok).perform()

    #Pulsamos en el color
    color_button = driver.find_element(By.ID, "color-button")
    action.click(on_element=color_button).perform()

    red = driver.find_element(By.ID, "color-selection-red")
    red.clear()
    #Primero con el rojo, introducimos sus valores en rgb
    red.send_keys("255")

    green = driver.find_element(By.ID, "color-selection-green")
    green.clear()

    green.send_keys("0")

    blue = driver.find_element(By.ID, "color-selection-blue")
    blue.clear()

    blue.send_keys("0")

    #Done
    done = driver.find_element(By.CSS_SELECTOR,"input[value*='Done']")
    action.click(on_element=done).perform()

    #Itroducimos el umbral
    umbral = driver.find_element(By.ID, "color-distance-value")
    umbral.clear()

    umbral.send_keys("79")

    xStep = driver.find_element(By.ID, "algo-param-xStep")
    xStep.clear()

    #Y cada cuantos pixeles hay punto
    xStep.send_keys("1")
    yStep = driver.find_element(By.ID, "algo-param-yStep")
    yStep.clear()

    yStep.send_keys("1")

    run = driver.find_element(By.CSS_SELECTOR, "input[value*='Run']")
    action.click(on_element=run).perform()

    #Renombramos y hacemos lo  mismo para la azul
    rename(driver,action)



def rename(driver,action):


    #clickamos en el dataset
    datasets = driver.find_element(By.ID,"tree-item-id-4")
    action.click(on_element=datasets).perform()
    red_item = driver.find_element(By.ID, "tree-item-id-5")
    action.click(on_element=red_item).perform()
    #clicamos en renombrar
    WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[7]/center/p[3]/input')))

    #renombramos el dataset
    input_nename=WebDriverWait(driver, 1000000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="rename-dataset-name-input"]')))
    input_nename.clear()
    input_nename.send_keys("Int. (hoy)")



    #click on rename
    WebDriverWait(driver, 1000000).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[36]/center/p[2]/input[1]'))).click()


    #creamos otro dataset
    WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tree-item-id-4"]'))).click()
    WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[5]/center/p[1]/input'))).click()

    #renombramos el azul
    input_nename=WebDriverWait(driver, 1000000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-single-dataset-name-input"]')))
    input_nename.clear()
    input_nename.send_keys("Int. (Ayer)")
    #renamed
    WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[35]/p[1]/input[2]'))).click()
    WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tree-item-id-6"]'))).click()


    #ponemos color azul
    WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="color-button"]'))).click()

    #enviamos las coordenadas rgb del color
    red_number=WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="color-selection-red"]')))
    red_number.clear()
    red_number.send_keys("111")

    green_number = WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="color-selection-green"]')))
    green_number.clear()
    green_number.send_keys("172")

    blue_number = WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="color-selection-blue"]')))
    blue_number.clear()
    blue_number.send_keys("255")


    #Done
    WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, '//html/body/div[25]/p[7]/input'))).click()



    #umbral
    blue_number = WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="color-distance-value"]')))
    blue_number.clear()
    blue_number.send_keys("91")



    #step
    blue_number = WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="algo-param-xStep"]')))
    blue_number.clear()
    blue_number.send_keys("1")
    blue_number = WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="algo-param-yStep"]')))
    blue_number.clear()
    blue_number.send_keys("1")
    WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div[3]/div[2]/p[9]/input'))).click()
    #Pulsamos en datasets y en export all data
    WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tree-item-id-4"]'))).click()
    WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[5]/center/p[2]/input'))).click()
    WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[34]/p[2]/input[1]'))).click()

    driver.quit()
def iterador_archivos():



    #itera sobre los directorios, normalmente se hace en tandas pues si no se para el programa
    length=len(files)
    for i in range(0,1):
        print(i)
        f = os.path.join(directory, files[i])
        # checking if it is a file
        if os.path.isfile(f):

            first(f)
            #para que sirva para cualquier persona se usa la ruta global
            rute_part = str(path).split("/")
            wpd='/'+rute_part[1]+'/'+rute_part[2]+'/Descargas/wpd_datasets.csv'
            filename=files[i].split('.png')[0]
            #lo movemos a la carpeta files
            os.rename(wpd,'./files'+'/'+filename)
            f=open('./files'+'/'+filename)
            #nos quedamos solo con las columnas Y
            with open('./formated'+'/'+filename, 'w') as fi_write:
                fi_write.write("Y(hoy),Y(ayer)\n")
                for line in f.readlines()[2:]:

                    columns=line.split(',')
                    fi_write.write(columns[1]+','+columns[3])



if __name__ == '__main__':
    iterador_archivos()

# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/