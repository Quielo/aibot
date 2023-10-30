
def divide_text_into_chunks(filename, chunk_size=3000, start=0):
    chunks = []
    with open(filename, 'rb') as file:
        file.seek(start)
        chunk = file.read(chunk_size).decode('utf-8', errors='ignore')
        if chunk:
            chunks.append(chunk)
            next_start = start + len(chunk.encode('utf-8'))
            chunks += divide_text_into_chunks(filename, chunk_size, next_start)
    return chunks
