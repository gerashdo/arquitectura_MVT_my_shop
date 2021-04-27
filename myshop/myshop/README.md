# Sistema de Compras MyShop

Esta carpeta contiene código fuente del Sistema MyShop. El sistema fue desarrollado utilizando el Framework Django.

## Estructura del Directorio

- .env: Archivo que almacena variables de entorno para el sistema.
- asgi.py: Archivo que almacena las configuraciones ASGI del sistema.
- settings.py: Archivo que almacena las configuraciones generales del sistema.
- urls.py: Archivo en donde se definen las urls para acceder a las vistas del sistema.
- views.py: Archivo en donde se definen las vistas del sistema.
- wsgi.py: Archivo que almacena las configuraciones WSGI para el despliegue del sistema.


## Prerrequisitos

- Como se mencionó en el archivo README.md del directorio raíz, antes de iniciar el contenedor myshop_web debemos realizar algunos pasos previos (si ya se realizaron, omitirlos). 

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
        <img src="docs/proceso_email2.png" width="70%" height="70%">
    </p>

    6. Navegamos hasta encontrar el apartado 'Acceso de aplicaciones poco seguras', si se encuentra desactivada la opción, procedemos a activarla.

    <p align="center">
        <img src="docs/proceso_email3.png" width="70%" height="70%">
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