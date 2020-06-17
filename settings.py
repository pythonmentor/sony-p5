#!/usr/bin/python
# -*- coding: utf-8 -*-

"""This module content all the constant values defined for the App."""

# URL link for API call
URL = 'https://fr.openfoodfacts.org/cgi/search.pl'

# Categories used as parameters for the API OpenFoodFact request
param_categories = ['Snacks',
                    'fromages',
                    'Boissons',
                    'Plats préparés à réchauffer au micro-ondes',
                    'Tartes salées',
                    'Biscuits et gâteaux',
                    'Glaces']

# categories uploaded and display in database purebeurre
category_app = {1: 'Snacks',
                2: 'Fromages',
                3: 'Boissons',
                4: 'Plats préparés (micro-ondes)',
                5: 'Tartes salées',
                6: 'Biscuits et gâteaux',
                7: 'Glaces'
                }

# features for definition of a product
fields = ['product_name', 'brands', 'generic_name',
          'nutriscore_grade', 'stores', 'url']

# Number of product retrieved by page after a API call """
NBR_PRODUCT_PER_PAGE = 100  # 20, or 50, or 100, or 250, or 500 or 1000
