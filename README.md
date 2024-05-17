# UoS - Take home Assignment

Task Description:
1. Use the provided Customer and Order CSV files to create corresponding tables in a database.

Tech Stack:

Programming: Python 3.x
AWS Serverless - Lambda Function
AWS RDS- MySQL
AWS S3, SSM, Cloud Watch.

Design Approach:

![image](https://github.com/Nanda-Vishvanathan/uosheffield-database-initializer-lambda/assets/59757238/33259d30-dd55-4171-81de-5c57d686ea87)


Code Walkthrough:

As part of task 1, this project contains the code for an AWS Lambda function that initializes a database with Customers and Orders tables. The data for these tables is fetched from CSV files stored in an S3 bucket, processed, and uploaded to the database.

To use the code, please follow the instructions below:

Clone the code: 
git clone https://github.com/Nanda-Vishvanathan/uosheffield-database-initializer-lambda.git

Create a new branch
git checkout -b <branch_name>

Make the changes & push to the repo.
git add .
git commit -m "Description of changes"
git push origin <branch_name>

To deploy please, follow the steps below:

please install the requirements.txt from the folder
pip install -r requirements.txt -t .

Zip the code using the following command:
zip -r database_intializer_lambda.zip .

Deploy it using manually, s3 or using CLI.
