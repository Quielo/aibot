from reader import divide_text_into_chunks
import os

# def main():
def output_chunks():
    
    # chunk_list = []

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
            # chunk_list.append(chunk)
            chunk_output = print(f"Chunk {i + 1}:\n{chunk}\n")
            return chunk_output

# if __name__ == '__main__':
#     main()