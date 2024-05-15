class UserRec:
    def __init__(self, cuisine, sort_pref, restaurant_list, user_location):
        self.cuisine = cuisine
        self.pref =  sort_pref
        self.restaurnt = restaurant_list
        self.location = user_location

    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, lon_lat):
        self._location = lon_lat

    @property
    def cuisine(self):
        return self._cuisine

    @cuisine.setter
    def cuisine(self, value):
        self._cuisine = value

    @property
    def filter(self):
        return self._pref
    
    @filter.setter
    def filter(self, value):
        self._cuisine = value



test = UserRec('Bagel','a-z','restuarant',[1,2])

print(test.location)