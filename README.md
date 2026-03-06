# Automated Excel Sheet

A Python utility for extracting data from Excel spreadsheets via the command line.

---

## Setup

```bash
pip install -r requirements.txt
```

Or install the dependency directly:

```bash
pip install openpyxl
```

## Usage

```bash
python main.py <path-to-excel-file> [options]
```

### Arguments

| Argument    | Required | Default      | Description                                    |
|-------------|----------|--------------|------------------------------------------------|
| `file_path` | Yes      | -            | Path to the Excel file                         |
| `--sheet`   | No       | Active sheet | Name of the worksheet to read                  |
| `--row`     | No       | `1`          | Row number to read from                        |
| `--col`     | No       | `10`         | Number of columns to read (1 through col)      |

### Examples

Read the first row (columns 1-10) from the active sheet:

```bash
python main.py /path/to/Mysheet.xlsx
```

Read from a specific sheet and row:

```bash
python main.py /path/to/Mysheet.xlsx --sheet "Sheet4" --row 2 --col 5
```

### Important

- **Close the Excel file** before running the script to avoid file-locking errors.

## Using as a Library

You can also import the `extract_data` function directly:

```python
from main import extract_data

values = extract_data("data.xlsx", sheet_name="Sheet1", row=1, col=5)
for v in values:
    print(v)
```

---

Any clarification: [click here](https://www.linkedin.com/in/aman-verma-906650190/)
