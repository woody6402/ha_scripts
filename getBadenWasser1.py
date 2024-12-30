import requests
from bs4 import BeautifulSoup
import json

# Step 1: Fetch the webpage
url = "https://www.baden.at/Unsere_Stadt/Umwelt/Wasserwerk/Wasserwerte"
response = requests.get(url)

# Ensure the page loaded correctly
if response.status_code == 200:
    # Step 2: Parse the webpage content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Step 3: Find the table data (based on inspection of the HTML structure)
    table_rows = soup.find_all('tr')
    
    # Step 4: Create a dictionary to store table data
    water_data = {}
    analysis_date = None
    
    # Step 5: Loop through each row and extract data
    for row in table_rows:
        cells = row.find_all('td')
        if len(cells) == 3:  # Ensure we have the right number of columns
            parameter = cells[0].get_text(strip=True)
            value = cells[1].get_text(strip=True)
            max_value = cells[2].get_text(strip=True)
            
            # Check if the current row contains 'Analysedatum'
            if 'Analysedatum' in parameter:
                analysis_date = value  # Assumes date is in the value field
                continue  # Skip adding 'Analysedatum' to water_data
            
            # Add the extracted data to the dictionary
            water_data[parameter] = {
                "value": value,
                "max_value": max_value
            }
    
    # Step 6: Create the Home Assistant sensor format
    home_assistant_sensor = {
        "state": analysis_date,
        "attributes": water_data
    }
    
    # Convert the output to JSON format
    json_output = json.dumps(home_assistant_sensor, indent=4)
    
    # Output the JSON data
    print(json_output)

else:
    print("Failed to load the webpage.")

