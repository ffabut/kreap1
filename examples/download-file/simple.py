"""
Program stahne danou stranku a vypise jeji HTML kod do terminalu.
Take vypise status code odpovedi na html dotaz - 200=OK, 404=NotFound atd... 
"""

import requests # requests 

url = "https://favu.vut.cz" # pevne stanovena adresa, pripadne muzete zmenit

response = requests.get(url) 

print(response.status_code)
print(response.text)
