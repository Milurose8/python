import graphic.rectangle
from graphic.Dgraphics import sphere

print("Area of rectangle",graphic.rectangle.area(3.,4))
print("perimeter of rectangle", graphic.rectangle.perimeter(3,4))


from graphic.Dgraphics.circle import area
print("area of circle",area(2))

from graphic.Dgraphics.circle import perimeter
print("perimeter of circle",perimeter(2))

from graphic.Dgraphics.cuboid import area
print("area of cuboid", area(1,2,3))

from graphic.Dgraphics.cuboid import perimeter
print("perimeter of cuboid",perimeter(1,2,3))

import graphic.Dgraphics.sphere
print("area of sphere",graphic.Dgraphics.sphere.area(2))
print("perimeter of sphere",graphic.Dgraphics.sphere.perimeter(2))

