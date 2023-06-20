import requests
import xml.etree.ElementTree as ET

def test_request(name1,name2,name3):
    url = "https://akabab.github.io/superhero-api/api//all.json"
    response = requests.get(url)
    response1 = response.json()
    intellect = {}
    for heroes in response1:
        if name1 in heroes['name']:
            intellect.update({name1 : heroes['powerstats']['intelligence']})
        if name2 in heroes['name']:
            intellect.update({name2 : heroes['powerstats']['intelligence']})
        if name3 in heroes['name']:
            intellect.update({name3 : heroes['powerstats']['intelligence']})
    print(f'Самый умный - {max(intellect)},показатель интеллекта - {max(intellect.values())}')       


if __name__ == '__main__':
   test_request('Captain America','Thanos','Hulk')
#    ('Captain America', 'Thanos', 'Hulk')