# ha_scripts
some scripts for home assistant usable via command_line.yaml

- NÖ air quality
```
# Sensor for NÖ (Lower Austria) air quality
# http://numbis.noe.gv.at/Numbis/aktuelledaten.jsp
- sensor:
    name: "Air Quality"
    command: "python /config/myscripts/getNOELuft.py 'Bad Vöslau'"
    json_attributes:
      - attributes
    value_template: "{{ value_json.state }}"
    scan_interval: 900  # Update interval in seconds
```
- water level for different rivers
```
# Stationsname: Cholerakapelle, Stationsnummer:208090
  - sensor:
    name: "Pegelstand_KlLe"
    command: "/config/myscripts/getWasserPegelCholera.sh 208090"
    unit_of_measurement: "cm"
    value_template: "{{ value.split(';')[1] | trim | float(1) }}"  # Extracts the second value (Pegelstand)
    command_timeout: 60
    scan_interval: 900  # Adjust the interval as needed
    json_attributes:
      time: "{{ value.split(';')[0] | trim }}"  # Extracts the first value (timestamp)
```
