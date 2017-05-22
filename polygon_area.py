# This program computes # the area of polygons 
import math
def main():
    num_sides = (3, 4, 5, 6, 7, 8, 9)
    sidelength = side_length(get_side_length)
    polygonarea = polygon_area
    get_side_length(report)
    report()

def report(side_length ):
    print('Side length\tNumber of Sides\tArea')
    print('----------------------------------')
    for sides in range (3,10):
          print(sidelength, num_sides, polygon_area)
    
def polygon_area( num_sides, side_length ):
    area = (num_sides * side_length * side_length) \
         / (4 * math.tan(math.pi / num_sides))
    return area (polygonarea)

def get_side_length():
    side = int(input('Input the length of a side: '))
    return side(side_length)

# start the program
main()
