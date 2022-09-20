import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'N':75, 'P':38, 'K':45, 'temperature':22 , 'humidity':80 , 'ph':7 , 'rainfall':250 })

print(r.json())