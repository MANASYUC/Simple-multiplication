import random
import json
import os
from dotenv import load_dotenv
import sys



input1 = int(input('Enter your first number '))
input2 = int(input('Enter your second number '))


# Load environment variables from .env file
load_dotenv()

# Define the required JSON file
REQUIRED_JSON_FILE = "config.json"

def validate_json_file():
    # Get the expected password from the .env file
    expected_password = os.getenv("EXPECTED_PASSWORD")
    if not expected_password:
        print("Error: The expected password is not set in the .env file.")
        sys.exit(1)

    # Check if the JSON file exists
    if not os.path.exists(REQUIRED_JSON_FILE):
        print(f"Error: Required JSON file '{REQUIRED_JSON_FILE}' is missing.")
        sys.exit(1)

    # Try to read and parse the JSON file
    try:
        with open(REQUIRED_JSON_FILE, "r") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print(f"Error: JSON file '{REQUIRED_JSON_FILE}' is not valid.")
        sys.exit(1)

    # Check if the "Password" key exists in the JSON file
    json_password = data.get("Password")
    if not json_password:
        print("Error: 'Password' key is missing in the JSON file.")
        sys.exit(1)

    # Validate the password in the JSON file against the .env password
    if json_password != expected_password:
        print("Error: The password in the JSON file does not match the expected password.")
        sys.exit(1)

    print("JSON file validated successfully. Proceeding with the script...")

# Main script logic
if __name__ == "__main__":
    validate_json_file()
    input3 = int(input('Enter your third number '))
    input3 = int(input('Enter your third number '))
    rand_num = random.randint(0,10)
    print(f'Differnece of num2 & num3 = {input2 - input3}')

    # Add the rest of your script logic here
    print("Main script is running...")
else:


    print(f'The result of multiplication is = {input1 * input2}')
    print(f'Difference of num1 & num2 = {input1 - input2}')




