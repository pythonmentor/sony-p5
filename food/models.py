#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This module manage....................."""

from database_xchange.database import db # db = my_database with mysql-connector

from database_xchange.managers import CategoryManager, ProductManager, FavoriteManager


class Category:

    objects = CategoryManager(db)
    
    def __init__(self, name=None, products=None):
        self.id_category = None
        self.name = name
        self.products = products

class Product:

    objects = ProductManager(db)

    def __init__(self,
                 name=None,
                 description=None,
                 nutriscore=None,
                 url=None,
                 store=None,
                 categories=None,
                 ):
        self.id_product = None
        self.name = name
        self.description = description
        self.nutriscore = nutriscore
        self.url = url
        self.store = store
        self.categories = categories

class Favorite:

    objects = FavoriteManager(db)

    def __init__(self,
                 id_product_origin=None,
                 id_product_substitute=None, 
                 request_date=None
                 ):
        self.id_favorite = None
        self.id_product_origin = id_product_origin
        self.id_product_substitute = id_product_substitute
        self.request_date = request_date
