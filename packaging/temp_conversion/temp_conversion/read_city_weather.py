
import sys
import os
import yaml
from datetime import datetime

# TODO: import the appropriate module here

# Obtain the YAML file name from the command line
#-------------------------------------------
file_name = sys.argv[1]

#------------------------------------------------
# Read the YAML file name
# Each section in the YAML file has:
#   - The type of conversion we want to do (key)
#   - A list of values we want to convert
#------------------------------------------------
with open(file_name, 'r') as yaml_file:
     yaml_content = yaml.load(yaml_file, yaml.Loader)

for key in yaml_content:
    mydict = yaml_content[key]
    state = mydict['State']
    lat = mydict['location']['lat']
    lon = mydict['location']['lon']
    elev = mydict['location']['elev']
    temp = mydict['temp']
    date = mydict['date']
    print(f"{key}, {state}")
    print(f"\t Latitude: {lat} Longitude: {lon} Elevation: {elev}")
    date_string = '%d-%m-%YT%H-%M-%S'
    target_format = '%a %b %d %H:%M:%S %Y'
    print(f"\t Date: {datetime.strptime(date, date_string).strftime(target_format)}")
    lastchar = temp[-1]
    val = float(temp.split(lastchar)[0])
    if temp.endswith('F'):
        var = temperature_functions.convert_fahrenheit_to_celsius(val)
    elif temp.endswith('K'):
        var = temperature_functions.convert_kelvin_to_celsius(val)
    elif temp.endswith('C'):
        var = val
    print(f"\t Temperature: {var:.2f} degree C")
