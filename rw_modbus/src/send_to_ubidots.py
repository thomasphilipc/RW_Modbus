import ubidots
import json

from ubidots import ApiClient


def send_data(data,assetname):
    print(data,assetname)

    import config


    from json import load
    from urllib2 import urlopen

    my_ip = load(urlopen('http://jsonip.com'))['ip']

    lat = load(urlopen('http://api.ipstack.com/'+my_ip+'?access_key=f594d087ce71f888d826af695fecfa0a'))['latitude']
    print(lat)

    lon = load(urlopen('http://api.ipstack.com/'+my_ip+'?access_key=f594d087ce71f888d826af695fecfa0a'))['longitude']
    print(lon)

    print()

    secrets = config.get_secrets()
    CONNECTION_STRING = str(secrets["ubidots-string"])
    print(CONNECTION_STRING)
    api = ApiClient(token=CONNECTION_STRING)


    #data_json = json.loads(data)

    print(data['Phase 1 Line to Neutral Volts'])
    print(data['Phase 2 Line to Neutral Volts'])
    print(data['Phase 3 Line to Neutral Volts'])
    print(data['Phase 1 Current'])
    print(data['Phase 2 Current'])
    print(data['Phase 3 Current'])


    api.save_collection([{'variable': '5c861e8193f3c30b1909184e', 'value': data['Phase 1 Line to Neutral Volts'], 'context': {'lat': lat, 'lng': lon}},
                         {'variable': '5c861e8293f3c30b1909184f', 'value': data['Phase 2 Line to Neutral Volts'], 'context': {'lat': lat, 'lng': lon}},
                         {'variable': '5c861e8293f3c30b19091850', 'value': data['Phase 3 Line to Neutral Volts'], 'context': {'lat': lat, 'lng': lon}},
                         {'variable': '5c861e8293f3c30b19091851', 'value':data['Phase 1 Current'], 'context': {'lat': lat, 'lng': lon}},
                         {'variable': '5c861e8293f3c30b19091852', 'value':data['Phase 2 Current'], 'context': {'lat': lat, 'lng': lon}},
                         {'variable': '5c861e8293f3c30b19091853', 'value':data['Phase 3 Current'], 'context': {'lat': lat, 'lng': lon}},
                         ]
                        )

#send_data(data,assetname)
