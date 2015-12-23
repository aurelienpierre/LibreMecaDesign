# -*- coding: utf-8 -*-
'''

'''


def q_string(query_string):
    """
    Split a query string into keywords and interprate boolean operators
        :query_string: unformatted string

    Output :
        :OR: list of terms to search alternatively
        :AND: list of sets to search together

    """

    OR_split = query_string.split('OR')

    AND = []
    OR = []

    for element in OR_split:
        if "AND" in element:
            AND_split = element.split('AND')
            AND.append(set(AND_split))
        else:
            OR.append(element)

    return OR, AND


if __name__ == '__main__':
    q_string('steel query OR string AND bla AND ta soeur OR 2e test AND shit')
