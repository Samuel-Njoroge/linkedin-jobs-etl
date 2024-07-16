# Importing libraries
import requests
import json
import pandas as pd
import csv
import psycopg2


# API Connection
url = "https://linkedin-data-api.p.rapidapi.com/search-jobs"

querystring = {"keywords":"dataengineer","locationId":"92000000","datePosted":"anyTime","sort":"mostRelevant"}

headers = {
	"x-rapidapi-key": "2be5d5701bmsh9cfd68b52506516p147db3jsn4d8e5fc63a17",
	"x-rapidapi-host": "linkedin-data-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# Save data into a json file
data = response.json()

# Save data into a file
filename = 'linkedin_jobs.json'
with open(filename, 'w') as file:
    json.dump(data, file)


# Read data into a dataframe
df = pd.read_json('linkedin_jobs.json')

# Normalize the data
df = pd.json_normalize(df['data'])

# Dataframe to CSV
file_path = 'data_engineer_jobs.csv'

df.to_csv(file_path, index=False)

# Postgres connection
def get_db_connection():
    connection = psycopg2.connect(
        host='localhost',
        database='postgres',
        user='postgres',
        password='postgres'
    )
    return connection

conn = get_db_connection()

# Creating database table
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    create_table_query = '''CREATE SCHEMA IF NOT EXISTS jobs;
                            DROP TABLE IF EXISTS jobs.data_engineer;

                            CREATE TABLE jobs.data_engineer(
                            id VARCHAR PRIMARY KEY,
                            title VARCHAR,
                            url VARCHAR,
                            referenceId VARCHAR,
                            posterId VARCHAR,
                            location VARCHAR,
                            type VARCHAR,
                            postDate VARCHAR,
                            benefits VARCHAR,
                            companyname VARCHAR,
                            companylogo VARCHAR,
                            companyurl VARCHAR
                            );'''
    
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()

create_table()

# Load csv data to database

def load_data_from_csv_to_table(csv_path, table_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            placeholder = ','.join(['%s'] * len(row))
            query = f'INSERT INTO {table_name} VALUES ({placeholder});'
            cursor.execute(query, row)
    conn.commit()
    cursor.close()
    conn.close()

# Load  data to database
data_engineer_csv_path = r'./data/data_engineer_jobs.csv'
load_data_from_csv_to_table(data_engineer_csv_path, 'jobs.data_engineer')

print('Data Loaded success fully')