# -*- coding: utf-8 -*-
from collections import namedtuple
from math import sqrt, pi

Triangle = namedtuple("Triangle", "a b c")


Rectangle = namedtuple("Rectangle", "a b ")


Ellipse = namedtuple("Ellipse", "a b")


Circle = namedtuple("Circle", "r")

def circle_area(circle):
    return pi * circle.r * circle.r

def triangle_area(triangle):
    s = (triangle.a + triangle.b + triangle.c) / 2
    return sqrt(s * (s - triangle.a) * (s - triangle.b) * (s - triangle.c))


def rectangle_area(rectangle):
    return rectangle.a * rectangle.b


def ellipse_area(ellipse):
    return pi * ellipse.a * ellipse.b


def input_triangle():
    a = input("a = ")
    b = input("b = ")
    c = input("c = ")
    return Triangle(float(a), float(b), float(c))


def input_rectangle():
    a = input("a = ")
    b = input("b = ")
    return Rectangle(float(a), float(b))


def input_ellipse():
    a = input("a = ")
    b = input("b = ")
    return Ellipse(float(a), float(b))

def input_circle():
    r = input('r = ')
    return Circle(float(r))


inputs = {1: input_triangle, 2: input_rectangle, 3: input_ellipse, 4: input_circle}
areas = {1: triangle_area, 2: rectangle_area, 3: ellipse_area, 4: input_circle}


def calculate_area():
    figure_number = int(input("Input 1 to choose triangle, 2 - rectangle, 3 - ellipse, 4 - circle: "))
    figure = inputs[figure_number]()
    area = areas[figure_number](figure)
    print(str.format("{0} area is {1}", figure, area))


def main():
    while True:
        try:
            calculate_area()
        except Exception as e:
            print(e)
            print("Exit")
            break


main()