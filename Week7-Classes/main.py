import shapes

some_shape = shapes.Triangle()
some_shape.set_side_length(3,0)
some_shape.set_side_length(4,1)
some_shape.set_side_length(5,2)

print(some_shape.get_area())

some_shape = shapes.Triangle()
print(shapes.Polygon.number_of_polygons)