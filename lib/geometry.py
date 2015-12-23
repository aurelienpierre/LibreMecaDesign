# -*- coding: utf-8 -*-
'''

'''

import pylab
from sympy import Symbol


class geometry:
    ''' geometry(section, length, a, b=0)
                *section* : type of the section
                *a* : first dimension (height or external diameter)
                *b* : second dimension (none or width or internal diameter)'''

    def rectangle(self):
        # a : height
        # b : width
        self.A = self.b * self.a
        self.I_x = (self.b * self.a ** 3) / 12
        self.I_y = self.I_x

    def circle(self):
        self.A = pi * (self.a ** 2) / 4
        self.I_x = pi * (self.a ** 4) / 64
        self.I_y = self.I_x

    def hollow_circle(self):
        # a : external diameter
        # b : internal diameter
        self.A = pi * (self.a ** 2 - self.b ** 2) / 4
        self.I_x = pi * (self.a ** 4 - self.b ** 4) / 64
        self.I_y = self.I_x

    def semi_circle(self):
        # a : external diameter
        self.A = pi * (self.a ** 2) / 8
        self.I_x = 0.1098 * (self.a / 2) ** 4
        self.I_y = pi / 8 * (self.a / 2) ** 4

    def right_triangle(self):
        # a : height
        # b : width
        self.A = self.b * self.a / 2
        self.I_x = (self.b * self.a ** 3) / 36
        self.I_y = self.I_x

    def __init__(self, section, shape=""):

        self.a = a
        self.b = b

        types = {
            "rectangle": self.rectangle,
            "circle": self.circle,
            "hollow circle": self.hollow_circle,
            "solid semicircle": self.semi_circle,
            "right triangle": self.right_triangle
        }

        types[section]()
