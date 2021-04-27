# Sistema MyShop

Esta carpeta contiene el código fuente del Sistema Myshop. El sistema fue desarrollado utilizando el Framework Django.

## Estructura del Directorio

- .dbdata: Directorio auxiliar para el contenedor myshop_db.
- .docker: Directorio auxiliar para el contenedor myshop_web.
- cart: Directorio que almacena el código fuente de la aplicación Cart.
- catalog: Directorio que almacena el código fuente de la aplicación Catalog.
- myshop: Directorio que almacena el código fuente de la aplicación principal Myshop.
- orders: Directorio que almacena el código fuente de la aplicación Orders.
- static: Directorio que almacena los archivos estáticos para el sistema.
- docker-compose.yml: Archivo que contiene las configuraciones necesarias para la construcción de los contenedores.
- Dockerfile: Archivo que contiene las configuraciones necesarias para el despliegue del sistema.
- manage.py: Archivo para el manejo del sistema desarrollado con el Framework django.
- requirements.txt: Archivo que contiene las dependencias del sistema.


## Prerrequisitos

- Como se mencionó en el archivo README.md del directorio raíz, antes de iniciar el contenedor myshop_web debemos realizar algunos pasos previos (si ya se realizaron, omitir estos pasos). 

    1. Nos dirigimos al archivo myshop/myshop/.env y modificamos los siguientes campos:
        - EMAIL_HOST_USER
        - EMAIL_HOST_PASSWORD
        - DEFAULT_FROM_EMAIL
        
        Esta información es importande debido a que la aplicación envía un correo electrónico cuando se genera una orden, para que esto funcione correctamente es necesario que añada esta información (utilizando un correo gmail).
    
    2. Modificamos la línea 88 del archivo myshop/orders/views.py, en donde se encuentra la etiqueta '<your_email>' colocamos nuestro correo de gmail (el mismo correo agregado en la variable EMAIL_HOST_USER en el archivo .env).

        Ahora que se ha completado el archivo .env procederemos a realizar algunas configuraciones en su cuenta gmail para que permita el envío de correos electrónicos.

    3. Iniciamos sesión en el correo gmail del cual ingresó la información en el archivo .env.

    4. Damos click en nuestro usuario y seleccionamos la opción 'Gestionar tu cuenta de Google'.

    <p align="center">
        <img src="docs/proceso_email.png" width="30%" height="30%">
    </p>

    5. En el menú que se encuentra en el lado izquierdo seleccionamos la opción de 'Seguridad'.

    <p align="center">
        <img src="docs/proceso_email2.png" width="80%" height="80%">
    </p>

    6. Navegamos hasta encontrar el apartado 'Acceso de aplicaciones poco seguras', si se encuentra desactivada la opción, procedemos a activarla.

    <p align="center">
        <img src="docs/proceso_email3.png" width="80%" height="80%">
    </p>

    Nota: Al realizar estos pasos quedaría lista la configuración, posiblemente llegue a su bandeja de correo un email indicando el inicio de sesión, eso se debe a que la aplicación django está haciendo uso de su cuenta para el envío de correos.

    Al momento de subir el proyecto a un repositorio recomendamos remover las credenciales del archivo .env.


## Fuente

- El código base de este proyecto fue obtenido del siguiente repositorio:

   > https://github.com/PacktPublishing/Django-By-Example/tree/master/Chapter%207/myshop


## Versión

1.0.0 - Marzo 2021

## Autores

* **Perla Velasco**
* **Jorge Alfonso Solís**