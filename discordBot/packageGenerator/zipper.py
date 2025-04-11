import os
import zipfile
from typing import List, Union

def create_zip_archive(files: List[str], output_filename: str) -> None:
    """
    Creates a ZIP archive containing multiple files.
    
    Args:
        files: List of file paths to include in the ZIP
        output_filename: Desired name for the ZIP file (must end with .zip)
        
    Raises:
        FileNotFoundError: If any specified file does not exist
        ValueError: If output filename is invalid
    """
    if not output_filename.endswith('.zip'):
        output_filename = f"{output_filename}.zip"
    
    # Verify all files exist
    for file_path in files:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        # Create ZIP archive
        with zipfile.ZipFile(output_filename, 'w', compression=zipfile.ZIP_DEFLATED) as zip_file:
            # Add each file to the archive
            for file_path in files:
                # Get just the filename for the archive
                filename = os.path.basename(file_path)
                zip_file.write(file_path, filename)
        
        print(f"Successfully created ZIP archive: {output_filename}")
    
    except Exception as e:
        raise RuntimeError(f"Error creating ZIP archive: {str(e)}")

# Example usage

def unzip_file(zip_path: str, extract_dir: str = None) -> None:
    """
    Unzip a file to a specified directory with detailed feedback.
    
    Args:
        zip_path: Path to the ZIP file
        extract_dir: Directory to extract to (defaults to current directory if None)
        
    Raises:
        FileNotFoundError: If the ZIP file doesn't exist
        NotADirectoryError: If the extraction directory doesn't exist
        zipfile.BadZipFile: If the file is not a valid ZIP archive
    """
    # Validate input file exists
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"ZIP file not found: {zip_path}")
    
    # Use current directory if none specified
    if extract_dir is None:
        extract_dir = os.path.dirname(zip_path)
    # Create directory if it doesn't exist
    elif not os.path.exists(extract_dir):
        os.makedirs(extract_dir)
        print(f"Created extraction directory: {extract_dir}")
    
    try:
        # Open and show ZIP file contents
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            print(f"\nZIP file contents:")
            for file in zip_ref.namelist():
                print(f"- {file}")
            
            # Extract files with progress
            print(f"\nExtracting to: {extract_dir}")
            for file in zip_ref.namelist():
                zip_ref.extract(file, extract_dir)
                print(f"Extracted: {file}")
            
            print("\nExtraction complete!")
            
    except zipfile.BadZipFile:
        raise zipfile.BadZipFile(f"Invalid ZIP file: {zip_path}")
    except Exception as e:
        raise Exception(f"Error during extraction: {str(e)}")

# Example usage
def main():
    try:
        # Example with default extraction directory
        print("Example 1: Using default directory")
        unzip_file("discordBot\\packageGenerator\\package.zip")
        
        # Example with custom extraction directory
        print("\nExample 2: Using custom directory")
        unzip_file("discordBot\\packageGenerator\\package.zip", "extracted_files")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()