## Comma Separated Values (CSV)

- Structured data format stored as a plain text file
- Commonly used to exchange spreadhseets and database files

### CSV Structure

#### Header

    - The header is located on the first row in a CSV file
    - It containes information about the data (metadata)

#### Rows

    - The rows after the header are the data itself
    - Separated by a new line

#### Columns

    - Each column represents a field
    - Separated by delimeters

#### Delimiters

    - Delimeters can be any character for example a comma

### Reading CSV Files

    1. Import CSV module
    2. Open file object
    3. Open CSV reader object
    4. Iterate CSV reader object
    5. Close file object

### CSV Reader

- return a CSV reader object from file object
- Is also an iterator
- Return a row for every iteration
  - A row is a list of strings
  - Each string corresponds to a CSV column

```
import csv
csv.reader(csvfile)
```

### CSV Writer

- return a CSV writer object from file object

```
import csv
csv.writer(csvfile)
```

### Writerow Method

- write row to the writer's file object
- row is a contrainer
- All items in a row are converted to strings before writing

```
csv.writer.writerow(row)
```

### Writerows Method

- write all itemns in rows to the writer's file object
- rows is a container of containers

## JavaScript Object Notation (JSON)

- Widespread text format for exchanging internet data
- Human readable
- Easy machine parsing
- Allows storage of more complex data structures
- Scalar, list and dictionaries types are preserved
- Close to Python syntax

### Converting from JSON

- json module has methods to convert JSON source to Python object
- Conversion riles (JSON to Python)

| JSON               | Python               |
| ------------------ | -------------------- |
| lowercase Booleans | capitalized Booleans |

### JSON Read Methods
