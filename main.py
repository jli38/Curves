from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

/*
bezier
80 235 80 20 475 486 425 425
bezier
80 235 95 140 475 486 425 425
display
save
test.png
*/

print_matrix(make_bezier())
print_matrix(make_hermite())

parse_file( 'script', edges, transform, screen, color )
