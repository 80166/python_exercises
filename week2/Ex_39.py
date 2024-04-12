states = {
    "Uttar Pradesh": "UP",
    "Maharashtra": "MH",
    "Karnataka": "KA",
    "Tamil Nadu": "TN",
    "Gujarat": "GJ",
}

cities = {
    "UP": "Lucknow",
    "MH": "Mumbai",
    "KA": "Bengaluru",
    "TN": "Chennai",
    "GJ": "Ahmedabad",
}

cities["Delhi"] = "New Delhi"
cities["UP"] = "Agra"

print("- " * 10)
print("Delhi State has:", cities["Delhi"])
print("UP State has:", cities["UP"])

print("- " * 10)
print("Uttar Pradesh's abbreviation is:", states["Uttar Pradesh"])
print("Maharashtra's abbreviation is:", states["Maharashtra"])

print("- " * 10)
print("Uttar Pradesh has:", cities[states["Uttar Pradesh"]])
print("Maharashtra has:", cities[states["Maharashtra"]])

print("- " * 10)
for state, abbrev in states.items():
    print("%s is abbreviated %s" % (state, abbrev))

print("- " * 10)
for abbrev, city in cities.items():
    print("%s has the city %s" % (abbrev, city))

print("- " * 10)
for state, abbrev in states.items():
    print(
        "%s state is abbreviated %s and has city %s"
        % (state, abbrev, cities.get(abbrev, "Unknown"))
    )

print("- " * 10)
state = states.get("Rajasthan", None)
if not state:
    print("Sorry, no Rajasthan.")

city = cities.get("RJ", "Does Not Exist")
print("The city for the state 'RJ' is:", city)
