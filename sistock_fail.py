import sys
import os
import requests

ENDPOINT = 'https://sandbox.sistock.org/app/export/?op=delivery1'

if not os.getenv('SISTOCK_BASIC_AUTH'):
    print("ERROR: env var SISTOCK_BASIC_AUTH must be set")
    sys.exit(1)

auth = os.getenv('SISTOCK_BASIC_AUTH')

header = {
    'Authorization': f'Basic {auth}',
}

response = requests.get(ENDPOINT, headers=header)
print(f"Response from {ENDPOINT}: {response.status_code}")
