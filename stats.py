def word_counter(file_path):
    with open(file_path) as content:
        text = content.read()
        num_words = len(text.split())
    return f"{num_words} words found in the document"