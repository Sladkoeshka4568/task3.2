import json


class JsonDataGetter:
    with open('CommonFunctions/config.json') as config_data:
        data = json.load(config_data)
        print(data)
    browser = data['browser']
    url = data['url']



class JsonDataGetterTestData:
    with open('CommonFunctions/test_data.json') as config_data:
        file = json.load(config_data)
    result = []
    for data in file:
        result.append(data)
