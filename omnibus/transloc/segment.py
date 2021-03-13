import requests
import json

from omnibus.transloc.transloc import Transloc

class Segment(Transloc):

    def __init__(self, route="8004962"):
        super(Segment, self).__init__()
        self.url = "https://transloc-api-1-2.p.rapidapi.com/segments.json"
        self.route = route

    def get_segment(self):
        querystring = {"agencies":self.agency_id,"routes":self.route,"callback":"call"}
        response = requests.request("GET", self.url, headers=self.headers, params=querystring)
        return json.loads(response.text)['data']
