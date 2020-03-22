import os
import mysql.connector
from mysql.connector import errorcode
import logging
import medishare_tables

logger = logging.getLogger('module medishare_db')
logger.setLevel(logging.DEBUG)

config = {
    'user': 'root',
    'password': 'test123',
    'host': 'localhost',
    'database': 'medishare'
}

def connect_dbms(config, logger):
    try:
        cnx = mysql.connector.connect(user=config['user'], password=config['password'])
        logger.info('connected DBMS')
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_CHANGE_USER_ERROR:
            logger.error('access denied, username or password are wrong! errormessage:', err)
        else:
            logger.error('an error has occurred! errormessage:', err)
        return None

def create_db(config, cursor, logger):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(config['database']))
        logger.info('created database', config['database'])
    except mysql.connector.Error as err:
        logger.error("Failed creating database: {}".format(err))
        exit(1)

def connect_db(config, logger):
    try:
        cnx = mysql.connector.connect(**config)
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_CHANGE_USER_ERROR:
            logger.error('access denied, username or password are wrong! errormessage:', err)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            logger.error('database does not exist! errormessage:', err)
        else:
            logger.error('an error has occurred! errormessage:', err)
        return None

cnx = connect_dbms(config, logger)
cursor = cnx.cursor()
try:
    cursor.execute("USE {}".format(config['database']))
except mysql.connector.Error as err:
    logger.error("Database {} does not exists.".format(config['database']))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_db(config, cursor, logger)
        logger.error("Database {} created successfully.".format(config['database']), err)
        cnx.database = config['database']
    else:
        logger.error('an error has occurred! errormessage:', err)
        exit(1)

for table_name in medishare_tables.TABLES:
    table_description = medishare_tables.TABLES[table_name]
    try:
        logger.info("Creating table {}: ".format(table_name))
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            logger.error('already exists.')
        else:
            logger.error(err.msg)
    else:
        logger.info('OK')

cursor.close()
cnx.close()