# Se indica qué tipo de proyecto es, incluyendo la versión del lenguaje
FROM python:3.9

# Se agrega para obtener logs
ENV PYTHONUNBUFFERED 1

# Se indica el working directory
WORKDIR /app

# Se copia el documento requirements.txt al working directory del contenedor
COPY requirements.txt /app/requirements.txt

# Se instalan los requerimientos indicados en el archivo con ayuda de pip
RUN pip install -r requirements.txt

# Se copian todos los archivos al working directory del contenedor
COPY . /app

# Se ejecuta el proyecto indicando el host y el puerto
CMD python manage.py runserver 0.0.0.0:8000