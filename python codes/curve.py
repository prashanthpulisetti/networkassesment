import numpy as np
import matplotlib.pyplot as plt

print "Enter value of a & b"
a=int(raw_input())
b=int(raw_input())
if((4*a*a*a+27*b*b)==0):
	print "Invalid value for a and b"
	exit(0) 

def main():
    y, x = np.ogrid[-5:5:100j, -5:5:100j]
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * a - b, [0])
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
