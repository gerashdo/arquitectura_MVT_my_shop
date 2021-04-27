# Aplicación Cart - Sistema de Compras Myshop

Esta carpeta contiene el código fuente de la aplicación Cart, la cual forma parte del Sistema MyShop. El sistema fue desarrollado utilizando el Framework Django.

## Estructura del Directorio

- migrations: Directorio que almacena archivos relacionados con las migraciones de la aplicación.
- templates: Directorio que almacena los templates (archivos html) de la aplicación.
- admin.py: Archivo en donde se registran las configuraciones para la aplicación de administración.
- cart.py: Archivo que contiene la clase Cart.
- context_processors.py: Archivo que contiene el procesador para el carrito de compras.
- forms.py: Archivo en donde se definen los formularios de la aplicación.
- models.py: Archivo en donde se definen los modelos de la aplicación.
- test.py: Archivo en donde se definen las pruebas de la aplicación.
- urls.py: Archivo en donde se definen las urls para acceder a las vistas de la aplicación.
- views.py: Archivo en donde se definen las vistas de la aplicación.


## Prerrequisitos

- Como se mencionó en el archivo README.md del directorio raíz, antes de iniciar el contenedor myshop_web debemos realizar algunos pasos previos (si ya se realizaron, omitir estos pasos). 
    
    1. Modificamos la línea 88 del archivo myshop/orders/views.py, en donde se encuentra la etiqueta '<your_email>' colocamos nuestro correo de gmail (el mismo correo agregado en la variable EMAIL_HOST_USER en el archivo .env).

    Al momento de subir el proyecto a un repositorio recomendamos remover el email añadido.


## Fuente

- El código base de este proyecto fue obtenido del siguiente repositorio:

   > https://github.com/PacktPublishing/Django-By-Example/tree/master/Chapter%207/myshop


## Versión

1.0.0 - Marzo 2021

## Autores

* **Perla Velasco**
* **Jorge Alfonso Solís**