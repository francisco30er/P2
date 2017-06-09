# Cobro automático de peajes y estacionamientos.
El proyecto consiste en un sistema de reconocimiento de imágenes en que al utilizar una cámara,se identifica el número de placa de un vehículo y este se asocia con una cuenta bancaria desde la cual se rebajan los costos del servicio.

Para el control de la aplicación se utilizó una Raspberry pi 3. Debe tener instalada la librería ALPR, con el éste comando "sudo apt-get update && sudo apt-get install -y openalpr openalpr-daemon openalpr-utils libopenalpr-dev"
Para correr el programa se de deben tener los archivos Final.py y datos.txt en una misma carpeta. Se ejecuta el código con el comando "sudo python Final.py".

