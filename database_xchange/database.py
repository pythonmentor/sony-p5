#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This module manage the connection to purebeurre database"""

import mysql.connector

from .config import info_bdd

db = mysql.connector.connect(**info_bdd)
