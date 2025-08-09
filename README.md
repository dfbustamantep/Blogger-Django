# Arquitectura de Django
- Patron MTV (Model-Template-View)

# 
```py
python -m venv venv
venv/Scripts/activate
```

- Instalar Django
```py
pip install django
```
- Crear la aplicacion 
```py
django-admin startproject [nombre_del_proyecto]
```
- El archivo manage.py nos permite ejectuar todos los comandos de nuestra aplicacion
```py
python manage.py runserver
```
- El archivo vercel.json se usa para definir las configuraciones que requerimos
- El archivo wsgi.py es el archivo que conecta django y vercel
- El archivo build_files.sh ejecuta comandos en el servidor para que nuestro programa funcione
- El comando collecstatic se usa para que todos los archivos estaticos esten comprimidos y se pueda usar en produccion
- Archivos estaticos Son los archivos donde definimos estilos o imagenes

- Vamos a crear una nueva aplicacion
```py
django-admin startapp apiBlogger
```
- Migrar todos los cambios que hemos hecho a la base de datos
```py
python manage.py migrate
```
- Crear un superusuario
```py
python manage.py createsuperuser
```
- Verificamos si hay migraciones 
```py
python manage.py makemigrations
```
- Hacemos las migraciones
```py
python manage.py migrate
```

pip install django-environ
