#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    This imports materials properties as a class and make them query-able by mapping their names and aliases to 
    human-readable names.
'''

import os
import sys
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
PARENT_PATH = os.path.dirname(CURRENT_PATH)
sys.path.append(PARENT_PATH)


class materials:

    def trimdata(self, file):
        """ 
        Extract the symbols of the properties from the 3rd line of the data-sheet

        """

        return

    def processdata(self, dir, file):
        return

    def __init__(self, material, standard="", **kwds):

        return
        # TODO:
        # Lib from URL
        # Lib from custom path


if __name__ == "__main__":
    object = materials('carbon AND steel')
