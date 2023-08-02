def count_characters(text):
    return len(text)

def count_words(text):
    words = text.split()
    return len(words)

def count_sentences(text):
    sentences = text.split('. ')
    return len(sentences)

def analyze_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

        character_count = count_characters(text)
        word_count = count_words(text)
        sentence_count = count_sentences(text)

        print("File Analysis:")
        print("Character count:", character_count)
        print("Word count:", word_count)
        print("Sentence count:", sentence_count)

print("Welcome to Words Counter!")

file_path = input("Enter the file path: ")
analyze_file(file_path)