
import  math

#We assume the polygon is regular
#According the formula in https://en.wikipedia.org/wiki/Regular_polygon
# n = number of edges, s = lenght of each edge.


def cot(x):
    return (math.cos(x)/math.sin(x))

def area_regular_polygon(n,s):
    return n*s*s* (cot(math.pi/n))*0.25

#Basic test
print area_regular_polygon(4,2) #==4 (rectangle of 2*2)

