import math

def distanceBetweenTwoPoints():
    points = ['xa', 'xb', 'ya', 'yb']
    coordinates = []

    for point in points:
            coordinates.append(int(input(f'type {point.upper()} coordinate: ')))

    xa = coordinates[0]
    xb = coordinates[1]
    ya = coordinates[2]
    yb = coordinates[3]

    result = math.sqrt(((xb - xa)^2) + ((yb - ya)^2))
    print(result)

distanceBetweenTwoPoints()
