# The WHERE clause

The `WHERE` clause filters the rows of a table of data based on some condition.

Here is the following syntax:
````sql
SELECT
    column_list
FROM 
    table
WHERE
    search_condition;
````
SQLite filters the rows based on the following process:
- Check the table in the `FROM` clause.
- Evaluate the conditions specified after the `WHERE` clause.
- Return the result set using the rows that meed the conditions in the above step with the columns in the `SELECT` clause.

The search condition for the `WHERE` clause contains the following syntax:
````sql
left_expression COMPARISON_OPERATOR right_expression
````

Some examples of search conditions are:

- `WHERE column_1 = 100;`
- `WHERE column_2 IN (1,2,3);`
-  `WHERE column_3 LIKE 'An%;'`
- `WHERE column_4 BETWEEN 10 AND 20;`

We can use the `WHERE` clause in the `UPDATE` and `DELETE` statements.

## SQLite comparison operators

A comparison operator tests if two expressions are the same. The following illustrates the comparison operators that we can use to construct expressions:
- = -> Equal to 
- < > or ! -> Not equal to 
-  < -> less than
- > -> greater than
- <= -> less than or equal to 
- >= -> greater than or equal to 










