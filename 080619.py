# monte carlo pi

# generating only random data, and using knowledge about circles
# approximate pi
# x2 + y2 = r2
# area of circle = pi*r2
# unit circle area of square = 1, r = .5
# generate random x,y points
# pi = area / .5^2
# n is the size of the random data set
def monte_pi(n):
    unit_square = np.random.uniform(0,1,(n,2))             # n x 2 matrix of x,y pairs
    circle_count = 0
    for x in unit_square:
        if (x[0]**2 + x[1]**2 < 1):
            circle_count += 1 
    circle_area =  np.float(circle_count)/np.float(n)      # points in circle / total points ~= area of circle 
    return circle_area / (0.5**2)                          # pi ~= area of circle / r^2

