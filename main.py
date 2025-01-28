from etl.generate_csv import generate_csv
from etl.transform import transform_data
from etl.load import load_to_postgres

def main():
    # Set the number of records you want to generate
    num_records = 1100  # Change this number as needed

    # Step 1: Generate CSV
    print(f"Generating CSV with {num_records} records...")
    generate_csv("data/data.csv", num_records)

    # Step 2: Transform Data
    print("Transforming data...")
    transform_data("data/data.csv", "data/transformed.csv")

    # Step 3: Load Data into PostgreSQL
    print("Loading data into PostgreSQL...")
    load_to_postgres("data/transformed.csv")

if __name__ == "__main__":
    main()
