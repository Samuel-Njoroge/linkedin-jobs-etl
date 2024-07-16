# LinkedIn Data Extraction and PostgreSQL Integration ETL .
This project focuses on extracting data from LinkedIn using the LinkedIn Data API and subsequently loading that data into a PostgreSQL database using Python. The goal is to automate the data retrieval process, allowing for efficient data storage and analysis. By leveraging the LinkedIn Data API, the project aims to gather valuable insights from professional networking data, which can be utilized for various analytical purposes.

## Project Architecture
![](https://github.com/Samuel-Njoroge/linkedin-jobs-etl/blob/main/project_architecture.svg)

## Objectives
- To extract relevant professional data from LinkedIn using the LinkedIn Data API.
- To clean and transform the extracted data to ensure it is structured and ready for analysis.
- To load the cleaned data into a PostgreSQL database for further analysis and reporting.
- To create a streamlined process that can be reused for future data extraction tasks from LinkedIn.

## Tools and Technologies
- `LinkedIn Data API`: For accessing and extracting professional data from LinkedIn.
- `Python`: The primary programming language used for scripting and automation.
- `Pandas`: For data manipulation and cleaning before loading into PostgreSQL.
- `SQLAlchemy`: For ORM (Object Relational Mapping) to interact with the PostgreSQL database.
- `PostgreSQL`: The database management system used for storing the extracted data.
- `Requests`: A Python library for making HTTP requests to the LinkedIn Data API.

## Skills Developed
- `API Integration`: Gained experience in working with APIs, including authentication, data retrieval, and error handling.
- `Database Management`: Improved skills in using PostgreSQL for data storage, including schema design and SQL queries.
- `Data Processing`: Enhanced ability to manipulate and clean data using Pandas, ensuring data quality for analysis.
- `Python Programming`: Strengthened proficiency in Python programming, focusing on data extraction, transformation, and loading (ETL) processes.

## Installation
1. Clone the repository
```sh   
git clone https://github.com/Samuel-Njoroge/linkedin-jobs-etl
```
```sh
cd linkedin-jobs-etl
```
2. Install the required packages:

```sh
pip install -r requirements.txt
```
3. Run the `etl_pipeline.py`
```sh
python etl_pipeline.py
```

## Usage
1. Create an account in [Rapid API](https://rapidapi.com/hub).
2. Subscribe to the [LinkedIn Data API](https://rapidapi.com/rockapis-rockapis-default/api/linkedin-data-api)
3. Run the `etl_pipeline.py` data extraction and loading script:
```sh
python etl_pipeline.py
```

The data will be automatically loaded into the specified PostgreSQL database.

## Contributing
Contributions to improve the project are welcome! 

Please feel free to fork the repository and submit a pull request.
