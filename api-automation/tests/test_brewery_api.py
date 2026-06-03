import pytest

 # https://www.openbrewerydb.org/documentation from the list: https://github.com/public-apis/public-apis

class TestBreweryAPI:


        #TC_API_001 – Get All Breweries Status Code
        #Verify breweries endpoint is accessible.
        #Expected Result: Status code 200.

    def test_get_breweries_status_code(self, brewery_api):
        response = brewery_api.get_all_breweries()

        assert response.status_code == 200

        #TC_API_002 – Response Is Not Empty
        #Verify breweries list contains data.
        #Expected Result: Response length is greater than 0. 

    def test_response_is_not_empty(self, brewery_api):
        response = brewery_api.get_all_breweries()

        assert len(response.json()) > 0

        #TC_API_003 – Response Is List
        #Verify API returns a list of breweries.
        #Expected Result: Response type is list.
    def test_response_is_list(self, brewery_api):
        response = brewery_api.get_all_breweries()

        assert isinstance(response.json(), list)

        #TC_API_004 – Required Fields Exist
        #Verify brewery contains required fields.
        #Expected Result: id, name, brewery_type, city, and state fields exist.
    def test_required_fields_exist(self, brewery_api):
        response = brewery_api.get_all_breweries()

        brewery = response.json()[0]

        required_fields = [
            "id",
            "name",
            "brewery_type",
            "city",
            "state"
        ]

        for field in required_fields:
            assert field in brewery

     #TC_API_005 – Search Brewery By City
     #Verify brewery search works for supported cities.
     #Expected Result: Status code 200 and response data returned.
      #TC_API_006 – Get Brewery By Valid ID
      #Expected code: 200
      #TC_API_007 – Get Brewery By Invalid ID
      #Expected code: 404       
    #pytest Parameterization
    @pytest.mark.parametrize(
        "city",
        [
            "san_diego",
            "new_york",
            "austin"
        ]
    )
    def test_search_by_city(self, brewery_api, city):
        response = brewery_api.get_breweries_by_city(city)

        assert response.status_code == 200
        assert isinstance(response.json(), list)

        #TC_API_008 – Response Time Validation
        #Verify API responds within acceptable time.
        #Expected Result: Response time is less than 2 seconds.

    def test_response_time_under_two_seconds(self, brewery_api):
        response = brewery_api.get_all_breweries()

        assert response.elapsed.total_seconds() < 2