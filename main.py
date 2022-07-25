import requests
from  pprint import pprint
import json
def http_request():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    # params = {"model": "nike123"}
    # headers = {"Authorization": "secret - token - 123"}
    response = requests.get(url)
    pprint(response.json())
    with open('superheroes.json', 'w') as f:
       json.dump(response.json(), f)



if __name__ == '__main__':
    http_request()
