import csv
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker for generating fake data
faker = Faker()

# Number of records to generate
num_records = 1000

# Define the output file path
output_file = "data/data.csv"

# Predefined list of email domains
email_domains = [
    "example.com",
    "sample.net",
    "test.org",
    "demo.io",
    "fakeemail.com",
    "mockmail.org",
    "placeholder.net",
    "tempemail.com",
    "randomdomain.co"
]


def generate_random_datetime(start_date, end_date):
    """
    Generate a random datetime between start_date and end_date.
    """
    delta = end_date - start_date
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return start_date + timedelta(seconds=random_seconds)


def generate_csv(file_path, num_records):
    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["user_id", "name", "email", "signup_date"])

        for user_id in range(1, num_records + 1):
            name = faker.name()

            # Generate random email with a random domain
            username = faker.user_name()
            domain = random.choice(email_domains)
            email = f"{username}@{domain}"

            # Generate random signup date and time within the past 2 years
            start_date = datetime.now() - timedelta(days=365 * 2)
            end_date = datetime.now()
            signup_date = generate_random_datetime(start_date, end_date).strftime("%Y-%m-%d %H:%M:%S")

            # Write the generated record to the CSV file
            writer.writerow([user_id, name, email, signup_date])

    print(f"CSV file '{file_path}' successfully created with {num_records} records.")


if __name__ == "__main__":
    generate_csv(output_file, num_records)