from influxdb import InfluxDBClient
import arrow

from itertools import cycle
from pathlib import Path
import json
import time
from pprint import pprint

project_path = Path(__file__).parent

with open(Path(project_path, 'MOCK_DATA.json'), 'r') as jsonfile:
    mock_data = json.load(jsonfile)

payloads = cycle(mock_data)

database = 'plants'

client = InfluxDBClient(host='localhost', port=8086, database=database)
client.create_database(database)

for p in payloads:
    json_body = [{
        "measurement": "tropical",
        "tags": {
            "environment": "development"
        },
        "time": str(arrow.utcnow()),
        "fields": p
    }]
    time.sleep(2)
    client.write_points(json_body)
    result = client.query('select * from tropical order by desc limit 1;')

    print(client.get_list_database())
    print(client.get_list_continuous_queries())
    print(client.get_list_retention_policies())
    print(client.get_list_measurements())
