#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This module manage the uploading of the cleaned data in MySQL."""

import mysql.connector

from database_xchange.config import info_bdd
from settings import param_categories


class Upload:
    """This class will populate the DB with cleaned data from the module
    parsecleaner."""

    def __init__(self, product_list):
        self.my_database = mysql.connector.connect(**info_bdd)
        self.my_cursor = self.my_database.cursor()
        self.product_list = product_list

    def load_category(self):
        """Load data in Categories TABLE."""

        for i in range(len(param_categories)):
            cat = (param_categories[i]).title()
            self.my_cursor.execute(
                "INSERT INTO Categories (name) VALUES (%s)", (cat,))
            self.my_database.commit()
        self.my_cursor.close()
        self.my_database.close()

    def load_products(self):
        """Load data in Products TABLE."""

        self.my_database = mysql.connector.connect(**info_bdd)
        self.my_cursor = self.my_database.cursor()
        for i in range(len(self.product_list)):
            query = ('INSERT INTO Products '
                     '(name, brand, description, nutriscore, store, url,'
                     ' id_category) '
                     'VALUES (%(product_name)s, %(brands)s, '
                     '%(generic_name)s, %(nutriscore_grade)s, '
                     '%(stores)s, %(url)s, %(id_category)s)')
            data = self.product_list[i]
            self.my_cursor.execute(query, data)
            self.my_database.commit()
        self.my_cursor.close()
        self.my_database.close()
        print('Database updated. Ready to be used...')
