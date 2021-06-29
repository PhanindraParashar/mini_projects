import numpy as np
from geopy import geocoders
from geopy.exc import GeocoderTimedOut 
from geopy.geocoders import Nominatim 
from geopy import distance
from geopy import Point

class GeoData:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="TSP")
        
    def get_coordinates(self,city):
        city_data = self.geolocator.geocode(city)
        lat,lng = city_data.latitude,city_data.longitude
        return lat,lng
    
    def get_distance_between_cities(self,citya,cityb):
        a = Point(self.get_coordinates(citya))
        b = Point(self.get_coordinates(cityb))
        return distance.distance(a,b).kilometers
    
    def get_distance_between_cities_from_coord(self,lat1,lng1,lat2,lng2):
        a = Point(lat1,lng1)
        b = Point(lat2,lng2)
        return distance.distance(a,b).kilometers
    
    def get_dict_coordinates(self,cities):
        return {i:self.get_coordinates(i) for i in cities}
    
    def get_distance_matrix(self,cities):
        n_cities = len(cities)
        m = np.zeros((n_cities,n_cities))
        d = self.get_dict_coordinates(cities)
        for i in range(len(cities)):
            for j in range(i,len(cities)):
                if i == j:
                    m[i][j] = 0
                else:
                    lat1,lng1 = d[cities[i]]
                    lat2,lng2 = d[cities[j]]
                    dist = self.get_distance_between_cities_from_coord(lat1,lng1,lat2,lng2)
                    m[i][j] = dist
                    m[j][i] = dist
        return m
        