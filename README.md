# ha_scripts
some scripts for home assistant usable via command_line.yaml

# Sensor for NÖ (Lower Austria) air quality
- sensor:
    name: "Air Quality"
    command: "python /config/myscripts/getNOELuft.py 'Bad Vöslau'"
    json_attributes:
      - attributes
    value_template: "{{ value_json.state }}"
    scan_interval: 900  # Update interval in seconds
