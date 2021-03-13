class Utils():

    def get_api_key(self):
        f= open('api_key.txt','r')
        return f.read()