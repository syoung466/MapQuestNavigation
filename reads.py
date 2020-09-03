# Samantha Young 59566370
import interacts
from implements import *

def input_checker():
    ''' Checks that the value of locations to be inputed is valid '''
    while True:
        try:
            input_num = int(input())
            if input_num >= 2:
                return input_num
            else:
                print('You must specify at least two locations.')
        except:
            print('Please enter an integer that is at least 2.')
        

def user_inputs():
    ''' Creates a list of locations that the user wishes to input '''
    input_list = []
    input_total = 0
    input_num = input_checker()
    while input_total < input_num:
        locations = input()
        input_list.append(locations)
        input_total += 1
    return input_list


def output_checker():
    ''' Checks that the value of outputs to be recieved is valid '''
    while True:
        try:
            output_num = int(input())
            if output_num >= 1 and output_num <= 5:
                return output_num
            else:
                print('Must be an integer that is at least 1 and up to 5.')
        except:
            print('You must specify output generators.')


def output_results():
    ''' Creates a list of outputs depending how many the user wants to receive '''
    output_list = []
    output_total = 0
    output_num = output_checker()
    while output_total < output_num:
        outputs = input()
        if outputs.upper() == 'STEPS':
            output_list.append(STEPS())
        elif outputs.upper() == 'TOTALDISTANCE':
            output_list.append(TOTALDISTANCE())
        elif outputs.upper() == 'TOTALTIME':
            output_list.append(TOTALTIME())
        elif outputs.upper() == 'LATLONG':
            output_list.append(LATLONG())
        elif outputs.upper() == 'ELEVATION':
            output_list.append(ELEVATION())
        output_total += 1
    return output_list


def run_mapquest():
    ''' Runs the mapquest program '''
    first = user_inputs()
    output = output_results()
    for objects in output:
        try:
            places = interacts.formats_text(interacts.directions_url(first))
            info = interacts.elevations_url(interacts.elevation_nums(places))
            elevations = interacts.formats_elevations(info)
            objects.generate(places, elevations)
        except KeyError:
            print('\n' + 'NO ROUTE FOUND')
            break
        except:
            print('\n' + 'MAPQUEST ERROR')
            break
    print('\n' + 'Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')

if __name__ == '__main__':
    run_mapquest()
       
