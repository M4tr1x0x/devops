# Usamos una imagen base de Python
FROM python:3.8-slim

# Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos el archivo de requerimientos primero para aprovechar la cache de Docker
COPY transactions/requirements.txt .

# Instalamos las dependencias
RUN pip install -r requirements.txt

# Copiamos el resto del código fuente del servicio de transacciones al directorio de trabajo
COPY transactions/ .

# Especificamos el comando para ejecutar la aplicación
CMD ["python", "app.py"]
