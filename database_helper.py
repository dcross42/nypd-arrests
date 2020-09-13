from sqlalchemy import create_engine
from configparser import ConfigParser


#create the helper class object
class DBHelper():

    def __init__(self, config_file):
        self.conn = self.create_connection(config_file)
    

    '''
    PARAMS: username/password for db, db hostname/port, database type, database name
    default values are for PostgreSQL

    RETURNS: connection to database
    '''
    def create_connection(self, config_file):
        config = ConfigParser()
        config.read(config_file)
        creds = config['database']

        user = creds['user']
        db_type = creds['db_type']
        pword = creds['password']
        host = creds['host']
        database = creds['database']
        port = creds['port']

        engine_string = "{db_type}://{user}:{password}@{host}:{port}/{database}".format(user=user, 
                                                                                        password=pword, 
                                                                                        host=host, 
                                                                                        database=database, 
                                                                                        port=port, 
                                                                                        db_type=db_type)
        return create_engine(engine_string)




