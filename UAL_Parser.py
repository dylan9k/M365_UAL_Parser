import pandas as pd
import json
import sys

def parse_json(data):
    """Parses JSON data from a given column."""
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        return {}

def main(input_file, output_file):
    try:
        # Load the Excel file
        data = pd.read_excel(input_file)
        
        # Apply the parsing function to the AuditData column
        data['ParsedAuditData'] = data['AuditData'].apply(parse_json)
        
        # Expand the JSON fields into separate columns
        audit_data_expanded = pd.json_normalize(data['ParsedAuditData'])
        
        # Combine the expanded audit data with the original data
        final_data = pd.concat([data.drop(columns=['AuditData', 'ParsedAuditData']), audit_data_expanded], axis=1)
        
        # Save the expanded dataset to a new Excel file
        final_data.to_excel(output_file, index=False)
        
        print(f"Data has been successfully parsed and saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python UAL_Parser.py <input_file_path> <output_file_path>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        main(input_file, output_file)
