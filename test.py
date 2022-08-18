import sqlalchemy
from sqlalchemy import create_engine

db_string = "postgresql://{}:{}@{}:{}/{}".format('<user>', '<password>', '<server-host>', '5432', '<database-name>')

engine = create_engine(db_string)
con = engine.raw_connection()
cur = con.cursor()

'''
function clone_schema() takes 5 arguments
1. Source schema name 
2. Destination schema name 
3. Bool - Copy records from source to destination
4. Bool - Copy DDL only
5. Bool - Print verbose messages - Defalt False
'''
cur.execute("select public.clone_schema('ref_schema', 'new_schema', True, False, False)")

con.commit()

print('Schema cloned!')