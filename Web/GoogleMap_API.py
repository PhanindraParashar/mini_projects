import numpy as np
import googlemaps
from datetime import datetime

class GoogleMap:
    
    def __init__(self):
        API = 'AIzaSyBBdRlOdK9PQJgMuYSHF4GjfE4QJdnSx1Q'
        gmaps = googlemaps.Client(key=API)
    
    def distance_places(self,place1,place2):
        dist = gmaps.distance_matrix(place1,place2)['rows'][0]['elements'][0]
        distance_km = dist['distance']['value']/1000
        time_hr = dist['duration']['value']/3600
        
        return distance_km,time_hr
    
    def get_coordinates(self,location):
        geocode_result = gmaps.geocode(location)
        latitude = geocode_result[0]['geometry']['location']['lat']
        longitude = geocode_result[0]['geometry']['location']['lng']
        
        return latitude,longitude
    
    def Distance_Time_Matrix(self,List):
        Ncities = len(List)
        Dist = []
        Time = []
        for i in List:
            for j in List:
                if i==j :
                    dist_km = 0
                    time_hr = 0
                else:
                    dist_km = self.distance_places(i,j)[0]
                    time_hr = self.distance_places(i,j)[1]
                Dist.append(dist_km)
                Time.append(time_hr)
        Matrix_D = np.array(Dist).reshape(Ncities,Ncities)
        Matrix_T = np.array(Time).reshape(Ncities,Ncities)     
        
        return Matrix_D,Matrix_T
