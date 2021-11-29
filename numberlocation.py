import phonenumbers
from mynumber import number
from phonenumbers import geocoder
from phonenumbers import carrier


API_KEY = "72d3af53f138463b82e0907e81f46866"


ph_numb = phonenumbers.parse(number)
your_location = geocoder.description_for_number(ph_numb, "en")

# prints location of the number
print(your_location)

# prints the service provider of the number
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(API_KEY)

Query = str(your_location)

results = geocoder.geocode(Query)
print(results)