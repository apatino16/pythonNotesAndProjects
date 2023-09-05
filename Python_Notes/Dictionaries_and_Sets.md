# Dictionaries

## Dictionary Methods

## Dictionary Iteration

## Default Dictionaries and Counter

## Nested Containers

# Sets

- Sets are containers of unique items
- Sets can only contain immutable items:
  - numbers
  - strings
  - tuples

### Set Properties

- Mutable, but follow a set condition
  - adding items that already exist will be rejected
- Sets are not sequences
  - items are unordered
  - no index operators
- Sets are iterable

## Set Literals

- Surrounded by curly braces `{ }`
- items are separated by a comma `,`
- An empty set is represented by a set function `set()`

## Set Functions

` set(container)`

- return a set with only unique items from the container

## Set Operators

- equality operator

` set1 == set2`

- inequlity operator

`set1 != set2`

- membership operator

`item in set2`

## Set Methods

`set.add(item)`

- add item to set only if the item does not already exist

`set.remove(item)`

- remove item from set
- if thhe item does not exist, throw KeyError exception

`set.clear()`

- remove all items in set

## Set Comprehension

`myset = { exp for item in iterable if con_exp}`
