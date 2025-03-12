from datetime import datetime, timedelta, timezone
from .models import SensorData, db

def calculate_air_volume(start_date, end_date):
    """
    Calcula el volumen total de aire consumido en un rango de fechas.
    """
    data = SensorData.query.filter(SensorData.timestamp.between(start_date, end_date)).all()
    total_volume = sum(entry.value for entry in data)
    return total_volume

def calculate_energy_saving(start_date, end_date):
    """
    Calcula el ahorro energético basado en el volumen de aire consumido.
    """
    total_volume = calculate_air_volume(start_date, end_date)
    # Supongamos que 1 unidad de volumen de aire ahorra 0.5kWh
    energy_savings = total_volume * 0.5
    return energy_savings

def generate_metrics():
    """
    Genera métricas clave para la optimización de la producción.
    """
    end_date = datetime.now(timezone.utc)
    start_date = end_date - timedelta(days=7)  # Últimos 7 días

    total_volume = calculate_air_volume(start_date, end_date)
    energy_savings = calculate_energy_saving(start_date, end_date)

    return {
        "total_volume": total_volume,
        "energy_savings": energy_savings,
        "start_date": start_date,
        "end_date": end_date
    }
