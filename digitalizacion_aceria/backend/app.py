from flask import Flask, render_template, request
from backend.models import SensorData, db
from datetime import datetime, timezone

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)

@app.route('/')
def index():
    latest_data = SensorData.query.order_by(SensorData.timestamp.desc()).limit(10).all()
    return render_template('index.html', data=latest_data)

@app.route('/historical')
def historical():
    start_date = datetime.strptime(request.args.get('start_date'), '%Y-%m-%d').replace(tzinfo=timezone.utc)
    end_date = datetime.strptime(request.args.get('end_date'), '%Y-%m-%d').replace(tzinfo=timezone.utc)
    historical_data = SensorData.query.filter(SensorData.timestamp.between(start_date, end_date)).all()
    return render_template('historical.html', data=historical_data)

if __name__ == '__main__':
    app.run(debug=True)