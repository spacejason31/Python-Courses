# Geocoding with Web
import geocode
import urllib
import requests
from time import sleep
from functools import lru_cache

base_url = "https://nominatim.openstreetmap.org/search?"
params = {"format": "json", "q": "Eiffel Tower"}
result = requests.get(base_url, params=params)
result.status_code
result.json()

params = {"format": "json", "q": "Cair Paravel, Narnia", "limit": 1}


@lru_cache(maxsize=2000)
def nominatim_geocode(address, format="json", limit=1, **kwargs):
    """thin wrapper around nominatim API.
    Documentation: https://wiki.openstreetmap.org/wiki
    /Nominatim#Parameters
    """
    params = {"format": format, "q": address, "limit": limit, **kwargs}
    response = requests.get(base_url, params)
    response.raise_for_status()
    sleep(1)
    return response.json()


nominatim_geocode("Eiffel Tower")
nominatim_geocode(
    address=None, street="221B Baker Street", city="London", country="Great Britain"
)


def title(f):
    def _title(*args, **kwargs):
        return f"<h1>{f(args)}</h1>"

    return _title


def mytext(x):
    return str(x)


MyTitle = title(mytext)
MyTitle("hello")


@title
def MyTitle(x):
    return str(x)


MyTitle("hello")


path_in = r"Data_Science_Apps\cities.csv"
path_out = r"Data_Science_Appr\geocoded.csv"
data = read_csv(path_in)
result, errors = geocode_bulk(data, column="address", verbose=True)
