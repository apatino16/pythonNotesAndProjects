# Python Basics

## Data: Types, Values, Variables, and Names

### Objects

In Python, an object is a chunk of data that contains at least the following: - A type that defines what it can do - A unique id to distinguish it from other objects - A value consistent with its type - A reference count that tracks how often this object is used

### Types

#### Python's basic data types

| Name           | Types     | Mutable? | Examples                                                | Notes Reference |
| -------------- | --------- | -------- | ------------------------------------------------------- | --------------- |
| Boolean        | bool      | no       | True, False                                             |                 |
| Integer        | int       | int      | 47, 2500, 25_000                                        |                 |
| Floating Point | float     | no       | 3.14, 2.7e5                                             |                 |
| Complex        | complex   | no       | 3j, 5 + 9j                                              |                 |
| Text String    | str       | no       | "hello", 'helo', "'Hello'"                              |                 |
| List           | list      | yes      | ["Carrots", "Onions", "Lettuce"]                        |                 |
| Tuple          | tuple     | no       | (2, 3, 4)                                               |                 |
| Bytes          | bytes     | no       | b'ab\xff'                                               |                 |
| ByteArray      | bytearray | yes      | bytearray(...)                                          |                 |
| Set            | set       | yes      | set([1,2,3])                                            |                 |
| Frozen Set     | frozenset | no       | frozenset(["Anthony", "Laura"])                         |                 |
| Dictionary     | dict      | yes      | {'game': 'bingo' , 'dog': 'dingo' , 'drummer': 'Ringo'} |                 |

#### Mutability

The type determines whether the data value contained by the box can be changed (mutable) or is constant (immutable).

Python is strongly typed whicch means that the type of the object does not change, even if it's value is mutlable.

## Values

There are two ways oif specifying data values in Python: - Literal - Variables

### Variables

## Numbers

### Arithmetic Operations

Python supports different types of arithmetic operations that can be performed on literal numbers, variables, or some combination. The primary arithmetic operators are:

`+` for addition

`-` for subtraction

`*` for multiplication

`/` for division

`%` for modulus (returns the remainder)

`**` for exponentiation

### Comments

A comment is a piece of text within a program that is not executed. It can be used to provide additional information to aid in understanding the code.

The `#` character is used to start a comment and it continues until the end of the line.

```
# Comment on a single line
```
