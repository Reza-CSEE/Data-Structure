import math

points = [
    (12, 55),
    (880, 123),
    (64, 64),
    (190, 1024),
    (77, 33),
    (42, 11),
    (0, 90)
]
#your code goes here
distance = list(range(len(points)))
z=0
for (x,y) in points:
    distance[z] = math.sqrt((x**2+y**2)) 
    z+=1

print(min(distance))
