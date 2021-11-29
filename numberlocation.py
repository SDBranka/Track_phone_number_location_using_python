import phonenumbers
from mynumber import number
# importing to provide location
from phonenumbers import geocoder
# importing to provide carrier
from phonenumbers import carrier
# import to provide timezone of the number
from phonenumbers import timezone
# import to find coordinates of location
from opencage.geocoder import OpenCageGeocode

# import to assist in geolocation
import folium

API_KEY = "72d3af53f138463b82e0907e81f46866"

# prints location of the number
ph_numb = phonenumbers.parse(number)
country_of_number = geocoder.description_for_number(ph_numb, "en")

print(country_of_number)



# prints the service provider of the number
service_provider = phonenumbers.parse(number)

print(carrier.name_for_number(service_provider, "en"))


# print timezone of the number
time_zone = phonenumbers.parse(number)
print(timezone.time_zones_for_number(time_zone))


# print coordinates of the number
geocoder = OpenCageGeocode(API_KEY)

Query = str(country_of_number)

results = geocoder.geocode(Query)
# print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

my_map = folium.Map(location=[lat, lng], zoom_start=9)

folium.Marker([lat, lng], popup=country_of_number).add_to(my_map)

# save map to html file
my_map.save("mymap.html")