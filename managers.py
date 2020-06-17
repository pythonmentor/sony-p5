#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This module manage all the dialogue with in MySQL."""

from datetime import datetime
import mysql.connector

from config import info_bdd


class DataMgt:
    """Management of all SQL request."""

    def __init__(self):
        self.selected_prod = ()
        self.product_origin = ()
        self.product_substitute = ()
        self.my_database = mysql.connector.connect(**info_bdd)
        self.my_cursor = self.my_database.cursor()
        self.category_selected = ()

    def get_all_cat(self):
        """retrieve all categories."""

        self.my_cursor.execute("SELECT id_category, name FROM Categories")
        self.myresult_0 = self.my_cursor.fetchall()
        return self.myresult_0

    def get_prod_by_category(self, category_selected):
        """retrieve product by category."""

        query = ("SELECT id_product, name, brand, id_category, nutriscore,"
                 " description, store FROM Products "
                 "WHERE id_category = %s ORDER BY name")
        self.my_cursor.execute(query, (category_selected,))
        myresult = self.my_cursor.fetchall()
        return myresult

    def get_one_prod(self, id_product):
        """retrieve a product and all the information associated with the
        id_product input."""

        query = ("SELECT id_product, name, brand, id_category, nutriscore,"
                 " description, store FROM Products "
                 "WHERE id_product = %s")
        self.my_cursor.execute(query, (id_product,))
        myresult = self.my_cursor.fetchall()
        return myresult

    def save_substitute(self, product_origin, product_substitute):
        """save substitute product in database."""

        date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.my_database = mysql.connector.connect(**info_bdd)
        self.my_cursor = self.my_database.cursor()
        query = (
            "INSERT INTO Favorites (id_product_origin, product_origin_name,"
            " product_origin_nutriscore, id_product_substitute,"
            " product_substitute_name, product_substitute_nutriscore,"
            " request_date) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        )
        data = (product_origin[0], product_origin[1], product_origin[4],
                product_substitute[0], product_substitute[1],
                product_substitute[6], date_time
                )
        self.my_cursor.execute(query, data)
        self.my_database.commit()

    def get_all_favorites(self):
        """retrieve all substitutes products saved in database."""

        self.my_cursor.execute(
            "SELECT * FROM Favorites ORDER BY id_favorite DESC")
        self.myresult_1 = self.my_cursor.fetchall()
        return self.myresult_1

    def suggest_substitute(self, product_origin):
        """suggest a substitute with a better nutriscore than the product
        selected by the user."""

        query1 = ("SELECT id_product, name, description, store, url, brand,"
                  " nutriscore FROM Products "
                  "WHERE id_category = %s AND nutriscore < %s")
        self.my_cursor.execute(query1, (product_origin[3], product_origin[4],))
        myresult = self.my_cursor.fetchall()
        if not myresult:
            query2 = ("SELECT id_product, name, description, store, url,"
                      " brand, nutriscore FROM Products "
                      "WHERE id_category = %s AND nutriscore = %s")
            self.my_cursor.execute(
                query2, (product_origin[3], product_origin[4],))
            myresult = self.my_cursor.fetchall()
        return myresult

    def is_database_empty(self):
        """test if Table product is empty."""

        query = ("SELECT 1 FROM Products LIMIT 1")
        self.my_cursor.execute(query)
        content = self.my_cursor.fetchall()
        return content
