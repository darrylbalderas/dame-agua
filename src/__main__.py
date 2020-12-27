from influxdb import InfluxDBClient
import arrow

from itertools import cycle
from pathlib import Path
import json
import time

project_path = Path(__file__).parent


def main():
    with open(Path(project_path, 'mock_data.json'), 'r') as jsonfile:
        mock_data = json.load(jsonfile)

    # TODO: Create a config class to handle reading environment variables

    database = 'house-plants'
    measurement = 'monitoring'

    client = InfluxDBClient(host='localhost', port=8086, database=database)
    client.create_database(database)

    for data in cycle(mock_data):
        json_body = [{
            "measurement": measurement,
            "tags": {},
            "time": str(arrow.utcnow()),
            "fields": data
        }]
        time.sleep(2)
        client.write_points(json_body)

        result = client.query(f'select * from {measurement} order by desc limit 1;')
        print(result)
