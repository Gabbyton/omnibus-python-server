from omnibus.utils.utils import Utils

class Transloc():
    
    def __init__(self):
        self.utilsObj = Utils()
        self.api_key = self.utilsObj.get_api_key()
        self.headers = {
            'x-rapidapi-host': "transloc-api-1-2.p.rapidapi.com",
            'x-rapidapi-key': self.api_key
        }
        self.agency_id = "1199"