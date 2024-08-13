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

# Uso de la API

La aplicación utiliza autenticación por medio de tokens. Los tokens son creados automáticamente al momento de agregar usuarios. Se puede obtener el token para un usuario realizando una petición POST a `/obtain-auth-token/` con el usuario y contraseña del usuario. Un ejemplo de petición con `curl` es:

```
curl -X POST http://localhost:8000/api-auth-token/ \
    -H "Content-Type: application/json" \
    -d '{"username": "<USER>", "password": "<PASS>"}'
```

El cual dará una respuesta tipo:

```
{"token":"<TOKEN>"}
```

Para autenticar en endpoints que lo requieran se debe agregar la cabecera HTTP `Authorization: Token <TOKEN>`, donde `<TOKEN>` es el token conseguido al realizar una petición a `/api-auth-token/`.

Existe solo una ruta definida con datos para agregar y listar reservas `/api/reservas/`. Un ejemplo para listar las reservas es:
```
curl http://localhost:8000/api/reservas/ \
    -H "Authorization: Token <TOKEN>"
```
Para agregar una reserva:
```
curl http://localhost:8000/api/reservas/ \
    -H "Content-Type: application/json" \
    -H "Authorization: Token <TOKEN>" \
    -d '{"casa":1, "nombre":"M", "email": "a@example.com", "cantidad_adultos": 1, "fecha_inicio": "2024-08-14", "fecha_fin": "2024-08-18"}'
```

Explicación de los campos:
- casa: Obligatorio. Representa una de las posibles casas que se pueden reservar. Acepta valores del 1 al 3.
- nombre: Obligatorio. Nombre de la persona que realizó la reserva.
- email: Obligatorio. Email de la persona que realizó la reserva.
- cantidad_adultos: Obligatorio. Cantidad de adultos para la reserva.
- fecha_inicio: Obligatorio. Fecha en la que inicia la reserva.
- fecha_fin: Obligatorio. Fecha en la que termina la reserva.

# Uso del panel de administración

El panel de administración está en la ruta `/admin/` (por ejemplo, `http://localhost:8000/admin/`), desde el también se pueden crear directamente entradas para reservas.