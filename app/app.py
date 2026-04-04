#!/usr/bin/env python3
"""
Air Quality Dashboard Backend
Proxies requests to Home Assistant API and serves the static dashboard.
"""

import os
from flask import Flask, jsonify, send_from_directory
import requests

app = Flask(__name__, static_folder='static')

# Configuration from environment variables
HA_URL = os.environ.get('HA_URL', 'http://homeassistant.local:8123')
HA_TOKEN = os.environ.get('HA_TOKEN', '')

# Entity IDs - customize these to match your Home Assistant setup
ENTITIES = {
    'aqi': os.environ.get('ENTITY_AQI', 'sensor.air_quality_aqi'),
    'pm1': os.environ.get('ENTITY_PM1', 'sensor.air_quality_pm1'),
    'pm25': os.environ.get('ENTITY_PM25', 'sensor.air_quality_pm25'),
    'pm40': os.environ.get('ENTITY_PM40', 'sensor.air_quality_pm40'),
    'pm10': os.environ.get('ENTITY_PM10', 'sensor.air_quality_pm10'),
    'temperature': os.environ.get('ENTITY_TEMP', 'sensor.air_quality_temperature'),
    'humidity': os.environ.get('ENTITY_HUMIDITY', 'sensor.air_quality_humidity'),
    'heat_index': os.environ.get('ENTITY_HEAT_INDEX', 'sensor.air_quality_heat_index'),
    'dew_point': os.environ.get('ENTITY_DEW_POINT', 'sensor.air_quality_dew_point'),
    'pressure': os.environ.get('ENTITY_PRESSURE', 'sensor.air_quality_pressure'),
    'aqi_corrected': os.environ.get('ENTITY_AQI_CORRECTED', 'sensor.outdoor_pm2_5_corrected_aqi')
}


def get_ha_state(entity_id):
    """Fetch the state of a single entity from Home Assistant."""
    headers = {
        'Authorization': f'Bearer {HA_TOKEN}',
        'Content-Type': 'application/json',
    }
    
    try:
        response = requests.get(
            f'{HA_URL}/api/states/{entity_id}',
            headers=headers,
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        return data.get('state')
    except requests.RequestException as e:
        app.logger.error(f'Error fetching {entity_id}: {e}')
        return None


@app.route('/')
def index():
    """Serve the main dashboard."""
    return send_from_directory('static', 'index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static/images', 'favicon.ico')


@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory('static/images', filename)


@app.route('/learn/')
def learn():
    """Serve the learn page."""
    return send_from_directory('static/learn', 'index.html')


@app.route('/api/sensors')
def get_sensors():
    """Fetch all sensor data from Home Assistant."""
    data = {}
    
    for key, entity_id in ENTITIES.items():
        state = get_ha_state(entity_id)
        if state is not None and state not in ('unknown', 'unavailable'):
            try:
                data[key] = float(state)
            except ValueError:
                data[key] = state
    
    return jsonify(data)


@app.route('/api/health')
def health():
    """Health check endpoint."""
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
