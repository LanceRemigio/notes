# Simple uses of the SELECT statement
We can do simple calculations such as the following:
````sql
SELECT 1 + 1; /* returns 2 */
````
We can mutiple expressions in our select statement

````sql
SELECT 
   10 / 5, 
   2 * 4;
````

The `SELECT` statement is often used to query data from more than one table. The syntax of this statement is as follows:
````sql
SELECT DISTINCT column_list
FROM table_list
    JOIN table ON join_condition
WHERE row_filter
ORDER BY column
LIMIT count OFFSET offset
GROUP BY column
HAVING group_filter;
````
Here we jot down what each statement does in this query:
- `ORDER BY clause` -> sorts the result of a set.
- `DISTINCT` -> query unique rows in a table
- `WHERE` -> filters rows in the result set
- `LIMIT OFFSET` -> limits the amount of rows returned 
- `INNER JOIN` or `LEFT JOIN` -> queries data from multiple tables using join.
- `GROUP BY` -> puts the group rows into groups and apply an aggregate function for each group.
- `HAVING` -> filters groups

We will focus on the simplest `SELECT` statement which allows you to query data from a single table.
````sql
SELECT column_list FROM table;
````
SQlite evaluates the `FROM` clause first, then the `SELECT` clause. To write this simple query, we first need to choose the table we want to grab our data from; do this in the `FROM` clause. Secondly, choose the column you want to pull the data from and put this in the `SELECT` statement. Don't forget to add the semicolon `;`.

# Using SELECT on our example database

We can gather data from our `tracks` table by specifying the columns we need.

````sql
SELECT /* specifying the columns from the table */ 
    trackid, 
    name, 
    composer,
    unitprice
FROM 
    tracks; /* choosing the table */
````
To get data from all the columns in the `tracks` table, wecan put the `*` command.

````sql
SELECT * FROM tracks;
````
However, if you are going to develop an application then it is best not to use the `*` command since it might return the wrong information when working with other people who are constantly changing adding columns to tables.




