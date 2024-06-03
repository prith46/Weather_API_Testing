import requests

response = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/['
                        'Puducherry,India]/1997-06-04/?key=68G7LZHXXUU6QR8QR2Q226C55')
data = response.json()
print(data['days'][0]['hours'][17]['temp'])
