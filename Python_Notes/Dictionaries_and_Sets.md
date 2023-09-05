# Dictionaries

- Dictionaries are containers of unique key-value pairs
  - keys are unique and can be strings, numbers or tuples (immutable)
  - Values can be any type
- Dictionaries are not sequences but are iterable
- Dictionaries are used for mapping, counting, accumulating, categorizing

### Dictionary Literals

- Surrounded by curly braces `{ }`
- items are key-value pairs separated by a colon `;`
  `key: value`
- items are separated by a comma `,`
- An empty dictionary `{ }`

### Dictionary Function

`dict( )`

- return an empty dictionary

### Dictionary Operators

- Index
  `d[key]`
  - return a value associuated with key
  - if the key does not exist, a KeyError exception is thrown
- Assignment
  d[key] = value
  - if key exists, update key's value to value
  - if key does not exist, add a new key-value item
- Membership
  `key in d`
  - return Boolena on weather key exists as a key in d
- Delete
  `del d[key]`
  - delete item with key
  - KeyError if not found

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

` set1 == set2`

- equality operator

`set1 != set2`

- inequlity operator

`item in set2`

- membership operator

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
