import pandas as pd
from database_helper import DBHelper
from configparser import ConfigParser

#get database connection
db = DBHelper('config.ini')
print(db.conn)

#get credentials from config file
config = ConfigParser()
config.read('config.ini')
creds = config['database']



#specify data types and date columns
dtypes = {
'ARREST_KEY' : 'int64',
'ARREST_DATE' : 'object',
'PD_CD' : 'float64',
'PD_DESC' : 'object',
'KY_CD' : 'float64',
'OFNS_DESC' : 'object',
'LAW_CODE' :  'object',
'LAW_CAT_CD' : 'object',
'ARREST_BORO' :  'object',
'ARREST_PRECINCT' : 'int64',
'JURISDICTION_CODE' :  'float64',
'AGE_GROUP' :  'object',
'PERP_SEX' : 'object',
'PERP_RACE' :  'object',
'X_COORD_CD' : 'float64',
'Y_COORD_CD' : 'float64',
'Latitude' : 'float64',
'Longitude' : 'float64'
}

dates = ['ARREST_DATE']


#read the csv
arrests = pd.read_csv('NYPD_Arrests_Data__Historic_.csv', dtype=dtypes, parse_dates=dates)

#push to the database, fail if exists as this is a one-time upload
arrests.to_sql(name='nypd_arrests', con=db.conn, if_exists='fail' )