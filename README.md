# ChainedHashTable

## Overview
The `ChainedHashTable` is a hash table implementation that uses chaining to handle collisions. Each bin in the hash table holds a list of key-value pairs. This implementation allows for efficient storage and retrieval of items using their keys.

## Features
- **Dynamic Resizing**: The hash table automatically resizes to maintain efficient operations as the number of elements changes.
- **Customizable List Type**: You can specify the type of list used for chaining, with `DLList` as the default.
- **Basic Operations**: Supports adding, finding, removing, and updating key-value pairs.

## Installation
1. **Clone the Repository**:
   - First, clone this GitHub repository to your local machine. Open your terminal and run:
     ```bash
     git clone https://github.com/NefariousNeo/ChainedHashTable-Project
     ```

2. **Navigate to the Project Directory**:
   - Go to the project directory:
     ```bash
     cd ChainedHashTable-Project
     ```

3. **Install Dependencies**:
   - Ensure you have `numpy` installed. You can install it using pip:
     ```bash
     pip install numpy
     ```

4. **Run the Project**:
   - You can now run this project and use the `ChainedHashTable` class as demonstrated in the usage example below.

## Usage
Note that a tester.py file is already included with several tests

Here is an example of how to use this class if you decide to create another file:

```
from ChainedHashTable import ChainedHashTable
from DLList import DLList

# Create a ChainedHashTable instance
cht = ChainedHashTable(listType=DLList)

# Add key-value pairs
cht.add("key1", "value1")
cht.add("key2", "value2")

# Find a value by key
print(cht.find("key1"))  # Output: value1

# Remove a key-value pair
print(cht.remove("key2"))  # Output: value2

# Update a value
cht.set("key1", "new_value1")
print(cht.find("key1"))  # Output: new_value1

# Get all keys
print(cht.get_keys())  # Output: ['key1']

# Print the hash table
print(cht)
```

## Methods

### `__init__(self, listType=DLList)`
Initializes an empty hash table with the specified list type.

- **Parameters**:
  - `listType`: The type of list used for chaining. Defaults to `DLList`.

### `_alloc_table(self, n: int)`
Creates a table with a given number of bins and list type.

- **Parameters**:
  - `n`: The number of bins in the table.

### `_hash(self, key: object) -> int`
Computes the hash value for the given key.

- **Parameters**:
  - `key`: The key to compute the hash value for.

- **Returns**:
  - `int`: The hash value (bin number) for the given key.

### `find(self, key: object) -> object`
Finds the value corresponding to the given key.

- **Parameters**:
  - `key`: The key of the item to search for.

- **Returns**:
  - `object`: The value corresponding to the key, if the key exists. Otherwise, returns `None`.

### `add(self, key: object, value: object)`
Adds a key-value pair to the table.

- **Parameters**:
  - `key`: The key of the item to add.
  - `value`: The value of the item to add.

- **Returns**:
  - `bool`: `True` if the value was successfully added; `False` if the key already exists and the new item was not added.

### `remove(self, key: int) -> object`
Removes the item with the given key and returns its value.

- **Parameters**:
  - `key`: The key of the item to remove.

- **Returns**:
  - `object`: The value of the removed item, if the key exists. Otherwise, returns `None`.

### `resize(self)`
Resizes the table to maintain efficient operations.

### `size(self) -> int`
Returns the number of items in the table.

- **Returns**:
  - `int`: The number of items in the table.

### `set(self, key, new_value)`
Replaces the value of the given key.

- **Parameters**:
  - `key`: The key of the item to modify.
  - `new_value`: The new value to set for the item.

- **Returns**:
  - `object`: The old value corresponding to the key that was replaced.

- **Raises**:
  - `ValueError`: If the given key does not exist in the table.

### `get_keys(self)`
Returns a list of all keys stored in the table.

- **Returns**:
  - `list`: A list of all keys stored in the table.

### `__str__(self)`
Returns a string representation of the table.

- **Returns**:
  - `str`: A string representation of the table with key-value items in the format `(key, value)`.

