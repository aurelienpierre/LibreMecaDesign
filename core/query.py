# -*- coding: utf-8 -*-
"""
Provide the base-level search class (layer 0) to fetch values from the database \
and store them into a class
"""

import os
import re
import sqlite3
import sys

from lib import aliases


CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
PARENT_PATH = os.path.dirname(CURRENT_PATH)
sys.path.append(PARENT_PATH)


class search:
    """
    Handle the queries
    """

    def remove_units(self, query_string):
        """
        Replace multiples and units strings by numbers

        """

        equation = re.compile("[0-9]")

        if equation.search(query_string):
            # Clean spaces
            query_string = query_string.strip()
            # Look for multiples symbols
            multiple = re.compile('|'.join(aliases.multiples.keys()))
            # Replace multiples by corresponding values
            result = multiple.sub(lambda x: aliases.multiples[x.group()],
                                  query_string)
            # Look for remaining units
            unit = re.compile('[A-Za-z]+$')
            # Delete units
            result = unit.sub('', result)
        else:
            result = query_string.strip()

        return result

    def prepare_query(self, query_string):
        """
        Split a query string into keywords and interpretate boolean operators

        :param query_string: unformatted string

        :return: nested list of lists of terms to search alternatively

            * the top level list contains the OR arguments
            * the nested lists contain the AND argument

        """

        OR_split = query_string.split('OR')

        self.terms = []

        for element in OR_split:
            AND_split = element.split('AND')
            self.terms.append(AND_split)


    def clean_query(self, queries):
        """
        Shortcut to loop remove_unit element by element in the terms list or nested list
        """
        for i in range(0, len(queries)):
            try:  # Case : simple list
                queries[i] = self.remove_units(queries[i])
            except:  # Case : nested list of lists
                for j in range(0, len(queries[i])):
                    queries[i][j] = self.remove_units(queries[i][j])
        return

    def build_request(self):
        """
        Build the sqlite3 request with the terms
        """
        request = ""
        equation = re.compile(r"[\=\>\<]+")
        for element in self.terms:  # OR statements
            last = str(self.terms[-1])
            for sub_element in element:  # AND statements

                text = str(sub_element)
                sub_last = str(element[-1])

                # Case : explicit symbol + operator + value declaration
                if equation.search(sub_element):
                    request = request + text
                    # Case : not the last element of the list
                    if len(element) > 1 and str(sub_element) != sub_last:
                        request = request + ' AND '
                # Case : implicit string
                else:

                    request = (
                                request +
                                " name LIKE '%" + text +
                                "%' OR aliases LIKE '%" + text +
                                "%' OR treatment LIKE '%" + text +
                                "%' OR category LIKE '%" + text +
                                "%' ")
                    # Case : not the last element of the list
                    if len(element) > 1 and str(sub_element) != sub_last:
                            request = request + ' AND '

            if len(self.terms) > 1 and str(element) != last:
                request = request + ' OR '

        return request

    def process_query(self):
        """
        Fetch all the matching results

        :return: self.results property
        :rtype: a list of all matching results built into \
        dictionaries where the key is the property symbol and \
        the value comes from the database
        """
        filename = os.path.abspath('../lib/properties.db')
        self.results = []
        with sqlite3.connect(filename) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM materials WHERE {r}".format(r=self.build_request()))
            i = 0
            for row in cursor.fetchall():
                self.results.append({})
                for field in row.keys():
                    self.results[i][field] = row[field]
                i = i + 1

    def __init__(self, query_string):
        self.prepare_query(query_string)
        self.clean_query(self.terms)
        self.process_query()
        # TODO! add units
        # TODO! add filters to keep only one value (max, min)

if __name__ == '__main__':
    q_string = 'steel AND S_y > 400 MPa AND S_ut > 500 MPa AND temper OR rolled'
    a = search(q_string)
    
    for item in a.results:
        print(item['category'], item['name'],item['S_ut'], item['treatment'])
