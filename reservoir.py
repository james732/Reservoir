import requests
import bs4
import json

URL = r'http://fhy.wra.gov.tw/ReservoirPage_2011/StorageCapacity.aspx'

response = requests.get(URL)
if response.status_code == 200:
    result = bs4.BeautifulSoup(response.text, features="html.parser").find_all('td')
    all_storage = {}
    storage = {}
    for i in range(0, len(result), 11):
        if result[i].text == '附註':
            break
        storage['name'] = result[i].text
        storage['capacity'] = result[i + 1].text
        storage['time'] = result[i + 2].text
        storage['rain'] = result[i + 3].text
        storage['water_in'] = result[i + 4].text
        storage['water_out'] = result[i + 5].text
        storage['water_diff'] = result[i + 6].text
        storage['update_time'] = result[i + 7].text
        storage['level'] = result[i + 8].text
        storage['remain_capacity'] = result[i + 9].text
        storage['percentage'] = result[i + 10].text
        all_storage[storage['name']] = storage
        i += 11
    print(json.dumps(all_storage, indent=4))