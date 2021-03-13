from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin

from omnibus.transloc.routes import Routes
from omnibus.transloc.segment import Segment
from omnibus.transloc.vehicles import Vehicles
from omnibus.transloc.times import Times
from omnibus.transloc.stops import Stops

app = Flask(__name__)
cors = CORS(app)
api = Api(app)

routesObj = None
vehiclesObj = None
segmentObj = None
timesObj = None
stopsObj = None


class start_up(Resource):
    def post(self):
        global routesObj, vehiclesObj, segmentObj, timesObj, stopsObj
        routesObj = Routes()
        segmentObj = Segment()
        vehiclesObj = Vehicles()
        timesObj = Times()
        stopsObj = Stops()

class get_stops(Resource):
    def get(self):
        global stopsObj
        if stopsObj == None:
            stopsObj = Stops()
        return stopsObj.get_stops()

class get_routes(Resource):
    def get(self):
        global routesObj
        if routesObj == None:
            routesObj = Routes()
        return routesObj.get_shuttle_routes()

class get_vehicles(Resource):
    def get(self):
        global vehiclesObj
        if vehiclesObj == None:
            vehiclesObj = Vehicles()
        return vehiclesObj.get_vehicles()

class get_segment(Resource):
    def get(self):
        global segmentObj
        if segmentObj == None:
            segmentObj = Segment()
        return segmentObj.get_segment()

class get_times(Resource):
    def get(self):
        global timesObj
        if timesObj == None:
            timesObj = Times()
        return timesObj.get_shuttle_times()

api.add_resource(start_up, '/start-up')
api.add_resource(get_stops, '/get-stops')
api.add_resource(get_routes, '/get-routes')
api.add_resource(get_vehicles, '/get-vehicles')
api.add_resource(get_times, '/get-times')
api.add_resource(get_segment, '/get-segment')
