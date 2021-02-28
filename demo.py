import functions

my_location = "Museumstraße 1, 38100 Braunschweig Germany"
my_workplace = "Inhoffenstraße 7B 38124 Braunschweig Germany"

# use gecoding to convert address to coordinate
coordiate = functions.google_geocoding(my_location)
print (f"The coordinate of my location is {coordiate}\n\n")

# search schools within the 1 km radius, show the first five
schools = functions.google_nearbysearch(coordiate["latitude"], coordiate["longitude"], "school")
first_five_schools = "\n".join(schools[:5])
print (f"These are the five schools around 1 km:\n{first_five_schools}\n\n")

# show the distance and drive time from work
from_work = functions.driving_time_and_distance(my_location, my_workplace)
print (f"The distance between my location and my workplace: {from_work['distance_text']}. Driving time: {from_work['duration_text']}")

