print("Farzaan Bin Khawar\n2023F-BIT-030")
favorite_places = {
    "abc": ["Bear Mountain", "Death Valley", "Tierra Del Fuego"],
    "xyz": ["Grand Canyon", "Paris", "Kyoto"],
    "123": ["New York City", "Sydney", "Machu Picchu"]
}

for person, places in favorite_places.items():
    print(f"{person} likes the following places:")
    for place in places:
        print(f"- {place}")
    print()  
