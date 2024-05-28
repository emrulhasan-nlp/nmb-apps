import re

def clean_text(text):
    """Cleans the text by removing extra spaces and empty lines."""
    # Remove leading and trailing spaces from each line
    lines = [line.strip() for line in text.splitlines()]
    
    # Replace multiple spaces within lines with a single space
    lines = [re.sub(r'\s+', ' ', line) for line in lines]
    
    # Remove empty lines
    cleaned_lines = [line for line in lines if line]
    
    # Join the cleaned lines back into a single string
    cleaned_text = "\n".join(cleaned_lines)
    
    return cleaned_text

def read_and_print_cleaned_file(file_path):
    """Reads text from a file, cleans it, and prints the cleaned text."""
    try:
        with open(file_path, 'rb') as file:
            # Read the byte content and decode it to a string
            content = file.read().decode('utf-8')
        
        cleaned_content = clean_text(content)
        return cleaned_content
        
        print(cleaned_content)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

