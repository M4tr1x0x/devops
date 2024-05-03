# Dockerfile

# Usa una imagen base oficial de Python
FROM python:3.8-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de la aplicación al directorio de trabajo
COPY app.py .

# Comando para ejecutar la aplicación
CMD ["python", "./app.py"]
