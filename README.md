# Microsoft 365 Unified Audit Logs (UAL) Log Parser

This Python script efficiently parses and expands Microsoft 365 Unified Audit Log (UAL) entries from Excel files. It reads an Excel file containing raw UAL data, focusing on the `AuditData` column, which consists of JSON-formatted strings. The script parses these JSON strings, normalizes the JSON structure into separate columns, and combines these with the original dataset. The final, expanded dataset is saved into a new Excel file, providing a clearer, more accessible format for further analysis or auditing purposes.

## Features

- **JSON Parsing**: Converts JSON strings in the `AuditData` column into Python dictionaries.
- **Data Expansion**: Normalizes and expands JSON objects into separate columns for easy analysis.
- **Excel Integration**: Inputs and outputs data via Excel files, making it compatible with common business tools.

## Prerequisites

- Python 3.x
- pandas library
- openpyxl library (for handling .xlsx files)

## Usage

Ensure you have the necessary Python environment and dependencies installed. Run the script from the command line as follows:

```python UAL_Parser.py <input_file_path> <output_file_path>```

- `<input_file_path>`: The path to the input Excel file containing the UAL data.
- `<output_file_path>`: The path where the output Excel file should be saved.

## Example

```python UAL_Parser.py 'input_data.xlsx' 'output_data.xlsx'```

This script simplifies the task of handling Microsoft 365 audit logs by automating the parsing and expansion of complex JSON data, making it an essential tool for system administrators or digital investigations.
