list_coordinates = [
    ("Paris", (48.51, 2.21)),
    ("Tokyo", (35.41, 139.41)),
    ("Buenos Aires", (-34.69, -58.22))
]

for i in list_coordinates:
    print(i)
    print(i[0])
    print(i[1])
    ville, (longitude, lattitude) = i
    print(f"Ville: {ville} ({longitude}, {lattitude})")

print()
