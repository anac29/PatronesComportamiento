# Acceso notebooks con desarrollo del proyecto

Este proyecto está en su mayoría desarollado y explicado en notebooks de python. Estos se encuentran ubicados en la siguiente ruta de este repositorio: [Notebooks/PatronesComportamiento-Notebooks/PatronesComportamiento](https://github.com/anac29/PatronesComportamiento/tree/main/Notebooks/PatronesComportamiento-Notebooks/PatronesComportamiento). Del 1 al 9 están los notebooks ordenados correspondiendo con el orden en el que se desarrollaron. A continuación se adjunta un breve manual de como modificar las rutas acorde al dispositivo final donde se esté ejecutando el notebook en el caso de que se quisiesen ejecutar las celdas, para visualizar los notebooks y ver los resultados esto no sería necesario pues ya están todas ejecutadas.

## Breve guía importación notebooks
Las rutas de los notebooks de este repositorio estan universalizadas. Lo que quiere decir que funcionan en cualquier dispositivo en el caso de querer ejecutar las celdas. Por tanto tan sólo hay que descargar el repositorio y acceder a los notebooks.
Como último apunte, los modelos fueron entrenados en google colab por lo que es posible que si se ejecuta en un entorno que no sea ese cualquier operación con los mismos no fncione pues al guardar con [skops](https://scikit-learn.org/stable/model_persistence.html) el modelo depende del sistema operativo. No obstante, el resto d métricas y celdas se pueden ejecutar.
En el caso de querer la versión de los notebooks de rive acceder a través de este [enlace](https://drive.google.com/drive/folders/1OlhHEGF5OvJh-oHJFasn_EWG-KcCmA5Z?usp=sharing).


Lo que se muestra a continuación es una pequeña guía sobre el código desarrollado para la automatización de extracción de datos.

# PatronesComportamiento
Hay que tener en cuenta una serie de aspectos:
* Puesto que se ha desarrollado en linux la rutas usadas en los scripts pueden diferir para otro sistema operativo.
* Aún no se han puesto las rutas relativas.
* Los ficheros generados tras la extracción de datos de las gráficas se encuentran en la carpeta Code> automatizacion > files
* Tras el formateo de esos ficheros se crea un csv en el que solo se encuentran las columnas Y, seán conveniente reordenar estos puntos. Estos ficheros se encuentran en Code > automatizacion >formated
* En Code > automatización > cropped están las fotos recortadas.
* Y en Code > traffic las fotos de las gráficas proporcionadas.

Este documentos se irá actualizando si alguno de estos aspectos cambiase.

# Configuración del sistema
Para poder ejecutar el código habrá que instalar selenium. Para ello ejecutamos el comando en el caso de encontrarnos en el **Linux**:
```sh
pip install selenium 

```
Ahora, hay que instalar el WebDriver:
Descargamos el driver:
```sh
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
```
Extraemos el fichero:
```sh
tar -xvzf geckodriver*
```
Lo convertimos en ejecutable:
```sh
chmod +x geckodriver
```
Lo convertimos en ejecutable:
```sh
sudo mv geckodriver /usr/local/bin/
