# ha_scripts
some scripts for home assistant usable via command_line.yaml
please beware, that are quick code snippets to retrieve some interesting values, not improved and not secured, as base for personal adaptations

In my configuration all scripts are located in myscripts.

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
- water level for different Lower Austrian rivers measured on different locations.
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
- Baden water quality (see package waterq.yaml)
```
command_line:
  - sensor:
      name: "Wasserwerte Baden (CLI Rohdaten)"
      unique_id: wasserwerte_baden_cli_rohdaten
      command: "curl -sSL 'https://raw.githubusercontent.com/woody6402/ha_scripts/main/myscripts/baden_wasserwerte.json'"
      scan_interval: 86400
      value_template: "{{ value_json.Probe.ProbenahmeDatum }}"
      json_attributes_path: "$.Messwerte"
      json_attributes:
        - Wassertemperatur
        - pH_Wert
        - Leitfähigkeit
        - Färbung
        - Geruch
        - Geschmack
        - Gesamthärte_mmol_l
        - Gesamthärte_dH
        - Carbonathärte
        - Säurekapazität_bis_pH_4_3
        - Hydrogencarbonat
        - Calcium_Ca
        - Magnesium_Mg
        - NPOC
        - Nitrat
        - Nitrit
        - Ammonium
        - Chlorid_Cl
        - Sulfat
        - Eisen_Fe
        - Mangan_Mn
        - Natrium_Na
        - Kalium_K
        - Koloniebildende_Einheiten_22C
        - Koloniebildende_Einheiten_37C
        - Escherichia_coli
        - Coliforme_Bakterien
        - Intestinale_Enterokokken

```
- water level Kärnten (yaml config untestet, script is working)
```
- sensor:
    - name: "Pegelstand KW Edling"
      command: "python /config/myscripts/getPegelKaernten.py Edling"
      value_template: "{{ value_json.level }}"
      json_attributes:
        - bs
        - datum
        - einzugsgebiet
        - gewasser
        - group
        - hq1
        - hq10
        - hq100
        - hq30
        - hq300
        - hq5
        - metrics
        - mjnqt
        - mq
        - nqkrit
        - nqt
        - pegelnullpunkt
        - rhhq
        - station
        - stationsbetreiber
        - stationsnummer
        - webgrafik
      scan_interval: 3600

```
