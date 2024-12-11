# OkatuAI
Made by Matthew Osorio
## What is it?
An application that allows user to keep track of their favorite anime and manga. If the user needs new anime or manga to endulge in they will be recommended anime or manga by ChatGPT
## Prerequisites
- python3.12 or greater
- OpenAI
- OpenAI API Key
- PostgreSQL 16.2 or greater
- Psycopg

    ```
    pip install openai
    pip install psycopg
    ```
## How to run locally 
1) Import OkatuAI schema and data to PostgreSQL database

    ```
    createdb -U <username> <target_database>
    psql -U <username> -d <target_database> -f otakuai_schema.sql
    psql -U <username> -d <target_database> -f otakuai_data.sql
    ```
2) Update the connection to the PostgreSQL with your credentials in src/BackEnd/Classes/DBCredentials.py
3) Run the main.py file in the 'src' directory

    On Windows:
    ```
    python main.py
    ```
    On Mac:
    ```
    python3 main.py
    ```