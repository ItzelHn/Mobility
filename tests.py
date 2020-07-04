from micro_mobility import Bicycle
from micro_mobility import Scooter
from micro_mobility import ElectricBicycle


print('================== BIKE TESTS =======================')
b1 = Bicycle()
# ============= First iteration =============
assert b1.status == 'locked'
assert not b1.maintenance
assert b1.current_speed == 0
b1.unlock()
assert b1.status == 'unlocked'
b1.begin_ride()
assert b1.status == 'in-ride'
b1.current_speed = 30
assert b1.current_speed == 30
b1.current_speed = 0
b1.end_ride()
assert b1.status == 'locked'  # only when the status changes from 'ín-ride' to 'locked' the num_rides should increment
# ============= First iteration end =============

# ============= Second iteration =============
assert not b1.maintenance
b1.unlock()
assert b1.status == 'unlocked'
b1.begin_ride()
assert b1.status == 'in-ride'
b1.end_ride()
assert b1.status == 'locked'
# ============= Second iteration end =============

# ============= Third iteration =============
assert not b1.maintenance
b1.unlock()
assert b1.status == 'unlocked'
b1.begin_ride()
assert b1.status == 'in-ride'
b1.end_ride()
assert b1.status == 'locked'
# ============= Third iteration end =============

# ============= Fourth iteration =============
assert b1.maintenance
b1.unlock()
assert b1.status == 'locked'
b1.repair()
assert b1.maintenance
b1.pick_up()
assert b1.status == 'in-transit'
b1.stashed()
assert b1.status == 'in-warehouse'
b1.repair()
assert not b1.maintenance
b1.deploy()
assert b1.status == 'in-warehouse'
b1.back_to_service()
assert b1.status == 'deploying'
b1.deploy()
assert b1.status == 'locked'
b1.unlock()
assert b1.status == 'unlocked'
b1.begin_ride()
assert b1.status == 'in-ride'
b1.end_ride()
assert b1.status == 'locked'
# ============= Fourth iteration end =============
print('All bikes tests passed')
print('================== BIKE TESTS END =======================')

print('================== SCOOTER TESTS =======================')
s1 = Scooter()
# ============= First iteration =============
assert s1.status == 'locked'
assert s1.current_speed == 0
s1.unlock()
assert s1.status == 'unlocked'
s1.begin_ride()
assert s1.status == 'in-ride'
s1.current_speed = 20
assert s1.current_speed == 20
s1.current_speed = 0
s1.end_ride()
assert s1.status == 'locked'  # only when the status changes from 'ín-ride' to 'locked' the battery should decrement
assert s1.battery == 82
# assert s1.current_speed == 'You are riding at 0 km/h'  # This should be changed to 0 once the vehicle is locked
# ============= First iteration end =============

# ============= Second iteration =============
s1.unlock()
assert s1.status == 'unlocked'
s1.begin_ride()
assert s1.status == 'in-ride'
s1.end_ride()
assert s1.status == 'locked'
assert s1.battery == 65
# ============= Second iteration end =============

# ============= Third iteration =============
s1.unlock()
assert s1.status == 'unlocked'
s1.begin_ride()
assert s1.status == 'in-ride'
s1.end_ride()
assert s1.status == 'locked'
assert s1.battery == 48
# ============= Third iteration end =============

# ============= Fourth iteration =============
s1.unlock()
assert s1.status == 'unlocked'
s1.begin_ride()
assert s1.status == 'in-ride'
s1.end_ride()
assert s1.status == 'locked'
assert s1.battery == 31
# ============= Fourth iteration end ============

# ============= Fifth iteration =============
s1.unlock()
assert s1.status == 'unlocked'
s1.begin_ride()
assert s1.status == 'in-ride'
s1.end_ride()
assert s1.status == 'locked'
assert s1.battery == 14
# ============= Fifth iteration end =============

# ============= Sixth iteration =============
s1.unlock()
assert s1.status == 'locked'
s1.charge()
assert s1.needs_charge
s1.pick_up()
assert s1.status == 'in-transit'
s1.stashed()
assert s1.status == 'in-warehouse'
s1.charge()
assert not s1.needs_charge
s1.back_to_service()
assert s1.status == 'deploying'
s1.deploy()
assert s1.status == 'locked'
s1.unlock()
assert s1.status == 'unlocked'
s1.begin_ride()
assert s1.status == 'in-ride'
s1.current_speed = 50
assert s1.current_speed == 35
# ============= Sixth iteration end =============
print('All scooter tests passed')
print('================== SCOOTER TESTS END =======================')

print('================== ElectricBicycle TESTS =======================')
e1 = ElectricBicycle()
# ============= First iteration =============
assert e1.status == 'locked'
assert e1.current_speed == 0
e1.unlock()
assert e1.status == 'unlocked'
e1.begin_ride()
assert e1.status == 'in-ride'
e1.current_speed = 20
assert e1.current_speed == 20
e1.current_speed = 0
e1.end_ride()
assert e1.status == 'locked'  # only when the status changes from 'ín-ride' to 'locked' the battery should decrement
assert e1.battery == 82
# assert s1.current_speed == 'You are riding at 0 km/h'  # This should be changed to 0 once the vehicle is locked
# ============= First iteration end =============

# ============= Second iteration =============
e1.unlock()
assert e1.status == 'unlocked'
e1.begin_ride()
assert e1.status == 'in-ride'
e1.end_ride()
assert e1.status == 'locked'
assert e1.battery == 65
# ============= Second iteration end =============

# ============= Third iteration =============
e1.unlock()
assert e1.status == 'unlocked'
e1.begin_ride()
assert e1.status == 'in-ride'
e1.end_ride()
assert e1.status == 'locked'
assert e1.battery == 48
# ============= Third iteration end =============

# ============= Fourth iteration =============
e1.unlock()
assert e1.status == 'locked'
assert e1.maintenance
assert e1.battery == 48
assert not e1.needs_charge
e1.pick_up()
assert e1.status == 'in-transit'
e1.stashed()
assert e1.status == 'in-warehouse'
e1.repair()
assert not e1.maintenance
assert e1.continues_rides == 0
e1.back_to_service()
assert e1.status == 'deploying'
e1.deploy()
assert e1.status == 'locked'
e1.unlock()
e1.begin_ride()
assert e1.status == 'in-ride'
e1.end_ride()
assert e1.status == 'locked'
assert e1.battery == 31
# ============= Fourth iteration end ============

# ============= Fifth iteration =============
e1.unlock()
assert e1.status == 'unlocked'
e1.begin_ride()
assert e1.status == 'in-ride'
e1.end_ride()
assert e1.status == 'locked'
assert e1.battery == 14
# ============= Fifth iteration end =============

# ============= Sixth iteration =============
e1.unlock()
assert e1.status == 'locked'
assert e1.needs_charge
e1.pick_up()
assert e1.status == 'in-transit'
e1.stashed()
assert e1.status == 'in-warehouse'
e1.charge()
assert not e1.maintenance
assert not e1.needs_charge
assert e1.continues_rides == 2
e1.back_to_service()
assert e1.status == 'deploying'
e1.deploy()
assert e1.status == 'locked'
e1.unlock()
e1.begin_ride()
assert e1.status == 'in-ride'
e1.end_ride()
assert e1.status == 'locked'
assert e1.battery == 83
# ============= Sixth iteration end =============

# ============= Seventh iteration =============
e1.unlock()
assert e1.status == 'locked'
assert e1.maintenance
assert not e1.needs_charge
e1.pick_up()
assert e1.status == 'in-transit'
e1.stashed()
assert e1.status == 'in-warehouse'
e1.repair()
assert not e1.maintenance
assert e1.continues_rides == 0
e1.back_to_service()
assert e1.status == 'deploying'
e1.deploy()
assert e1.status == 'locked'
e1.unlock()
e1.begin_ride()
assert e1.status == 'in-ride'
e1.end_ride()
assert e1.status == 'locked'
assert e1.battery == 66
# ============= Seventh iteration end =============

# ============= Eight iteration =============
e1.unlock()
assert e1.status == 'unlocked'
e1.begin_ride()
assert e1.status == 'in-ride'
e1.end_ride()
assert e1.status == 'locked'
assert e1.battery == 49
# ============= Eight iteration end =============

# ============= Ninth iteration =============
e1.unlock()
assert e1.status == 'unlocked'
e1.begin_ride()
assert e1.status == 'in-ride'
e1.end_ride()
assert e1.status == 'locked'
assert e1.battery == 32
# ============= Ninth iteration end =============

# ============= Tenth iteration =============
e1.unlock()
assert e1.status == 'locked'
assert e1.maintenance
assert not e1.needs_charge
e1.pick_up()
assert e1.status == 'in-transit'
e1.stashed()
assert e1.status == 'in-warehouse'
e1.repair()
assert not e1.maintenance
assert e1.continues_rides == 0
e1.back_to_service()
assert e1.status == 'deploying'
e1.deploy()
assert e1.status == 'locked'
e1.unlock()
e1.begin_ride()
assert e1.status == 'in-ride'
e1.end_ride()
assert e1.status == 'locked'
assert e1.battery == 15
# ============= Tenth iteration end =============

# ============= Eleventh iteration =============
e1.unlock()
assert e1.status == 'unlocked'
e1.begin_ride()
assert e1.status == 'in-ride'
e1.end_ride()
assert e1.status == 'locked'
assert e1.battery == 0
# ============= Eleventh iteration end =============

# ============= twelfth iteration =============
e1.unlock()
assert e1.status == 'locked'
assert e1.needs_charge
assert e1.empty_battery_count == 2
assert e1.maintenance
e1.pick_up()
assert e1.status == 'in-transit'
e1.stashed()
assert e1.status == 'in-warehouse'
e1.repair()
e1.charge()
assert not e1.maintenance
assert not e1.needs_charge
assert e1.continues_rides == 0
assert e1.empty_battery_count == 0
e1.back_to_service()
assert e1.status == 'deploying'
e1.deploy()
assert e1.status == 'locked'
e1.unlock()
e1.begin_ride()
assert e1.status == 'in-ride'
e1.end_ride()
assert e1.status == 'locked'
assert e1.battery == 83
# ============= twelfth iteration end =============

print('All ElectricBicycle tests passed')
print('================== ElectricBicycle TESTS END =======================')
