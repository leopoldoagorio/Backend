## Lista de comandos útiles

- Para instalar django usando el gestor pip:

```bash
pip install django
```

- Para crear una carpeta de trabajo con nombre `name`:

```bash
django -admin startproject name
```

- Para correr el servidor

```bash
py .\manage.py runserver
```

Esto devuelve una dirección al servidor local que crea django. 

- Para crear una aplicación con nombre base a partir de un template:

```bash
py .\manage.py startup base
```
Para agregar a cheep la aplicación hay que agregar el arcivo cheep/settings.py en la lista `INSTALLED_APPS` el elemento `base.apps.BaseConfig`

### Modelos

Para crear una clase en la base de datos a partir de una definida en los modelos se usa:

```bash
py .\manage.py makemigrations
py .\manage.py migrate
```

### Logins

Para crear un superuser de la aplicación se usa:

```
py .\manage.py createsuperuser
```

### Admin

user:leopo
pass: 12345