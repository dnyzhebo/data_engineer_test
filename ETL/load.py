import csv
import psycopg2

def load_to_postgres(file_path, db_config):
    # Connect to the PostgreSQL database
    try:
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

    # PostgreSQL database configuration
    db_config = {
        "host": "localhost",
        "database": "etl_db",
        "user": "postgres",
        "password": "your_password",
        "port": 5432
    }

    load_to_postgres(file_path, db_config)