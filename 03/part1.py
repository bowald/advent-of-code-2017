from math import ceil, sqrt
#   C------+------C  |
#   |  Q2  |  Q3  |  |
#   |      |      |  |
#   +------+------+  d
#   |  Q1  |  Q0  |  |
#   |      |      |  |
#   C------+------C  |
#   -----  d  -----

# d = dimension
# q = Quadrant [Q0, Q1, Q2, Q3]
# C = Corner

def next_odd(f):
	return int(ceil(f)) | 1

def next_half(f):
	return round(f * 2) / 2

def get_dimension(i):
	return next_odd(sqrt(i))

def get_quadrant(d,i):
	return int((d - next_half(sqrt(i))) * 2)

def get_corner_square(q,d):
	return d*d - q * (d-1)

def corner_distance(d):
	return (d-1)

def square_distance_from_corner(i,q,d):
	return abs(i-get_corner_square(q,d))

square = 368078
d = get_dimension(square)
q = get_quadrant(d,square)
steps = abs(corner_distance(d) - square_distance_from_corner(square,q,d))
print steps