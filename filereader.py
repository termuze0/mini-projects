class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_all(self):
        try:
            with open(self.file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "File not found. Please check the file path."
        except Exception as e:
            return f"An error occurred: {e}"

    def read_lines(self):
        try:
            with open(self.file_path, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            return "File not found. Please check the file path."
        except Exception as e:
            return f"An error occurred: {e}"

    def read_line_by_line(self):
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("File not found. Please check the file path.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    file_path = "example.txt"
    reader = FileReader(file_path)
    
    print("Reading entire content:")
    print(reader.read_all())
    
    print("\nReading content as lines:")
    print(reader.read_lines())
    
    print("\nReading line by line:")
    reader.read_line_by_line()