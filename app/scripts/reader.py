
def divide_text_into_chunks(filename, chunk_size=300, start=0):
    chunks = []
    with open(filename, 'rb') as file:
        file.seek(start)
        chunk = file.read(chunk_size).decode('utf-8', errors='ignore')
        if chunk:
            chunks.append(chunk)
            next_start = start + len(chunk.encode('utf-8'))
            chunks += divide_text_into_chunks(filename, chunk_size, next_start)
    return chunks

# def main():
#     filename = 'your_large_text_file.txt'
#     chunks = divide_text_into_chunks(filename)

#     for i, chunk in enumerate(chunks):
#         print(f"Chunk {i + 1}:\n{chunk}\n")

if __name__ == '__main__':
    main()
