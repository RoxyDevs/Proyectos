import os
from dotenv import load_dotenv

# Cargar variables de entorno desde un archivo .env
load_dotenv()

class Config:
    # Configuración de la base de datos
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///sensor_data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Clave secreta para Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'una_clave_secreta_muy_segura')