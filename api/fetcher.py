import requests
from api.config import settings

ROOT_URL = settings.ROOT_URL

def states_accessor():
    #Go through the doc api examples!
    url = f"{ROOT_URL}/states/all"
    r = requests.get(url)
    if not r.ok:
        raise RuntimeError(r.json())
    print(r.json())

def tracks_accessor():
    url = f"{ROOT_URL}/tracks/all?icao24=3c4b26&time=0"
    r = requests.get(url)
    if not r.ok:
        raise RuntimeError(r.json())
    print(r.json())

def flights_accessor():
    url = f"{ROOT_URL}/flights/all?begin=1517227200&end=1517230800"
    r = requests.get(url)
    if not r.ok:
        raise RuntimeError(r.json())
    print(r.json())