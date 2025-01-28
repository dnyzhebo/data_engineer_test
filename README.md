ETL Pipeline with Docker
========================

This project implements an ETL (Extract, Transform, Load) pipeline using Python and Docker. The pipeline consists of:
1. Generating fake user data.
2. Transforming the data.
3. Loading the data into a PostgreSQL database.

---------------------------
GETTING STARTED
---------------------------

Prerequisites:
- Docker and Docker Compose installed on your system.
- Basic knowledge of Docker and command-line tools.

---------------------------
HOW TO BUILD AND RUN DOCKER CONTAINERS
---------------------------

1. Clone the Repository:
    git clone https://github.com/dnyzhebo/data_engineer_test
    cd data_engineer_test

2. Create a `.env` File:
    Create a `.env` file in the root directory with the following content:
        DATABASE_HOST=postgres
        DATABASE_NAME=etl_db
        DATABASE_USER=etl_user
        DATABASE_PASSWORD=secure_password_123
        DATABASE_PORT=5432

3. Build the Docker Images:
    docker compose build

4. Start the Services:
    docker compose up -d

5. Monitor the Logs:
    docker compose logs -f

---------------------------
HOW TO RERUN THE ETL PROCESS
---------------------------

Option 1: Restart the ETL App
    docker compose restart etl_app

Option 2: Run the ETL App as a One-Off Container
    docker compose run etl_app

---------------------------
DATABASE SCHEMA
---------------------------

The database consists of a single table named `users`. Below is the schema:

    Column Name   | Data Type   | Constraints        | Description
    --------------|-------------|--------------------|-----------------------------------------
    user_id       | SERIAL      | Primary Key        | Auto-incrementing unique user ID.
    name          | TEXT        | NOT NULL           | User's full name.
    email         | TEXT        | NOT NULL, UNIQUE   | User's email address. Must be unique.
    signup_date   | DATE        | NOT NULL           | Date when the user signed up (YYYY-MM-DD).
    domain        | TEXT        | NOT NULL           | Email domain extracted from `email`.

---------------------------
ASSUMPTIONS
---------------------------

1. Data Generation:
   - Fake user data is generated using the `Faker` library.
   - A predefined list of email domains is used.

2. Data Transformation:
   - Dates are converted to `YYYY-MM-DD` format.
   - Email domains are extracted from the `email` field.
   - Rows with invalid emails are handled gracefully.

3. Database Connection:
   - The ETL app connects to PostgreSQL using the hostname `postgres`, which resolves via Docker Compose networking.

4. Data Persistence:
   - PostgreSQL data is stored in a named volume (`postgres_data`) to ensure persistence across container restarts.

---------------------------
HOW TO VERIFY THE RESULTS
---------------------------

1. Connect to PostgreSQL:
    docker exec -it etl_postgres psql -U etl_user -d etl_db

2. Query the `users` Table:
    SELECT * FROM users LIMIT 10;

3. Check Transformed Data:
    cat data/transformed.csv

---------------------------
TROUBLESHOOTING
---------------------------

1. Hostname Resolution Issues:
   - If you encounter the error:
        "could not translate host name 'postgres' to address"
   - Ensure that you’re running the ETL app as part of the Docker Compose network.

2. Data Directory Issues:
   - Ensure the `data` directory exists or is dynamically created by the ETL scripts:
        mkdir data

3. Logs:
   - Check the logs for detailed error messages:
        docker compose logs etl_app
        docker comp
