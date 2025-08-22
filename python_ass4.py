def main():
    filename = input("Enter the filename to read: ")

    try:
        # Try opening the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content
        modified_content = content.upper()

        # Create a new output file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Successfully wrote modified content to '{new_filename}'")

    except FileNotFoundError:
        print("Error: The file was not found. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
