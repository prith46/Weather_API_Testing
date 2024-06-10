import requests

# Forecast Request
response = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
                        'Puducherry,India/1997-06-04/?key=68G7LZHXXUU6QR8QR2Q226C55')
data = response.json()
print(data['days'][0]['hours'][17]['temp'])

# Forecast Request Example using longitude and latitude
response = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
                        '11.9416, 79.8083/1997-06-04/?key=68G7LZHXXUU6QR8QR2Q226C55')
data = response.json()
print(data['days'][0]['hours'][17]['temp'])

# Date Range Request Example
response = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
                        'Puducherry,India/1997-06-04/1997-07-04?key=68G7LZHXXUU6QR8QR2Q226C55')
data = response.json()
print(data)

# Date Request Example using UNIX Time (Epoch Time)
response = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
                        'Puducherry,India/865427100/860156700?key=68G7LZHXXUU6QR8QR2Q226C55')
data = response.json()
print(data)

# Date Range Request Example using UNIX Time (Epoch Time)
response = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
                        'Puducherry,India/865427100?key=68G7LZHXXUU6QR8QR2Q226C55')
data = response.json()
print(data)

# Specific Time Request Example for every hour
response = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
                        'Puducherry,India/2020-12-15T13:00:00?key=68G7LZHXXUU6QR8QR2Q226C55')
data = response.json()
print(data)

# Specific Time Request Example
response = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
                        'Puducherry,India/2020-12-15T13:00:00?key=68G7LZHXXUU6QR8QR2Q226C55&include=current')
data = response.json()
print(data)

# Dynamic period Request Example
response = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
                        'Puducherry,India/last10days?key=68G7LZHXXUU6QR8QR2Q226C55')
data = response.json()
print(data)

# Using elements list and options parameter to request only daily with limited elements
response = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
                        'Puducherry,India/last10days?key=68G7LZHXXUU6QR8QR2Q226C55&include=days&elements=tempmax,'
                        'tempmin,temp')
data = response.json()
print(data)

# Degree day elements list example
response = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
                        'Puducherry,India/last30days?unitGroup=us&key=68G7LZHXXUU6QR8QR2Q226C55&include=days&'
                        'elements=datetime,tempmax,tempmin,degreedays,accdegreedays&degreeDayTempMaxThreshold=86&'
                        'degreeDayTempBase=50')
data = response.json()
print(data)

# Historical forecast example
response = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
                        'Puducherry,India/2023-05-01/2023-05-15?unitGroup=us&key=YOUR_API_KEY&include=days&'
                        'forecastBasisDate=2023-05-01')
data = response.json()
print(data)
