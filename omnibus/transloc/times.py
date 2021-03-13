import requests
import json

from omnibus.transloc.transloc import Transloc


class Times(Transloc):
    def __init__(self, routes="8004962"):
        super(Times, self).__init__()
        self.url = "https://transloc-api-1-2.p.rapidapi.com/arrival-estimates.json"
        self.routes = routes

    def get_shuttle_times(self):
        querystring = {"routes": self.routes,
                       "callback": "call", "agencies": self.agency_id}
        response = requests.request(
            "GET", self.url, headers=self.headers, params=querystring)
        times = json.loads(response.text)
        return times['data']
