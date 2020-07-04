import os
import json
import uuid

def create_dict():
    id = uuid.uuid1()

    vehicle_type = int(input(
        '¿Which type of vehicle do you want to create?\n(Type 1 for Scooter, 2 for Bicycle, 3 for Electric Bicycle)\n'))

    if vehicle_type == 1:
        battery = int(input('You have chosen to create a new Scooter, please give its battery value:\n'))
        status = input('Please give its status:\n')

        new_dict = {"id": str(id),
                    "type": 'scooter',
                    "battery": battery,
                    "status": status,
                    "current_speed": 0,
                    "needs_charge": False
                    }
        return new_dict

    elif vehicle_type == 2:
        status = input('You have chosen to create a new Bicycle, please give its status:\n')

        new_dict = {"id": str(id),
                    "type": 'bicycle',
                    "status": status,
                    "current_speed": 0,
                    "maintenance": False
                    }
        return new_dict

    else:
        battery = input('You have chosen to create a new Electric Bicycle, please give its battery:\n')
        status = input('Please give its status:\n')

        new_dict = {"id": str(id),
                    "type": 'electricbicycle',
                    "battery": battery,
                    "status": status,
                    "current_speed": 0,
                    "maintenance": False
                    }
        return new_dict

# function to add to JSON
def write_json(data, filename='db_test.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

with open('db_test.json') as json_file:
    data = json.load(json_file)
    temp = data['vehicles']

    # appending data to vehicles from input
    new_vehicle = True
    while new_vehicle:
        temp.append(create_dict())
        repeat = input('Do you want to create another vehicle? (y/n)')
        if repeat == 'n':
            new_vehicle = False
    #temp.append(create_dict())

write_json(data)

