# UoS - Take home Assignment

Task Description:
1. Use the provided Customer and Order CSV files to create corresponding tables in a database.

Tech Stack:

Programming: Python 3.x
AWS Serverless - Lambda Function
AWS RDS- MySQL
AWS S3, SSM, Cloud Watch.

Design Approach:

![image](https://github.com/Nanda-Vishvanathan/uosheffield-database-initializer-lambda/assets/59757238/36866f86-aa88-4fd4-94c6-2dbbdc000e2a)

Code Walkthrough:

As part of task 1, this code is hosted as an AWS lambda function that create initializes/creates the database with Customers and Orders table. The given CSV are stored in S3 bucket and the code fetch 
