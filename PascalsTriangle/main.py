#!/usr/bin/python3

"""
main file 
"""

#PascalTriangle = __import__(PascalTriangle').PascalTriangle

def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))
        
        if __name__ == "__main__":
            print_triangle(PascalTriangle(5))
            