import phonenumbers
import folium 
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode


number = input ("Enter a Phone Number:")
key = "f9db1eb5f08a4a3bbceb5bd02d901ad6"

get_number =phonenumbers.parse(number)
location = geocoder.description_for_number(get_number ,"en")
print(location)


service_provider =phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

geocoder = OpenCageGeocode(key)

query = str(location)
results =geocoder.geocode(query)

latitude = results[0]['geometry']['lat']
longitude = results[0]['geometry']['lng']
print(latitude,longitude)

map_my = folium.Map(location=[latitude,longitude],zoom_start=8)
folium.Marker([latitude,longitude],popup=location).add_to((map_my))

map_my.save("map.html")