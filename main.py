from Homework4.micro_mobility import Bicycle
from Homework4.micro_mobility import Scooter
from Homework4.micro_mobility import ElectricBicycle
import json

# Read a file of any type
with open('db_test.json', 'r') as f:
    raw_data = f.read()

# Convert the json file to a dictionary
vehicles_data = json.loads(raw_data)

# We filter the Scooters
scooters_from_db = filter(lambda x: x['type'] == 'scooter', vehicles_data['vehicles'])
scooters_list = []
for scooter_item in scooters_from_db:
    scooters_list.append(Scooter.from_db(**scooter_item))

# We filter the Bicycles
bicycles_from_db = filter(lambda x: x['type'] == 'bicycle', vehicles_data['vehicles'])
bicycles_list = []
for bicycle_item in bicycles_from_db:
    bicycles_list.append(Bicycle.from_db(**bicycle_item))

# We filter the Electric Bicycles
electric_bikes_from_db = filter(lambda x: x['type'] == 'electricbicycle', vehicles_data['vehicles'])
electric_bikes_list = []
for electric_bike_item in electric_bikes_from_db:
    electric_bikes_list.append(ElectricBicycle.from_db(**electric_bike_item))


# ============================== Scooters test ==================================
s1 = scooters_list[0]
print('Battery:', s1.battery)
print('Status:', s1.status)
s1.unlock()
s1.begin_ride()
print('Current speed:', s1.current_speed)
s1.current_speed = 20 # Update the scooter speed
print('Current speed:', s1.current_speed)
# s1.end_ride()
# s1.current_speed = 0
# s1.end_ride()
# print('Status:', s1.status)
# print('Battery:', s1.battery)

# ============================== Bicycles test ==================================
b1 = bicycles_list[0]
print('Needs maintenance:', b1.maintenance)
print('Status:', b1.status)
b1.unlock()
b1.begin_ride()
print('Current speed:', b1.current_speed)
b1.current_speed = 50 # Update the bicycle speed
print('Current speed:', b1.current_speed)
# b1.end_ride()
# b1.current_speed = 0
# b1.end_ride()
# print('Status:', b1.status)
b1.maintenance=True
print('Needs maintenance:', b1.maintenance)

# ========================== Electric Bicycles test =============================
eb1 = electric_bikes_list[0]
print('Status:', eb1.status)
eb1.unlock()
eb1.begin_ride()
print('Current speed:', eb1.current_speed)
eb1.current_speed = 30 # Update the electric bicycle speed
print('Current speed:', eb1.current_speed)

print('Battery:', eb1.battery)
eb1.battery = 80 # Update the electric bicycle battery
print('Battery:', eb1.battery)