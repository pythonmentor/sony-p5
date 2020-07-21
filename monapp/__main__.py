#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Purebeurre Application 'MyFoodApp' The Aim of this application is to
suggest a healthiest food than the original choice of a user.

Script Python
Files: settings.py, __main__.py, api.py, config.py, managers.py,
parsecleaner.py, upload.py, views.py
"""


from api_xchange.api import GetApiData
from food.parsecleaner import Parser
from database_xchange.upload import Upload
from database_xchange.managers import DataMgt
from user_interface.views import App


def main():
    """Method to launch the app."""

    content = DataMgt()
    if not content.is_database_empty():  # check content of table Product
        api = GetApiData()
        api.download_data()  # if yes, launch api request
        liste = Parser(api.api_result)  # parse api result
        liste.clean()  # clean api result
        data = Upload(liste.products_list)
        data.load_category()  # upload table categories content
        data.load_products()  # upload table products content
    session = App()
    session.start()  # launch the client app


if __name__ == '__main__':
    main()
