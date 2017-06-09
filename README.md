# Cobro automático de peajes y estacionamientos.
El proyecto consiste en un sistema de reconocimiento de imágenes en que al utilizar una cámara, se identifica el número de placa de un vehículo y éste se asocia con una cuenta bancaria mediante una base de datos desde la cual se rebajan los costos del servicio.

Para el control de la aplicación se utilizó una Raspberry pi 3. Debe tener instalada la librería ALPR, con el éste comando 
```
sudo apt-get update && sudo apt-get install -y openalpr openalpr-daemon openalpr-utils libopenalpr-dev
```
También se debe confugurar los pines GPIO para controlar el servomotor de la aguja y los botones para tomar foto y bajar la aguha del peaje. Ésta librería se instala con la siguiente linea de comandos:
```
sudo apt-get update
sudo apt-get upgrade
wget https://pypi.python.org/packages/source/R/RPi.GPIO/RPi.GPIO-0.5.4.tar.gz
tar zxf RPi.GPIO-0.5.4.tar.gz
cd RPi.GPIO-0.5.4.tar.gz
sudo python setup.py install
```
Para el control de la cámara en Python sebe instalar la librería picamara.

Instalación

Antes de nada conectaremos el módulo de cámara al puerto CSI de la Raspberry Pi estando desconectada de la red eléctrica. Luego arrancamos la Raspberry e iniciamos sesión con nuestro usuario y contraseña. Abrimos una ventana de la terminal y escribimos:
```
sudo raspi-config
sudo raspi-config
```
En el menú seleccionamos la opción ‘Enable Camera‘ luego le damos a ‘Enable‘ y a ‘Finish‘ para reiniciar la Raspberry. Una vez instalado y activado el módulo de cámara vamos a instalar la librería:
```
sudo apt-get install python-picamera
```
Para correr el programa se de deben tener los archivos Final.py y datos.txt en una misma carpeta. Se ejecuta el código con el comando
```
sudo python Final.py
```
