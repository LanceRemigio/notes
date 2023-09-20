# Sorting rows

We can sort a result set of a query in SQLite by using the `ORDER BY` clause.

## Intro

The order in which SQLite stores its data may be unspecified. This becomes apparent when we use the `SELECT` statement to query the data from a specific table. We can fix this issue by adding the `ORDER BY` statement when we're selecting our data. The syntax is as follows:
````sql
SELECT 
    select_list /* the columns we want */
FROM 
    table 
ORDER BY
    column_1 ASC /* ascending order (from least to greatest) */,
    column_2 DESC /* descending order (from greatest to least) */;
````
If we don't specify in which order we want the data columns are sorted by, then SQLite defaults to ascending order. The `ORDER BY` statement sorts rows using the first column specified. Then, it continues this same process until the nth statement is reached.

## ORDER BY example

Using our sample database, let us select the following columns included in the code below:

````sql
SELECT 
    name, 
    milliseconds,
    albumid
FROM 
    tracks;
````
However, this does not use the `ORDER BY` clause so the resulting columns are not organized in any type of order. We can go ahead and add the clause so that we may have ordered columns.

````sql
SELECT 
    name, 
    milliseconds,
    albumid
FROM 
    tracks
ORDER BY 
    albumid ASC;

````

Suppose we also want to sort by the milliseconds column but in a descending order instead of the default ascending order. Then we have the following query:
````sql
SELECT 
    name, 
    milliseconds,
    albumid
FROM 
    tracks
ORDER BY 
    albumid ASC;
    milliseconds DESC;
````
This data selects the three columns specified above and then sorts them by album id in an ascending order and then sorts the columns via the milliseconds column by descending order.

## Using ORDER BY by specifying the column position

Instead of using the names of the columns to sort the data, we can sort by the number assigned to each column in a table. 
````sql
SELECT 
    name, 
    milliseconds,
    albumid
FROM 
    tracks
ORDER BY
    3,2; /* where 3 is assigned to album id and 2 is assigned to milliseconds */
````

# Sorting NULLS

- Sometimes you have information missing or have data that is not applicable.
- This means you won't have, say, birthday information if it does not exist in a table yet. 
- `NULL` was created to resolve this issue of not having the information. It is basically just a placeholder until the information is inputted by somebody else.
- `NULL` cannot be compared to any value
- We cannot compare `NULL` with itself; that is, we have `NULL = NULL` will always be false.
- SQlite considers `NULL` to be the absolute min when compared to other values.
- It will always appear at the beginning of any result when it is sort in ascending order (NULL FIRST) and at the end  if it is sorted (NULL LAST) in the descending order.

An example is the following query:

````sql
SELECT 
    TrackId,
    Name,
    Composer
FROM
    tracks
ORDER BY
    Composer NULLS LAST;
````

# Summary

- We can sort columns of a given data table by using `ORDER BY` clause.
- We can choose to organize based on one column or multiple columns either by ascending and descending orders.
