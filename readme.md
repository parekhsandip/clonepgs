## Clone/Duplicate PostgreSQL Schema with or without data
- The solution uses PostgreSQL function in select statement to generate cloned schema.
- Use the clone_schema.sql [original code](https://github.com/denishpatel/pg-clone-schema) to create two functions in your database' default schema.
- test.py is a simple python script to test the function via code.