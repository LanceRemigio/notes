# Select Distinct 

- Basic Syntax and use cases
- Select distinct examples
- Distinct on multiple columns
- Select disinct on `NULL` 



We will learn how to filter our data by removing duplicate rows with the `DISTINCT` clause.


## Basic Syntax and use cases

Consider the syntax in the following statement:
````sql
SELECT DISTINCT select_list 
FROM table;
````
- Always put the `DISTINCT` clause right after the `SELECT` statement.

- Then specify the column or list of columns after the `DISTINCT`
statement. Once this is done, SQLite uses the values in that column to evaluate the duplicates. With multiple columns, SQLite uses a combination of values to evaluate duplicate data.

- SQLite considers the `NULL` values as duplicates.
- This means we may not have enough info or have info that is not applicable at the moment.

## SQLite  SELECT DISTINCT examples

Suppose we use the `customers` table in our sample database.

Suppose we want to get information about the location of cities where customers reside. We can do this by using the `SELECT` statement to gather data from the `CITY` column of the `customers` table.
````sql
SELECT city 
FROM customers
ORDER BY city;
````
- Notice that this query returns 59 rows and we have some duplicates such as `Berlin`, `London`, and `Mountain View`. - We can remove the duplicates by using the `DISTINCT` clause as follows:

````sql
SELECT DISTINCT city
FROM customers
ORDER BY city;
````
Here we have removed 6 duplicate rows, returning 53 rows due to the `DISTINCT` clause.


## DISTINCT on multiple columns

Suppose we add the `country` column to our table of data. Then the following query:
````sql
SELECT 
    city, 
    country
FROM 
    customers
ORDER BY
    country;
````
which returns our table with a few duplicates with `Sao Paulo` being one of them. To remove these duplicates, we can easily just add the `DISTINCT` keyword to our query.

````sql
SELECT DISTINCT
    city,
    country
FROM 
    customers
ORDER BY
    country;
````

## SELECT DISTINCT with NULL

The following query returns a table of names of companies from the customers table.
````sql
SELECT company
FROM customers;
````
This returns 59 rows with a lot of `NULL` values. We can apply the `DISTINCT` clause to remove some of the `NULL` values. Notice that we only are only left with one `NULL` value in the table. This is because SQLite turns the multiple null values into one null value when we apply the `DISTINCT` clause.

- If we select a list of columns from a table and try to get a unique combination of some columns, we can use the `GROUP BY` clause to do this.


