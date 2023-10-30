import os

def prompt_chunks():
    relative_path = 'Work/projects/python/prod/aibot/app/prompts'
    folder_path = os.path.expanduser(f'~/{relative_path}')
    filename = os.path.join(folder_path, 'prompt.txt')  # Replace 'your_input_file.txt' with the actual filename

    try:
        with open(filename, 'r') as file:
            file_content = file.read()
        formatted_text = ' '.join(file_content.splitlines())
        prompt = formatted_text
        return prompt
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None



