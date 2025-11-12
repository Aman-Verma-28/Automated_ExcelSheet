# Automated Excel Sheet Reader

A Python-based automation tool for reading and processing data from Excel spreadsheets using the openpyxl library. This lightweight utility simplifies the process of extracting data from Excel files programmatically.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Basic Setup](#basic-setup)
  - [Configuration](#configuration)
  - [Running the Script](#running-the-script)
- [Code Structure](#code-structure)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Best Practices](#best-practices)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

Automated_ExcelSheet is a simple yet powerful Python script designed to automate the process of reading data from Excel files. It leverages the openpyxl library to access workbooks, navigate through sheets, and extract cell data efficiently. This tool is ideal for data processing tasks, report generation, data migration, and any scenario where you need to programmatically access Excel data.

## Features

- **Easy Excel File Access**: Load and read Excel workbooks (.xlsx format) with minimal code
- **Multi-Sheet Support**: Work with specific sheets within workbooks containing multiple sheets
- **Flexible Data Extraction**: Configure row and column ranges to extract exactly the data you need
- **Null Value Handling**: Automatically filters out empty cells during data extraction
- **Simple Configuration**: Easy-to-modify parameters for customizing data extraction
- **Console Output**: Prints extracted data directly to the console for immediate viewing
- **Extensible Design**: Base code that can be easily extended for custom data processing needs

## Prerequisites

Before using this tool, ensure you have the following:

- **Python 3.x**: Python 3.6 or higher is recommended
- **pip**: Python package installer (usually comes with Python)
- **Excel File**: An .xlsx format Excel file to work with
- **Basic Python Knowledge**: Understanding of Python basics is helpful for customization

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/Aman-Verma-28/Automated_ExcelSheet.git
cd Automated_ExcelSheet
```

### Step 2: Install Required Dependencies

Install the openpyxl library using pip:

```bash
pip install openpyxl
```

Alternatively, if you're using a virtual environment (recommended):

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install openpyxl
pip install openpyxl
```

## Usage

### Basic Setup

1. **Prepare Your Excel File**: Ensure your Excel file (.xlsx format) is accessible and note its full path
2. **Close the Excel File**: Important - Make sure the Excel file is closed before running the script to avoid file access conflicts
3. **Identify Your Target Sheet**: Know the name of the sheet you want to read from (e.g., 'Sheet1', 'Sheet4', etc.)

### Configuration

Open `main.py` and modify the following parameters according to your needs:

#### 1. Set the Excel File Path

```python
wb = openpyxl.load_workbook("C:/Users/verma/OneDrive/Desktop/Mysheet.xlsx")
```

Replace the path with your Excel file's location. Examples:
- Windows: `"C:/Users/YourName/Documents/data.xlsx"`
- macOS/Linux: `"/home/username/documents/data.xlsx"`
- Relative path: `"./data/myfile.xlsx"`

#### 2. Specify the Sheet Name

```python
sh1 = wb['Sheet4']
```

Replace `'Sheet4'` with the name of your target sheet (e.g., `'Sheet1'`, `'Data'`, `'Report'`, etc.)

#### 3. Configure Row and Column Range

```python
row = 1  # Starting row number
col = 10  # Number of columns to read
```

- `row`: The row number from which to start reading (1-indexed)
- `col`: The number of columns to read from that row

**Note**: The current implementation reads data vertically (down columns) starting from the specified row. The loop iterates through rows 1 to `col+1` and reads from column `row`.

### Running the Script

Execute the script using Python:

```bash
python main.py
```

The script will:
1. Open the specified Excel workbook
2. Access the designated sheet
3. Extract data from the configured range
4. Print non-empty cell values to the console

## Code Structure

The main script (`main.py`) follows this structure:

```python
import openpyxl

# Load the workbook
wb = openpyxl.load_workbook("path/to/your/file.xlsx")

# Select the sheet
sh1 = wb['SheetName']

# Configure reading parameters
row = 1   # Row to read from
col = 10  # Number of columns to process

# Extract and process data
for i in range(1, col+1):
    dataInCell = sh1.cell(i, row).value
    if dataInCell != None:
        print(dataInCell)
    # Add your custom processing logic here
```

### Key Components

- **openpyxl.load_workbook()**: Opens the Excel file and returns a workbook object
- **wb['SheetName']**: Accesses a specific sheet within the workbook
- **sh1.cell(row, col).value**: Retrieves the value from a specific cell
- **Null check**: Filters out empty cells before processing

## Examples

### Example 1: Reading a Column of Data

To read the first 10 rows of column A:

```python
wb = openpyxl.load_workbook("data.xlsx")
sh1 = wb['Sheet1']

row = 1  # Column A
col = 10  # First 10 rows

for i in range(1, col+1):
    dataInCell = sh1.cell(i, row).value
    if dataInCell != None:
        print(dataInCell)
```

### Example 2: Processing Data into a List

Modify the script to store data in a list:

```python
data_list = []

for i in range(1, col+1):
    dataInCell = sh1.cell(i, row).value
    if dataInCell != None:
        data_list.append(dataInCell)

print(f"Extracted {len(data_list)} items: {data_list}")
```

### Example 3: Reading Multiple Columns

To read data from multiple columns:

```python
start_row = 1
end_row = 10
columns_to_read = [1, 2, 3]  # Columns A, B, C

for col in columns_to_read:
    print(f"\nColumn {col}:")
    for row in range(start_row, end_row + 1):
        dataInCell = sh1.cell(row, col).value
        if dataInCell != None:
            print(f"  Row {row}: {dataInCell}")
```

### Example 4: Writing Data to Another File

Process and save data to a text file:

```python
with open('output.txt', 'w') as f:
    for i in range(1, col+1):
        dataInCell = sh1.cell(i, row).value
        if dataInCell != None:
            f.write(f"{dataInCell}\n")
```

## Troubleshooting

### Common Issues and Solutions

#### Issue: "FileNotFoundError: [Errno 2] No such file or directory"

**Solution**: 
- Verify the file path is correct
- Use absolute paths or ensure relative paths are correct
- Check that the file exists at the specified location
- On Windows, use forward slashes (/) or escaped backslashes (\\\\)

#### Issue: "PermissionError: [Errno 13] Permission denied"

**Solution**:
- Close the Excel file before running the script
- Ensure you have read permissions for the file
- Check if another program is using the file

#### Issue: "KeyError: 'Worksheet SheetName does not exist.'"

**Solution**:
- Verify the sheet name is spelled correctly (case-sensitive)
- Check the exact sheet name in your Excel file
- List all sheets: `print(wb.sheetnames)`

#### Issue: "ModuleNotFoundError: No module named 'openpyxl'"

**Solution**:
- Install openpyxl: `pip install openpyxl`
- If using a virtual environment, ensure it's activated
- Try: `python -m pip install openpyxl`

#### Issue: No data is printed

**Solution**:
- Verify the row and column parameters are correct
- Check if the cells contain data
- Ensure you're reading from the correct sheet
- Print cell values without the null check to see what's there

## Best Practices

1. **Always Close Excel Files**: Before running the script, close any Excel files you're accessing to prevent file locking issues

2. **Use Absolute Paths**: When possible, use absolute file paths to avoid confusion about file locations

3. **Backup Your Data**: Always work with copies of important Excel files

4. **Error Handling**: Consider adding try-except blocks for production use:
   ```python
   try:
       wb = openpyxl.load_workbook("file.xlsx")
   except FileNotFoundError:
       print("Error: File not found. Please check the path.")
   except Exception as e:
       print(f"An error occurred: {e}")
   ```

5. **Virtual Environments**: Use virtual environments to manage dependencies and avoid conflicts

6. **Data Validation**: Validate extracted data before processing to ensure data integrity

7. **Memory Management**: For large Excel files, consider processing data in chunks or using read-only mode:
   ```python
   wb = openpyxl.load_workbook("large_file.xlsx", read_only=True)
   ```

8. **Documentation**: Comment your code when modifying the script for specific use cases

## Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

Please ensure your code follows Python best practices and includes appropriate comments.

## License

This project is open source and available for educational and commercial use. Please check the repository for specific license information.

## Contact

For questions, clarifications, or support:

**Aman Verma**
- LinkedIn: [Aman Verma](https://www.linkedin.com/in/aman-verma-906650190/)
- GitHub: [@Aman-Verma-28](https://github.com/Aman-Verma-28)

Feel free to reach out for:
- Technical support
- Feature requests
- Bug reports
- Collaboration opportunities
- General questions about the project

---

**Note**: This tool is designed for .xlsx files (Excel 2007 and later). For older .xls files, consider using the xlrd library instead.

**Happy Automating!**
