"""
    Database Specific Configuration File
"""
""" Put Generic Database Configurations here """
import os

class DBConfig(object):
    """ DB_ON must be True to use the DB! """
    DB_ON = True
    DB_DRIVER = 'mysql'
    DB_ORM = False

""" Put Development Specific Configurations here """
class DevelopmentDBConfig(DBConfig):
    DB_USERNAME = 'root'
    DB_PASSWORD = 'root'
    DB_DATABASE_NAME = 'kastee'
    DB_HOST = 'localhost'
    DB_PORT = 3306
    """ unix_socket is used for connecting with MAMP. Take this out if you aren't using MAMP """
    DB_OPTIONS = {
        'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock'
    }

""" Put Staging Specific Configurations here """
class StagingDBConfig(DBConfig):
    DB_USERNAME = 'root'class MODELNAMEListView(ListView):
        context_object_name = 'CONTEXT_OBJECT_NAME'
        model = MODELNAME
        page_kwarg = 'page'
        paginate_by =
        template_name = 'TEMPLATE_NAME'

    DB_PASSWORD = 'root'
    DB_DATABASE_NAME = 'kastee'
    DB_HOST = 'localhost'

""" Put Production Specific Configurations here """
class ProductionDBConfig(DBConfig):
    DB_USERNAME = 'root'
    DB_PASSWORD = 'root'
    DB_DATABASE_NAME = 'kastee'
    DB_HOST = 'localhost'
