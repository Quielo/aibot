from scripts.reader import divide_text_into_chunks
import os

def output_chunks():
    chunk_list = []  # Create a list to store the chunks

    relative_path = 'Work/projects/python/prod/aibot/app/source_docs'
    folder_path = os.path.expanduser(f'~/{relative_path}')

    file_list = []

    for file in os.listdir(folder_path):
        if file.endswith('.txt'):
            file_path = os.path.join(folder_path, file)
            file_list.append(file_path)
            
    for filename in file_list:
        chunks = divide_text_into_chunks(filename)
        for i, chunk in enumerate(chunks):
            chunk_output = f"Chunk {i + 1}:   {chunk}   "
            print(chunk_output)
            chunk_list.append(chunk_output)  # Append the chunk to the list

    return chunk_list  # Return the list of chunk_output strings
