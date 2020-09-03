# Samantha Young 59566370


class STEPS:
    ''' Prints the steps to get to each location '''
    def generate(self, json_text: 'JSON text for directions', json_text2: 'JSON text for elevation'):
        print('\n' + 'DIRECTIONS')
        for objects in json_text['route']['legs']:
            for moves in objects['maneuvers']:
                print(moves['narrative'])


class TOTALDISTANCE:
    ''' Prints the total distance of traveling in miles '''
    def generate(self, json_text: 'JSON text for directions', json_text2: 'JSON text for elevation'):
        print('\n' + 'TOTAL DISTANCE: {distance} {m}'.format(distance = round(json_text['route']['distance']), m = 'miles'))


class TOTALTIME:
    ''' Prints the total time of traveling in minutes '''
    def generate(self, json_text: 'JSON text for directions', json_text2: 'JSON text for elevation'):
        print('\n' + 'TOTAL TIME: {time} {mins}'.format(time = int(round(json_text['route']['time'] / 60)), mins = 'minutes')) 
    

class LATLONG:
    ''' Prints the latitude and longitude of the locations '''
    def generate(self, json_text: 'JSON text for directions', json_text2: 'JSON text for elevation'):
        print('\n' + 'LATLONGS')
        for objects in json_text['route']['locations']:
            if objects['latLng']['lat'] > 0:
                if objects['latLng']['lng'] < 0:
                    print(str(round(objects['latLng']['lat'], 2)) + 'N', str(round(abs(objects['latLng']['lng']), 2)) + 'W')
            elif objects['latLng']['lat'] < 0:
                if objects['latLng']['lng'] < 0:
                    print(str(round(objects['latLng']['lat'], 2)) + 'S', str(round(abs(objects['latLng']['lng']), 2)) + 'W')
            elif objects['latLng']['lat'] < 0:
                if objects['latLng']['lng'] > 0:
                    print(str(round(objects['latLng']['lat'], 2)) + 'S', str(round(abs(objects['latLng']['lng']), 2)) + 'E')
            elif objects['latLng']['lat'] > 0:
                if objects['latLng']['lng'] > 0:
                    print(str(round(objects['latLng']['lat'], 2)) + 'N', str(round(abs(objects['latLng']['lng']), 2)) + 'E')
                    

class ELEVATION:
    ''' Prints the elevations of the locations in meters '''
    def generate(self, json_text: 'JSON text for directions', json_text2: 'JSON text for elevation'):
        print('\n' + 'ELEVATIONS')
        for objects in json_text2:
            print(round(objects['elevationProfile'][0]['height'] * 3.28))
        
