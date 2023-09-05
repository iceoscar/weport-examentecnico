# WEPORT - Examen técnico

## Objetivo

<p>Crear un sistema para que el departamento de recursos humanos registre, actualize y realize la baja de los empleados</p>

## Herramientas
- Python - lenguaje de desarrollo, version 3.10
- Django - Framwework del lenguaje Python, version 4.2
- MySQL - Base de datos, Usar la version 8 para compatibilidad de Django 4.2 

## Requisitos previos
- Tener instalado Python version 3.10
- Tener instalada MySQL version 8
- Crear la base de datos en MySQL
- Iniciar un ambiente virtual con Python

## Instalación
<p>Con el ambiente virtual iniciado instalar el archivo <b>requirements.txt</b></p>

```python
pip install requirements.txt
```

<p>Creamos el archivo .env dentro de la carpeta src</p>

```python
touch src/.env
```

<p>Dentro del archivo <b>.env</b> agregamos las variables de entorno</p>

```python
SECRET_KEY=<String alphanumeric + special characters>
DEBUG=False
ALLOWED_HOSTS=<server-IP>

DATABASE_URL=<Database connection URLs>
```

<p>Para la variable <b>SECRET_KEY</b> se puede usar la siguiente cadena de texto:</p>

```python
# Se recomienda para ambientes productivos usar cadenas de texto complejas
SECRET_KEY=django-insecure-a%1o644rc21jpm0e$6%feo9!klm(oi7%g#uv)w5khu#r7@bax3
```

<p>Para la variable <b>ALLOWED_HOSTS</b> se puede obtener mediante el ipconfig (para Windows) o ifconfig (para Linux o mac) y es el valor de <b> Dirección IPv4</b></p>
<p>Para la variable <b>DATABASE_URL</b> se debe usar el modo URL para la conexión a la base de datos</p>

```python
DATABASE_URL=mysql://USER:PASS@SERVER_IP:PORT/DB_NAME
```

<p>Ir a la carpeta <i>src</i> del proyecto</p>

```python
cd src
```

<p>Instalar las migraciones del proyecto</p>

```python
python manage.py migrate
```

<p>Creamos el usuario administrador</p>

```python
python manage.py createsuperuser

# Completamos el Wizard
Nombre de usuario (leave blank to use 'foo'): <username>
Dirección de correo electrónico: <optional, press enter to jump step>
Password:
Password (again):
Superuser created successfully.
```

## Ejecución
<p>Iniciar el proyecto con el siguiente comando</p>

```python
python manage.py runserver <IP_SERVER>:<PORT>
# Ejemplo
python manage.py runserver 192.168.1.245:8080
```