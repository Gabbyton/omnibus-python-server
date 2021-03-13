import requests
import json

from omnibus.transloc.transloc import Transloc

class Vehicles(Transloc):

    def __init__(self, routes="8004946"):
        super(Vehicles, self).__init__()
        self.url = "https://transloc-api-1-2.p.rapidapi.com/vehicles.json"
        self.routes = routes
    
    def get_vehicles(self):
        querystring = {"agencies":self.agency_id,"routes":self.routes,"callback":"call"}
        response = requests.request("GET", self.url, headers=self.headers, params=querystring)
        return json.loads(response.text)['data']