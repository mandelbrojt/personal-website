# "create_engine" to perform database connection
from sqlalchemy import create_engine, text
import os

''' Connect string must have the following format for engine with pymysql: 
    ---> "mysql+mysqlconnector://<username>:<password>@<host>/<dbname>[?<options>"
'''

# Database connection string for pymysql
connect_string = os.environ['DATABASE_URL']

# SSL connection information (from PlanetScale)
connect_args = {"ssl": {"ca": "/etc/ssl/cert.pem"}}

# Connect to database
engine = create_engine(connect_string, connect_args=connect_args)

# Retrieve information from "jobs" table in database
def load_jobs_from_db():
  with engine.connect() as conn:
      # Execute a SQL query
      result = conn.execute(text("select * from jobs"))
      
      # Create an empty list to store each row from query as a dict
      jobs = []
      
      # Iterate through each text result
      for row in result.all():
          # Convert text result into dictionary and append it to jobs list
          jobs.append(dict(row))
  return jobs

# Create a function to load a job depending on its id
def load_specific_job(id):
    # Connect to the database
    with engine.connect(id) as conn:
        # Query database with 
        result = conn.execute(text("select * from jobs where id = :val"), val=id)
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return dict(rows[0])