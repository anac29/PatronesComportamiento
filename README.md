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




```

