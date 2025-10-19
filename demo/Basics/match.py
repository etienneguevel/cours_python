list_coordinates = [
    ("Paris", "France", "Europe", "francais", (48.51, 2.21)),
    ("Tokyo", "Japon", (35.41, 139.41)),
    ("Buenos Aires", "Argentine", "Amerique", "espagnol", (-34.69, -58.22)),
    (120, "Londres")
]

test = []
for city in list_coordinates:
    match city:
        case str(city), *_, (float(lon), float(lat)):
            output = f"{city:15} | {lat:9.1f} | {lon:9}"
            print(output)
            test.append(output)
        
        case _:
            print("Wrong city format")

print(*test, sep="\n")