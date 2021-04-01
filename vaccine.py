import requests
import time
import beepy
import webbrowser
from halo import Halo

state = 'CA'
cities = ['NEWARK', 'FREMONT', 'HAYWARD', 'PLEASANTON', 'DUBLIN', 'MENLO PARK', 'MOUNTAIN VIEW', 'SUNNYVALE', 'SAN RAMON',  'SAN LEANDRO', 'SANTA CLARA', 'PALO ALTO', 'SAN CARLOS', 'DANVILLE', 'SAN JOSE', 'LIVERMORE', 'SAN MATEO', 'ALAMO', 'CUPERTINO', 'CAMPBELL', 'MORAGA', 'REDWOOD CITY', 'ALAMEDA', 'SARATOGA', 'LAFAYETTE', 'ORINDA', 'LOS GATOS', 'OAKLAND', 'HALF MOON BAY', 'WALNUT CREEK', 'TRACY', 'SAN BRUNO', 'EMERYVILLE', 'BRENTWOOD', 'PLEASANT HILL', 'BERKELEY', 'ALBANY', 'DALY CITY', 'EL CERRITO', 'MARTINEZ', 'CONCORD', 'PITTSBURG', 'ANTIOCH']

spinner = Halo(text='Finding CVS appointments in {}'.format('CA'), spinner='dots')

def findAVaccine():
    hours_to_run = 3
    max_time = time.time() + hours_to_run*60*60
    while time.time() < max_time:
        spinner.start()

        response = requests.get("https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.{}.json?vaccineinfo".format(state.lower()), headers={"Referer":"https://www.cvs.com/immunizations/covid-19-vaccine"})
        payload = response.json()

        mappings = {}
        for item in payload["responsePayloadData"]["data"][state]:
            mappings[item.get('city')] = item.get('status')

        for key in mappings.keys():
            if (key in cities) and (mappings[key] != 'Fully Booked'):
                print("\n")
                print(city, mappings[city])
                webbrowser.open("https://www.cvs.com/vaccine/intake/store/cvd-store-select/first-dose-select")
                for _ in range(10):
                    beepy.beep(sound = 'coin')
                break
            else:
                pass
        time.sleep(1)

findAVaccine()
