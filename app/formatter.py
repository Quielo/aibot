import os
import string

def format_text_file(file_path):

    relative_path = 'Work/projects/python/prod/aibot/app/source_docs'
    folder_path = os.path.expanduser(f'~/{relative_path}')

    file_list = []

    for file in os.listdir(folder_path):
        if file.endswith('.txt'):
            file_path = os.path.join(folder_path, file)
            file_list.append(file_path)
            
    for filename in file_list:
        try:
            # Open the file for reading
            with open(filename, 'r') as file:
                text = file.read()

            # Remove non-printable characters
            printable_text = ''.join(filter(lambda x: x in string.printable, text))

            # Open the file for writing and save the updated text
            with open(filename, 'w') as file:
                file.write(printable_text)

            print(f'File "{filename}" has been formatted and saved.')

        except FileNotFoundError:
            print(f'File "{filename}" not found.')

if __name__ == "__main__":
    filename = "~/source_docs/chunky.txt"  # Replace with your file's path
    format_text_file(filename)
