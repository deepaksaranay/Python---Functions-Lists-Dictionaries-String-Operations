Task 1: Read a File and Handle Errors

def read_file():
    file_name = "sample.txt"
    try:
        with open(file_name, "r") as file:
            print("Reading file content:")
            for index, line in enumerate(file, start=1):
                print(f"Line {index}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")


if __name__ == "__main__":
    read_file()


Task 2: Write and Append Data to a File

def write_and_append_file():
    file_name = "output.txt"

    try:
        user_input = input("Enter text to write to the file: ")
        with open(file_name, "w") as file:
            file.write(user_input + "\n")
        print("Data successfully written to output.txt.")

        additional_input = input("Enter additional text to append: ")
        with open(file_name, "a") as file:
            file.write(additional_input + "\n")
        print("Data successfully appended.")

        print("\nFinal content of output.txt:")
        with open(file_name, "r") as file:
            print(file.read())

    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    write_and_append_file()

