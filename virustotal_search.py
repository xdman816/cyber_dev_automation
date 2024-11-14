#!/usr/bin/env python3

import sys
import requests
import time
import datetime
from cyber_api_key import vt_key

api_key = vt_key
download_hashes = []

if len(sys.argv) > 1:
    for hash in sys.argv[1:]:
        download_hashes.append(hash)

for hash in download_hashes:
    url = f"https://www.virustotal.com/api/v3/files/{hash}"

    headers = {
        "accept": "application/json",
        "x-apikey": api_key
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            file_data = response.json()
            if 'attributes' in file_data:
                print("known virus found!")
                time.sleep(1)
                print(f"this is the data for file hash {hash}:")
                time.sleep(1)
                threat_name = file_data['data']['attributes']['popular_threat_classification']['popular_threat_name']
                print(f"Known threat names tags: {threat_name}")
                first_date = datetime.datetime.fromtimestamp(file_data['data']['attributes']['first_submission_date'])
                print(f"First submitted: {first_date}")
                last_date = datetime.datetime.fromtimestamp(file_data['data']['attributes']['last_submission_date'])
                print(f"Last submitted: {last_date}")
            else: 
                print(f"there is no data for file hash {hash}")
        else: 
            print(f"Unable to fetch data from Virustotal: error code {response.status_code}")
    except Exception as e:
        print(f"Error during VirusTotal API call: {e}")
