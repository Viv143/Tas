'''Write a Python program that uses tuples to represent points in a 2D coordinate system. 
The program should calculate the distance between two points.'''

class Coordinate_system:
    def __init__(self,point1,point2):
        self.point1=point1
        self.point2=point2

    def calculate_distance(self):
        x1,y1=self.point1
        x2,y2=self.point2

        distance=((x2-x1)**2 + (y2-y1)**2)**0.5
        return distance
    

point1=(10,6)
point2=(12,7)

points=Coordinate_system(point1,point2)
points.calculate_distance()
print(f"Distance between {points.point1} and {points.point2} is {points.calculate_distance():.2f}")