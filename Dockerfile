FROM alpine

# Instalamos python3 y actualizamos pip
RUN apk update \
    && apk add --no-cache python3 \
    && pip3 install --upgrade pip

# Instalamos las dependencias necesarias de la aplicación
COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt

# Copiamos el código de la aplicación y los archivos estáticos necesarios
COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/

# Indicamos el puerto que tiene que exponer
EXPOSE 5000

# Ejecutamos la aplicación
CMD ["python3", "/usr/src/app/app.py"]
