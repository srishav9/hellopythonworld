#2 functions of json module:
#loads() and dumps()
#loads()---->json->python initials: {} then a dictionary, [] then a list
#dumps()---->python->json
#load from string || dump to string

import json
a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
print(a_string)
d = json.loads(a_string)
print("------")
print(type(d))
print(d.keys())
print(d['resultCount'])
# print(a_string['resultCount'])



import json
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)
d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}
print(d)
print('--------')
print(pretty(d))
