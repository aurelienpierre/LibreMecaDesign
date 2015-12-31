#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module imports all CSV data sheet from the ``lib`` directory into a sqlite database. 
This script has to be executed each time a data sheet is added or edited.
You just need to call it without argument.

.. warning:: Each new call of the module overwrite the previous database. Make a backup before.

Included data
-------------

* Carbon steel

Adding data
-----------

Only standard data from reputable and trusted sources are and should be used in the librairies. 

For materials properties, data should include in this order :

#. normalized name    
#. aliases (commercial or usual names, comma separated)
#. treatment (e.g. molded, rolled, normalized, etc.)
#. modulus of elasticity (E, in GPa)
#. modulus of rigidity (G, in GPa)
#. Poisson's ratio (nu)
#. volumic mass (often called density, in kg/m³)
#. tensile yield strength at 0,2 % (S_y, in MPa)
#. ultimate tensile strength (S_ut, in MPa)
#. thermal expansion coefficient (alpha, in µ/°C)
#. brinell hardness
#. Rockwell B hardness
#. Rockwell C hardness
#. Fatigue strength at 5E8 cycles (S_f, in MPa)

A ``.csv`` template is provided in the ``lib`` root.


#.    Check and ensure such data don't already exist to avoid duplicates
#.    Use the provided ``.csv`` template and open it in your favorite spreadsheet editor
#.    **IMPORTANT !** Use the same exact order of columns and symbols headers
#.    Ensure values have a correct number format in the final CSV file :

    *    numbers should use dots . as decimal separator
    *    numbers should not be into quotation marks "" meaning their format in the spreadsheet should be number
    *    numbers should not use thousands separators

#.    Include the data source (organization, book, etc.) of your data in the 1st line of the header. It will be used in the database as a comment and to ensure the trustability of the data
#.    Give your final CSV file a relevant name like ``material.csv``. For example : ``stainless-steel.csv``, ``carbon-steel.csv``, ``cast-iron.csv`` This name will be added into the database in the category column.
#.    Try to split your data into consistent files to keep less than ~ 100 entries in each files (for maintainability)
#.    Save your file into the proper directory : the one mentioning the source organization of the data or the standard used to compute/measure the data : ISO, ACNOR, SAE, ASHRAE, etc.


.. note:: 
    *    Use "dimensionless" as a unit for ratios and coefficients, and "none" if a unit is not relevant (for text) to ensure the correct column spacing.
    *    Use SI units ONLY ! British units will be converted on the fly in the code.
  
"""

import codecs
import csv
import os
import sqlite3
import sys


CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
PARENT_PATH = os.path.dirname(CURRENT_PATH)
sys.path.append(PARENT_PATH)

#TODO: update instead of overwriting previous database

#TODO: keep consistency if CSV columns headers don't match with database headers
    
def database_handle(db):
    """
    Create or overwrite the sqlite3 database and open a connection if it does.

    :param db: database filename
    :type db: str
    :return: connection socket to the sqlite3 database

    """

    database = open(os.path.abspath(db), "w")
    database.close()
    connection = sqlite3.connect(db)
    return connection


def create_tables(cursor, prop):
    """
    Create the relevant tables into the database

    :param cursor: sqlite 3 cursor
    :param prop: the desired property - for now : "materials"

    """
    if prop == "materials":
        cursor.execute("""CREATE TABLE IF NOT EXISTS materials 
                        (category text, -- category of material e.g. stainless steel, or tools steel, or carbon steel, or brass etc.
                        source text, -- source of the data, put in the data-sheet header
                        name text not null, -- normalized name of the material e.g. 4130, or 1010
                        aliases text, -- commercial or usual names coma separated e.g. Chromoly
                        treatment text, -- description of thermical and mechanical manufacturing
                        E real, -- GPa - modulus of elasticity
                        G real, -- GPa - modulus of rigidity
                        nu real, -- dimensionless - Poisson's ratio
                        rho real, -- kg/m^3 - volumic mass
                        S_y real, -- MPa - tensile yield strength at 0.2% offset
                        S_ut real, -- MPa - ultimate tensile strength
                        alpha real, -- E-6 / °C - thermal expansion coefficient
                        HB integer, -- Brinell hardness
                        HRB integer, -- Rockwell B hardness
                        HRC integer, -- Rockwell C hardness
                        S_f real -- MPa - fatigue strength at 5E8 cycles
                        ) 
                       """)


def check_pattern(line, prop):
    """
    Check and ensure that the properties are given in the expected order to avoid mixing up the columns

    :param line: the header line corresponding to the symbols of the given columns
    :type line: str list
    :param prop: the desired property to check
    :return: raise an error if given and expected headers don't match

    """
    if prop == 'materials':
        pattern = ['symbol', 
                   'none', 
                   '',
                   'E',  # GPa
                   'G',  # GPa
                   'nu',  # dimensionless
                   'rho',  # kg/m^3
                   'S_y',  # MPa
                   'S_ut',  # MPa
                   'alpha',  # E-6/°C
                   'HB',
                   'HRB',
                   'HRC',
                   'S_f'  # MPa
                   ]

    if pattern != line:
        raise NameError(
            "Database pattern and CSV file pattern do not match \n Given : %s \n Expected : %s" % line, pattern)


def SI_convert(line, prop):
    """
    Convert usual engineering units & multiples to SI units to normalize database
    
    .. note::  the units and multiple handled from the CSV data-sheet are considered\
    given in usual engineering habits (GPa, MPa, etc.) because they are human-readable\
    and standard tables are given is such units. \
    However, to make the database unit-independant and facilitate later querying,\
    multiples have to be normalized into SI standards.
    
    """

    if prop == "materials":
        # Mandatory values
        line[4] = float(line[4]) * 1E9  #: E : Convert GPa in Pa (SI)
        line[5] = float(line[5]) * 1E9  #: G : Convert GPa in Pa (SI)
        line[7] = float(line[7]) * 1E6  #: S_y : Convert MPa in Pa (SI)
        line[8] = float(line[8]) * 1E6  #: S_ut : Convert MPa in Pa (SI)
        
        # Optional values
        try:
            line[9] = float(line[9]) * 1E-6  #: alpha : Convert µ/°C in 1/°C
        except ValueError:
            print("Warning : Thermal expansion coefficient is missing and will be ignored")

    return line

def insert_property(prop, cursor, comment, category, line):
    """
    Build the database insertion with the relevant formatted data

    :param prop: the property to build
    :param cursor: the database cursor handler
    :param comment: the comment to add in every insertion, namely : the source of the data - should be the first line of the CSV data-sheet
    :param category: the category of the property to add. For exemple : cast iron, stainless steel, carbon steel, etc.
    :param line: the data line from the CSV data-sheet
    :type prop: string
    :type cursor: sqlite3 handler
    :type comment: string
    :type category: string
    :type line: list of strings

    """

    
    if prop == "materials":
        line = SI_convert(line, prop)
        save = tuple([category, comment] + line)
        print(save)
        cursor.execute("""INSERT INTO materials VALUES 
        (
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        )
        """ , save)


def parse_csv(PATH, cursor, database, prop):
    """
    Parse the CSV files and process their data

    :param PATH: root of all the librairies
    :param cursor: sqlite3 handler
    :param database: sqlite file
    :param prop: the given property

    """
    for (directory, _, files) in os.walk(PATH + prop):
        for f in files:
            if f.endswith('.csv'):

                print(os.path.join(directory, f))

                with codecs.open(os.path.join(directory, f), 'r', encoding="utf-8", errors="ignore") as csv_file:
                    # File name : extract the category of the data-sheet
                    category = f.replace('.csv', '').replace('-', ' ')
                    reader = csv.reader(csv_file, delimiter='\t')

                    i = 0

                    for line in reader:
                        if i == 0:
                            # First line : extract the comment/source of the
                            # data
                            comment = line[0]
                        if i == 2:
                            # Third line : extract the columns symbols header
                            # and check them
                            check_pattern(line, prop)
                        if i > 3:
                            # Fourth line and following : insert data into
                            # database
                            insert_property(
                                prop, cursor, comment, category, line)

                        i = i + 1


def build_property(prop):
    """
    Sequence of functions to build a new property into the database

    """
    PATH = os.path.dirname(prop)
    db = database_handle('properties.db')
    cursor = db.cursor()
    create_tables(cursor, prop)
    parse_csv(PATH, cursor, db, prop)
    db.commit()
    db.close()

if __name__ == '__main__':
    properties = ["materials"]
    for element in properties:
        build_property(element)
