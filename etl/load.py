import csv
import psycopg2
import os

def load_to_postgres(file_path):
    """
    Load transformed CSV data into a PostgreSQL database.

    :param file_path: Path to the transformed CSV file.
    """
    # Get database configuration from environment variables
    db_config = {
        "host": os.getenv("DATABASE_HOST", "localhost"),
        "database": os.getenv("DATABASE_NAME", "etl_db"),
        "user": os.getenv("DATABASE_USER", "etl_user"),
        "password": os.getenv("DATABASE_PASSWORD", "secure_password_123"),
        "port": int(os.getenv("DATABASE_PORT", 5432)),
    }

    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        # Create the table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            signup_date DATE NOT NULL,
            domain TEXT NOT NULL
        );
        """)

        # Open the transformed CSV file
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            # Insert each row into the database
            for row in reader:
                cursor.execute("""
                INSERT INTO users (name, email, signup_date, domain)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (email) DO NOTHING;
                """, (row['name'], row['email'], row['signup_date'], row['domain']))

        # Commit the transaction and close the connection
        conn.commit()
        cursor.close()
        conn.close()

        print(f"Data from '{file_path}' successfully loaded into PostgreSQL.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Path to the transformed CSV file
    file_path = "data/transformed.csv"

    # Call the function to load data into PostgreSQL
    load_to_postgres(file_path)
