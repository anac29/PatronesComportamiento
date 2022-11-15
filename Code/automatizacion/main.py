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

directory = './cropped'

files = os.listdir(directory)


def first(image):
    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options)
    driver.get("https://apps.automeris.io/wpd/")
    element = driver.find_element(By.CSS_SELECTOR, "input[value*='Load Image']")
    action = ActionChains(driver)
    action.perform()

    action.click(on_element=element)
    action.perform()
    elegir_arc = driver.find_element(By.ID, "fileLoadBox")


    parts=image.split("/")

    elegir_arc.send_keys("/home/ana/Documentos/TFG/automatizacion/cropped/"+parts[2])
    print("aaaa")
    align = driver.find_element(By.CSS_SELECTOR,"input[value*='Align Axes']")

    action.click(on_element = align)

    proce = driver.find_element(By.CSS_SELECTOR,"input[value*='Proceed']")

    action.click(on_element = proce)
    canva = driver.find_element(By.CLASS_NAME,"canvasLayers")

    action.move_to_element_with_offset(canva, -354, 216).click().perform()

    action.move_to_element_with_offset(canva, 378, 216).click().perform()
    action.move_to_element_with_offset(canva, -389, 147).click().perform()
    action.move_to_element_with_offset(canva, -389, -196).click().perform()

    comple = driver.find_element(By.CSS_SELECTOR, "input[value*='Complete!']")

    action.click(on_element=comple).perform()
    x1=driver.find_element(By.ID,"xmin")
    x1.clear()
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

    color_button = driver.find_element(By.ID, "color-button")
    action.click(on_element=color_button).perform()

    red = driver.find_element(By.ID, "color-selection-red")
    red.clear()

    red.send_keys("255")

    green = driver.find_element(By.ID, "color-selection-green")
    green.clear()

    green.send_keys("0")

    blue = driver.find_element(By.ID, "color-selection-blue")
    blue.clear()

    blue.send_keys("0")

    done = driver.find_element(By.CSS_SELECTOR,"input[value*='Done']")
    action.click(on_element=done).perform()


    umbral = driver.find_element(By.ID, "color-distance-value")
    umbral.clear()

    umbral.send_keys("79")

    xStep = driver.find_element(By.ID, "algo-param-xStep")
    xStep.clear()

    xStep.send_keys("1")
    yStep = driver.find_element(By.ID, "algo-param-yStep")
    yStep.clear()

    yStep.send_keys("1")

    run = driver.find_element(By.CSS_SELECTOR, "input[value*='Run']")
    action.click(on_element=run).perform()

    rename(driver,action)



def rename(driver,action):


    datasets = driver.find_element(By.ID,"tree-item-id-4")
    action.click(on_element=datasets).perform()
    red_item = driver.find_element(By.ID, "tree-item-id-5")
    action.click(on_element=red_item).perform()

    WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[7]/center/p[3]/input')))

    #rename = driver.find_element(By.CSS_SELECTOR, "input[value*='Rename Dataset']")
    #action.click(on_element=rename)
    #rename_input.send_keys("Int. (hoy)")
    #WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[7]/center/p[3]/input'))).click()


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


    #ponemos clor azul
    WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="color-button"]'))).click()


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

    WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tree-item-id-4"]'))).click()
    WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[5]/center/p[2]/input'))).click()
    WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[34]/p[2]/input[1]'))).click()

    driver.quit()
def iterador_archivos():

    # assign directory

    # iterate over files in
    # that directory
    length=len(files)
    for i in range(30,40):
        print(i)
        f = os.path.join(directory, files[i])
        # checking if it is a file
        if os.path.isfile(f):

            first(f)
            wpd='/home/ana/Descargas/wpd_datasets.csv'
            filename=files[i].split('.png')[0]
            os.rename(wpd,'./files'+'/'+filename)
            f=open('./files'+'/'+filename)
            with open('./formated'+'/'+filename, 'w') as fi_write:
                fi_write.write("Y(hoy),Y(ayer)\n")
                for line in f.readlines()[2:]:

                    columns=line.split(',')
                    fi_write.write(columns[1]+','+columns[3])



if __name__ == '__main__':
    iterador_archivos()

# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/