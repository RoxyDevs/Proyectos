# Proyectos
Acerías 4C OBRA: Implementación de herramientas de digitalización industrial + Industria 4.0


# Digitalización de Planta de Acería con LoRa y Python

Este proyecto tiene como objetivo digitalizar una planta de acería mediante la implementación de tecnología LoRa para la recolección de datos y Python para el desarrollo del servidor, la base de datos y la interfaz de usuario.

## Funcionalidades
- **Información en Tiempo Real**: Visualización de los últimos 10 registros del caudalímetro.
- **Información Histórica**: Consulta de datos históricos con filtros de rango de fechas.
- **Volumen de Aire Consumido**: Almacenamiento y consulta del volumen de aire consumido.
- **Ahorro Energético**: Cálculo de métricas y estadísticas para mejorar la productividad.

## Estructura del Proyecto

digitalizacion_acería/
│
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── lorawan.py
│   ├── utils.py
│   ├── requirements.txt
│   ├── config.py
│   ├── migrations/
│   └── tests/
│       ├── test_app.py
│       └── test_models.py
│
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   ├── js/
│   │   │   └── main.js
│   │   └── images/
│   └── templates/
│       ├── index.html
│       ├── historical.html
│       └── layout.html
│
├── README.md
├── .gitignore
└── .env

## Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/digitalizacion_acería.git

pip install -r backend/requirements.txt

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

python backend/app.py

## Contribución

Si deseas contribuir al proyecto, por favor abre un issue o envía un pull request.

## Licencia
Este proyecto está bajo la licencia MIT.

