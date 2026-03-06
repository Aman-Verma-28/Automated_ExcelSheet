"""Automated Excel Sheet Data Extractor.

Reads cell values from a specified Excel spreadsheet and prints them to the console.
Supports command-line arguments for flexible configuration.
"""

import argparse
import sys

import openpyxl


def parse_arguments():
    """Parse command-line arguments for Excel data extraction."""
    parser = argparse.ArgumentParser(
        description="Extract and display data from an Excel spreadsheet."
    )
    parser.add_argument(
        "file_path",
        help="Path to the Excel file (e.g., /path/to/Mysheet.xlsx)",
    )
    parser.add_argument(
        "--sheet",
        default=None,
        help="Name of the worksheet to read (defaults to the active sheet)",
    )
    parser.add_argument(
        "--row",
        type=int,
        default=1,
        help="Row number to read from (default: 1)",
    )
    parser.add_argument(
        "--col",
        type=int,
        default=10,
        help="Number of columns to read (default: 10)",
    )
    return parser.parse_args()


def extract_data(file_path, sheet_name=None, row=1, col=10):
    """Extract cell values from the specified Excel file.

    Args:
        file_path: Path to the Excel workbook.
        sheet_name: Name of the worksheet. Uses the active sheet if None.
        row: Row number to read from.
        col: Number of columns to read (1 through col).

    Returns:
        A list of non-None cell values.

    Raises:
        FileNotFoundError: If the Excel file does not exist.
        KeyError: If the specified sheet name is not found in the workbook.
        ValueError: If row or col values are less than 1.
    """
    if row < 1:
        raise ValueError(f"Row must be at least 1, got {row}")
    if col < 1:
        raise ValueError(f"Column count must be at least 1, got {col}")

    try:
        workbook = openpyxl.load_workbook(file_path, read_only=True)
    except FileNotFoundError:
        raise FileNotFoundError(f"Excel file not found: {file_path}")

    try:
        if sheet_name is not None:
            if sheet_name not in workbook.sheetnames:
                raise KeyError(
                    f"Sheet '{sheet_name}' not found. "
                    f"Available sheets: {workbook.sheetnames}"
                )
            sheet = workbook[sheet_name]
        else:
            sheet = workbook.active

        values = []
        for i in range(1, col + 1):
            data_in_cell = sheet.cell(row=row, column=i).value
            if data_in_cell is not None:
                values.append(data_in_cell)

        return values
    finally:
        workbook.close()


def main():
    """Main entry point for the Excel data extractor."""
    args = parse_arguments()

    try:
        values = extract_data(args.file_path, args.sheet, args.row, args.col)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    for value in values:
        print(value)


if __name__ == "__main__":
    main()
