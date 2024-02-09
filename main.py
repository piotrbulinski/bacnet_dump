import json
import sys

import BAC0

if __name__ == '__main__':
    try:
        ip_address = sys.argv[1]
    except IndexError:
        print("Usage: main.py <deviceIP>")
        exit(1)

    BAC0.log_level('silence')
    bacnet = BAC0.lite()

    device = BAC0.device(ip_address, 2, bacnet)

    print(json.dumps(device.binary_states))
    print(json.dumps(device.multi_states))

    properties = [
        'objectIdentifier', 'objectName', 'description', 'presentValue', 'units', 'resolution',
        'minPresValue', 'maxPresValue', 'statusFlags', 'reliability', 'outOfService', 'eventState',
        'inactiveText', 'activeText', 'numberOfStates', 'stateText',
    ]

    for pt in device.points:
        record = dict()

        for p in properties:
            try:
                record[p] = pt.bacnet_properties[p]
            except KeyError:
                pass

        try:
            if pt.bacnet_properties.priorityArray:
                record['priorityArray'] = True
        except AttributeError:
            pass

        print(json.dumps(record))
