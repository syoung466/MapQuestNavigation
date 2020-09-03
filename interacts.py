# Samantha Young 59566370

import json
import urllib.request
import urllib.parse

APIKEY = 'CT86q8UfrhVBb3saybvLUj9YoTAymynO'


def directions_url(locations: [str]):
    ''' Creates a url for directions '''
    locations_list = []
    url = 'http://open.mapquestapi.com/directions/v2/route?key=' + APIKEY + '&'
    locations_list.append(('from', locations[0]))
    for objects in locations[1:]:
        locations_list.append(('to', objects))
    return url + str(urllib.parse.urlencode(locations_list))


def formats_text(url: str):
    ''' Takes a url and formats it into json text '''
    opens = urllib.request.urlopen(url)
    return json.loads(opens.read().decode(encoding = 'utf-8'))

def elevations_url(locations: [str]):
    ''' Creates a url for elevations '''
    elevations_list = []
    url = 'http://open.mapquestapi.com/elevation/v1/profile?key=' + APIKEY + '&latLngCollection='
    for objects in range(len(locations)):
        elevations_list.append(url + str(locations[objects]))
    return elevations_list

def formats_elevations(url: list):
    ''' Takes a list of elevation urls and formats it into json text '''
    list_of_elevations = []
    for elevations in url:
        open_elevations = urllib.request.urlopen(elevations)
        formatted = json.loads(open_elevations.read().decode(encoding = 'utf-8'))
        list_of_elevations.append(formatted)
    return list_of_elevations


def elevation_nums(json_text: 'JSON-formatted text'):
    ''' Gets elevations for all locations '''
    latlong_list = []
    for objects in range(len(json_text['route']['locations'])):
        latlong_list.append(str(json_text['route']['locations'][objects]['latLng']['lat']) + ',' + str(json_text['route']['locations'][objects]['latLng']['lng']))
    return latlong_list
                                                   



