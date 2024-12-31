import json
import subprocess
import sys

def fetch_data():
    """
    Fetches the JSON data using the given curl command.
    :return: JSON string or None if the fetch fails
    """
    curl_command = [
        "curl",
        "https://hydrographie.ktn.gv.at/DE/repos/evoscripts/hydrografischer/getFluesseWasserstand.es?_=1735601419382",
        "-H", "Accept: application/json, text/javascript, */*; q=0.01",
        "-H", "Accept-Language: de-AT,de;q=0.9,en-AT;q=0.8,en;q=0.7,de-DE;q=0.6,en-US;q=0.5",
        "-H", "Connection: keep-alive",
        "-H", "Cookie: websidprjpflegeanwaltschaft=258C04601A0E7864c6fb62b1797947909491a02fa8ab; _l42cc_confirmed=false",
        "-H", "Referer: https://hydrographie.ktn.gv.at/gewasser/fluesse-wasserstaende",
        "-H", "Sec-Fetch-Dest: empty",
        "-H", "Sec-Fetch-Mode: cors",
        "-H", "Sec-Fetch-Site: same-origin",
        "-H", "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "-H", "X-Requested-With: XMLHttpRequest",
        "-H", 'sec-ch-ua: "Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "-H", "sec-ch-ua-mobile: ?0",
        "-H", 'sec-ch-ua-platform: "Linux"'
    ]

    try:
        result = subprocess.run(curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout  # Return the fetched JSON string
    except subprocess.CalledProcessError as e:
        print(f"Error fetching data: {e}")
        return None

def filter_by_station(json_input, station_name):
    """
    Filters the JSON data to find the record for the specified station.
    :param json_input: JSON string containing the data
    :param station_name: Name of the station to filter by
    :return: Dictionary of the matching record or None if not found
    """
    try:
        data = json.loads(json_input)  # Parse the JSON input
        for record in data.get("data", []):  # Iterate through the records
            if station_name.lower() in record.get("station", "").lower():  # Match the station
                return record
        return None  # Return None if no matching station is found
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <station_name>")
        sys.exit(1)
    
    station_name = sys.argv[1]

    # Fetch data from the server
    json_data = fetch_data()
    if not json_data:
        print("Failed to fetch data.")
        sys.exit(1)

    # Filter data by station
    result = filter_by_station(json_data, station_name)
    if result:
        print(json.dumps(result, indent=4))
    else:
        print(f"No data found for station: {station_name}")

