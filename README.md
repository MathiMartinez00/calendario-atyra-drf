# Descripción 
Este proyecto es una agenda virtual. Hecho con Django, Bootstrap y PostgreSQL.

# Requerimientos
Tener instalado los siguientes paquetes:
1. python3 (Python 3.8 o superior requerido)
2. python3-venv

Las instrucciones en este documento fueron probadas en Ubuntu 24.04 LTS. Tener en cuenta que estas podrían cambiar según la distribución de Linux utilizada.

# Pasos de instalación
1. Clonar el repositorio: 
```
git clone https://github.com/MathiMartinez00/calendario-atyra-drf.git
```
2. Ingresar al directorio creado: 
```
cd calendario-atyra-drf
```
3. Crear un entorno virtual de Python:
```
python3 -m venv ./env
```
4. Ingresar al entorno virtual creado:
```
source ./env/bin/activate
```
5. Instalar los paquetes necesarios para ejecutar la aplicación:
```
pip install -r requirements.txt
```
6. Crear una copia del archivo con las variables de entorno:
```
cp .env.sample .env
```
7. Completar la configuración en el archivo copiado en el paso anterior:
```
SECRET_KEY=
DEBUG_MODE=
ALLOWED_HOSTS=
```
Explicación de los valores:

- `SECRET_KEY` es una cadena de caracteres utilizada por Django para fines criptográficos. Puede ser creada con el comando: `python3 -c 'import random; print("".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]))'`.
- `DEBUG_MODE` define si se debe correr la aplicación en modo debug, ponerle cualquier valor hará que esté prendido.
- `ALLOWED_HOSTS` es una lista de dominios que el servidor acepta separado por espacios. Tiene por defecto el valor `localhost 127.0.0.1`.

8. Crear las tablas en la base de datos con los modelos de Django:
```
python3 manage.py migrate
```
9. Crear un superusuario para poder acceder al panel de administración:
```
python3 manage.py createsuperuser
```
10. Iniciar el servidor:
```
python3 manage.py runserver
```
11. Ingresar a `http://localhost:8000` para acceder a la aplicación.


