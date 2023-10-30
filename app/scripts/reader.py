def divide_text_into_chunks(filename, chunk_size=300, start=0):
    chunks = []
    with open(filename, 'rb') as file:
        file.seek(start)
        chunk = ""
        while True:
            char = file.read(1).decode('utf-8', errors='ignore')
            if not char:
                break  # End of file
            if len(chunk.encode('utf-8')) >= chunk_size and char.isspace():
                chunks.append(chunk)
                chunk = ""
                continue
            elif char == '\n':
                chunk += '    '  # Replace line break with a triple space
            elif char == '¬':  # Exclude the "¬" character
                chunk += ''
            else:
                chunk += char

    if chunk:
        chunks.append(chunk)

    return chunks
