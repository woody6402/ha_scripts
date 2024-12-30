import requests
from bs4 import BeautifulSoup
import json
import sys

def fetch_page_data(url):
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the date from the div with class "tabledescription"
    date_div = soup.find('div', class_='tabledescription')
    if date_div:
        date_text = date_div.get_text(strip=True).split('\n')[0]
    else:
        raise ValueError("Date not found in the table description.")

    # Find the table
    table = soup.find('table')
    if not table:
        raise ValueError("Table not found on the page.")
    
    # Extract headers from the table
    thead = table.find('thead')
    headers_row = thead.find('tr') if thead else None
    headers = [th.get_text(strip=True) for th in headers_row.find_all('th')] if headers_row else []

    # Set the first header to 'Ort'
    if headers:
        headers[0] = 'Ort'

    # Extract data rows from the table body
    tbody = table.find('tbody')
    rows = tbody.find_all('tr') if tbody else []
    
    return date_text, headers, rows

def extract_data(row, headers):
    cells = row.find_all('td')
    #print(cells)
    data = {}
    # The first cell is for the location, which corresponds to 'Ort'
    for header, cell in zip(headers[1:], cells[0:]):  # Skip the first header (location header)
        data[header] = cell.get_text(strip=True)
    return data

def main(location):
    url = "http://numbis.noe.gv.at/Numbis/aktuelledaten.jsp"
    date_text, headers, rows = fetch_page_data(url)
    
    if not rows:
        print("No rows found in the table.")
        return

    # Search for the row matching the parameter
    for row in rows:
        th = row.find('th')
        if th and th.get_text(strip=True) == location:
            data = extract_data(row, headers)
            home_assistant_sensor = {
                "state": date_text,
                "attributes": {
                    "Ort": location,
                    **data
                }
            }
            print(json.dumps(home_assistant_sensor, indent=4))
            break
    else:
        print(f"No data found for location {location}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python getNOELuft.py <Ort>")
        sys.exit(1)

    location = sys.argv[1]
    main(location)

