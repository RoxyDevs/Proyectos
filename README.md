# Proyectos

Acerías 4C OBRA: Implementación de herramientas de digitalización industrial + Industria 4.0

## Descripción del Proyecto

Este proyecto implementa un backend para la digitalización industrial y la Industria 4.0 en una acería. El backend utiliza Flask y SQLAlchemy para manejar datos de sensores y generar métricas clave para la optimización de la producción.

## Estructura del Proyecto

```
Proyectos/
└── digitalizacion_aceria/
    ├── backend/
    │   ├── app.py
    │   ├── config.py
    │   ├── lorawan.py
    │   ├── models.py
    │   ├── utils.py
    │   └── tests/
    │       ├── test_app.py
    │       └── test_models.py
    └── requirements.txt
    └── .env
```

## Configuración del Proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/RoxyDevs/Proyectos.git
cd Proyectos/digitalizacion_aceria
```

### 2. Crear y activar un entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar las variables de entorno

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
DATABASE_URL=sqlite:///sensor_data.db
SECRET_KEY=una_clave_secreta_muy_segura
```

### 5. Inicializar la base de datos

```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

## Ejecución del Proyecto

Para ejecutar el servidor Flask, usa el siguiente comando:

```bash
flask run
```

El servidor estará disponible en `http://127.0.0.1:5000/`.

## Pruebas

Para ejecutar las pruebas, usa el siguiente comando:

```bash
pytest
```

## Contribución

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.