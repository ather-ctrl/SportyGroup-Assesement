import requests


# using these apis: https://www.openbrewerydb.org/documentation

class BreweryAPI:
    BASE_URL = "https://api.openbrewerydb.org/v1/breweries"

    def get_all_breweries(self):
        return requests.get(self.BASE_URL)

    def get_breweries_by_city(self, city):
        return requests.get(
            self.BASE_URL,
            params={"by_city": city}
        )

    def get_brewery_by_id(self, brewery_id):
        return requests.get(
            f"{self.BASE_URL}/{brewery_id}"
        )