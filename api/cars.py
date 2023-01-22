from flask import Blueprint, request, jsonify
import requests
from flask_restful import Api, Resource

# Creating a Flask blueprint and API routing
cars_api = Blueprint('cars_api', __name__ ,
                    url_prefix='/api/cars')

# API instance from flask_restful
api = Api(cars_api)

# Get request for the API
def carsAPI():
    global cars_api  
    try: cars_info
    except: cars_info = None
       
    url = "https://car-data.p.rapidapi.com/cars"

    querystring = {"limit":"49","page":"0"}

    headers = {
	"X-RapidAPI-Key": "d3a3e94748msh74bb629320d5734p160ceajsn7f28f4859ea2",
	"X-RapidAPI-Host": "car-data.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    cars_info = response
    return response

# Get method + json of the response
class CarsAPI(Resource):
    def get(self):
        response = carsAPI()
        return response.json()

api.add_resource(CarsAPI, '/')