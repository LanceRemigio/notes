# Lecure 2

In this lecture we will be covering:

- Dictionaries
- Tuples
- Sets

## Dictionaries

Each value within a dictionary is assigned to a unique key.

````python
d = {'key1': 'value', 'key2': 123}
````
We can grab the value wihin a dictionary by specifying the key in the dictionary. For example, we have
````python
print(d['key1']).
````
If we have a dictionary with a list within it, then we could also grab an element from that list.
This is demonstrated by the following code:
````python
d = {'k1': [1,2,3]}
my_list = d['k1']
print(my_list[0]) # prints out the first element of list within list
````
or 
````python
print(d['k1'][0]) # prints out the same element in the list but in one line
````
We can have nested dictionaries:
````python
d = {'k1': {'innerkey': [1,2,3]}}
print(d['k1']['innerkey'][1])
````
Dictionaries are not arranged in a sequential order like lists. Values are assigned to (key, value) pair mappings.

## Difference between Tuples and Lists

Tuples and lists are similar in that they have a sequence-like structure. We can grab elements from either a list or a tuple by specifying the index where the element is stored. The key difference is that you cannot reassign elements within a tuple; they are immutable!

## Sets
This is just a collection of elements that are unique. We can add the same element to the same set , but if we try to print it it will not repeat the same element twice.



