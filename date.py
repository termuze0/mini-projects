from datetime import datetime

def convert_date(date_str, input_format, output_format):
    """
    Convert a date string from one format to another.

    :param date_str: The date string to convert.
    :param input_format: The current format of the date string.
    :param output_format: The desired format of the date string.
    :return: The converted date string.
    """
    try:
        # Parse the date string into a datetime object
        date_obj = datetime.strptime(date_str, input_format)
        # Convert it to the desired format
        converted_date = date_obj.strftime(output_format)
        return converted_date
    except ValueError as e:
        return f"Error: {e}"

# Example usage
input_date = "2025-01-16"
input_format = "%Y-%m-%d"  # Original format (YYYY-MM-DD)
output_format = "%d/%m/%Y"  # Desired format (DD/MM/YYYY)

converted_date = convert_date(input_date, input_format, output_format)
print("Converted Date:", converted_date)