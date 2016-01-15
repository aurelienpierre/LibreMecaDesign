# -*- coding: utf-8 -*-
"""
Reference
---------

*Machine Design, an integrated approach*. Robert L. Norton, \
Prentice Hall. Fifth Edition, 2014.

*Résistance des matériaux*. Bazergui, Bui-Quoc, Biron, McIntyre, Laberge, \
Presses internationales Polytechnique. Third Edition, 2002.

General consideration
---------------------

For beams, use the x axis along the longest dimension of the beam. \
Thus the cross-section of the beam will be in the (y, z) plan.
"""


from sympy import Symbol
import scipy

class geometry:
    """
    Store and compute basic geometrical properties of a material object
    
    :param position: coordinates of the origin of the object. \
    For example, the centroid of an extreme surface
    :type position: 3 elements array or tuple
    
    :param dimensions: lengths over the 3 space dimensions or \
    formal expressions of these dimensions.
    :type dimensions: 3 elements array or tuple
    
    :param a,b: geometric parameters to compute section properties \
    for standard/usual profiles as defined in Norton's *Machine design* book.
    
    """

    def rectangle(self):
        """
        :param a: height
        :param b: width
        """
        self.area = self.b * self.a
        # self.Q = 
        # self.J = 
        # self.k = 
        self.I_y = (self.b * self.a ** 3) / 12
        self.I_z = self.I_y

    def circle(self):
        """
        :param a: radius
        :param b: none
        """
        self.area = pi * (self.a ** 2) / 4
        # self.Q = 
        # self.J = 
        # self.k = 
        self.I_y = pi * (self.a ** 4) / 64
        self.I_z = self.I_y

    def hollow_circle(self):
        """
        :param a: external diameter
        :param b: internal diameter
        """
        self.area = pi * (self.a ** 2 - self.b ** 2) / 4
        # self.Q = 
        # self.J = 
        # self.k = 
        self.I_y = pi * (self.a ** 4 - self.b ** 4) / 64
        self.I_z = self.I_y

    def semi_circle(self):
        """
        :param a: external diameter
        """
        self.area = pi * (self.a ** 2) / 8
        # self.Q = 
        # self.J = 
        # self.k = 
        self.I_y = 0.1098 * (self.a / 2) ** 4
        self.I_z = pi / 8 * (self.a / 2) ** 4

    def right_triangle(self):
        """ 
        :param a: height
        :param b: width
        """
        self.area = self.b * self.a / 2
        # self.Q = 
        # self.J = 
        # self.k = 
        self.I_y = (self.b * self.a ** 3) / 36
        self.I_z = self.I_y

    def __init__(self, **kwargs):
        # Coordinates of the origin of the material object
        x = Symbol('x')
        y = Symbol('y')
        z = Symbol('z')

        self.position = kwargs.get('position', [x, y, z])

        # Shape/Length values or formal equations
        x_length = Symbol('x_length')
        y_length = Symbol('y_length')
        z_length = Symbol('z_length')

        self.dimensions = kwargs.get('dimensions', [x_length, y_length, z_length])

        # Section/geometry parameters
        a = Symbol('a')
        b = Symbol('b')

        self.a = kwargs.get('a', a)
        self.b = kwargs.get('b', b)

        # Surfaces moments
        section = kwargs.get('section', '')

        types = {
            "rectangle": self.rectangle,
            "circle": self.circle,
            "hollow circle": self.hollow_circle,
            "solid semicircle": self.semi_circle,
            "right triangle": self.right_triangle
        }

        types[section]()

if __name__ == '__main__':
    object = geometry(section="rectangle", a=2, b=5)

    attrs = vars(object)

    print (', '.join("%s: %s" % item for item in attrs.items()))
