from influxdb import InfluxDBClient
import arrow

from itertools import cycle
from pathlib import Path
import json
import time

project_path = Path(__file__).parent

with open(Path(project_path, 'MOCK_DATA.json'), 'r') as jsonfile:
    mock_data = json.load(jsonfile)

payloads = cycle(mock_data)

database = 'plants'

client = InfluxDBClient('localhost', 8086, database=database)
client.create_database(database)

for p in payloads:
    json_body = [
        {
            "measurement": "tropical",
            "tags": {
                "environment": "development"
            },
            "time": str(arrow.utcnow()),
            "fields": p
        }
    ]
    time.sleep(1)
    client.write_points(json_body)
    result = client.query('select value from tropical;')
    print(f"Result: {result}")

