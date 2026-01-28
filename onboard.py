import boto3
import csv
from botocore.exceptions import ClientError

# 1. Initialize the IAM Client globally
iam = boto3.client('iam')

# --------------------------
# Helper functions
# --------------------------

def create_iam_group(group_name):
    try:
        iam.create_group(GroupName=group_name)
        print(f"Created group: {group_name}")
    except iam.exceptions.EntityAlreadyExistsException:
        print(f"Group {group_name} already exists.")
    except ClientError as e:
        print(f"Unexpected error creating group {group_name}: {e}")

def create_login_profile(username, password):
    try:
        iam.create_login_profile(
            UserName=username,
            Password=password,
            PasswordResetRequired=True
        )
        print(f"Login profile created for {username}.")
    except iam.exceptions.EntityAlreadyExistsException:
        print(f"Login profile already exists for {username}.")
    except ClientError as e:
        print(f"Error creating login profile for {username}: {e}")

# --------------------------
# Main Logic
# --------------------------

def create_user(username, group_name):
    # 1. Create IAM User
    try:
        iam.create_user(UserName=username)
        print(f"Created user: {username}")
    except iam.exceptions.EntityAlreadyExistsException:
        print(f"User {username} already exists.")
    except ClientError as e:
        print(f"Unexpected error creating user {username}: {e}")
        return # Stop if we can't create user

    # 2. Ensure Group Exists (Self-Healing)
    # We can try to create it. If it exists, the exception handler catches it.
    # This is faster than "Check then Create" (EAFP principle).
    create_iam_group(group_name)

    # 3. Add User to Group
    try:
        iam.add_user_to_group(GroupName=group_name, UserName=username)
        print(f"Added {username} to {group_name}")
    except ClientError as e:
        print(f"Error adding {username} to {group_name}: {e}")

    # 4. Create Console Password
    create_login_profile(username, 'TempPass123!')

# --------------------------
# Execution
# --------------------------

if __name__ == '__main__':
    # Ensure you have employees.csv in the same folder!
    try:
        with open('employees.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user = row['user']
                dept = row['department']
                print(f"\nProcessing: {user} -> {dept}")
                create_user(user, dept)
    except FileNotFoundError:
        print("Error: employees.csv not found. Please create the file.")