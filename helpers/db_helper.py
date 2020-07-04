import json
import os


def update_db_item(item, instance):
    if instance.__class__.__name__ == 'Scooter':
        item['needs_charge'] = instance.needs_charge
        item['current_speed'] = instance.current_speed
        item['status'] = instance.status
        item['battery'] = instance.battery

    #return item

    elif instance.__class__.__name__ == 'Bicycle':
        item['status'] = instance.status
        item['current_speed'] = instance.current_speed
        item['maintenance'] = instance.maintenance

    else:
        item['status'] = instance.status
        item['current_speed'] = instance.current_speed
        item['maintenance'] = instance.maintenance
        item['battery'] = instance.battery

    return item

def update_db(instance):
    with open(os.path.join(os.path.dirname(__file__), '../db_test.json'), 'r+') as f:
        raw_data = f.read()
        vehicles_data = json.loads(raw_data)
        updated_data = list(map(
            lambda x: update_db_item(x, instance) if x['id'] == instance.id
            else x,
            vehicles_data['vehicles']
        ))
        vehicles_data['vehicles'] = updated_data

        f.seek(0)
        f.truncate()
        f.write(json.dumps(vehicles_data))
