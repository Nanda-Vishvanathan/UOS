# UoS - Take home Assignment

**Task Description:**
1. Use the provided Customer and Order CSV files to create corresponding tables in a database.

**Tech Stack:**

1. Programming: Python 3.x<br>
2. AWS Serverless - Lambda Function<br>
3. AWS RDS- MySQL<br>
4. AWS S3, SSM, Cloud Watch.<br>


**Design Approach:**

![image](https://github.com/Nanda-Vishvanathan/uosheffield-database-initializer-lambda/assets/59757238/33259d30-dd55-4171-81de-5c57d686ea87)


**Code Walkthrough:**

As part of task 1, this project contains the code for an AWS Lambda function that initializes a database with Customers and Orders tables. The data for these tables is fetched from CSV files stored in an S3 bucket, processed, and uploaded to the database.


**Code Use**

Clone the code:<br>
***git clone https://github.com/Nanda-Vishvanathan/uosheffield-database-initializer-lambda.git<br>***

Create a new branch<br>
***git checkout -b <branch_name><br>***

Make the changes & push to the repo.<br>
***git add .<br>***
***git commit -m "Description of changes"<br>***
***git push origin <branch_name><br>***

To deploy please, follow the steps below:

please install the requirements.txt from the folder<br>
***pip install -r requirements.txt -t .<br>***

Zip the code using the following command:<br>
***zip -r database_intializer_lambda.zip .<br>***

Deploy it using manually, s3 or using CLI.
