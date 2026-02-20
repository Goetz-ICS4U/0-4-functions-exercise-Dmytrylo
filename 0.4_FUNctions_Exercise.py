"""
author: Dmytrylo
date: 2026/02/20
0.4 - Functions Review Exercises
"""
import math

# Exercise 1
def sum_cubes(n):
    """
    Caculate the sum of the first n cubes and prints the result
    
    Arg: n (int) - The number of cubes to sum
    
    Returns: none
    """
    total = 0
    for num in range(1, n + 1):
        total = total + num ** 3
    print(total)

# Test cases for sum_cubes
sum_cubes(0)    
sum_cubes(1)    
sum_cubes(5)    
sum_cubes(10)   
sum_cubes(50)   


# Exercise 2: 
def volume_sphere(r):
    """
    Calculates the volume of a sphere given its radius.

    Arg: r (float) - Radius of the sphere.

    Returns (float): Volume of the sphere.
    """
    vol = (3/4) * math.pi * (r ** 3)
    return vol


def area_sphere(r):
    """
    Calculates the surface area of a sphere given its radius.

    Arg: r (float) - Radius of the sphere.

    Returns:
    float: Surface area of the sphere.
    """
    surf = 4 * math.pi * (r ** 2)
    return surf


# Test Cases for volume_sphere and area_sphere
radii = [0, 1, 4, 10.4, 100.344]
for r in radii:
    v = volume_sphere(r)
    a = area_sphere(r)
    print("Radius:", r, "-> Volume:", round(v, 2), "Area:", round(a, 2))


# Exercise 3
def swap(a, b):
    """
    Swaps two input values and returns them in reversed order.
    """
    temp1 = b
    temp2 = a
    return temp1, temp2

# Test cases for swap
x, y = swap(3, 5)
print(x, y)

x, y = swap("Boo", "Hoo")
print(x, y)


# Exercise 4: Challenge
def approximate_pi(n):
    """
    Approximates the value of pi using the Leibniz series.
    """
    result = 0
    sign = 1

    for i in range(n):
        denom = 2 * i + 1
        result = result + sign * (4 / denom)
        sign = sign * -1

    return result


# Test cases for approximate_pi
print(approximate_pi(3))
print(approximate_pi(10))
print(approximate_pi(100))
print(approximate_pi(1000))