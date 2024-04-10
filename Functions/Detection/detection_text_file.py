# detect encoded punctuation
from docx import Document

def read_encoded_characters_from_word_file_with_paragraphs(file_path):
    
    # Initialize an empty list to store the words
    words = []

    try:
        # Open the Word document
        doc = Document(file_path)

        # Iterate through each paragraph in the document
        for paragraph in doc.paragraphs:
            # Add the original paragraph text to the list
            words.extend(paragraph.text.split())

        
    except Exception as e:
        # Handle any exceptions that occur during file processing
        print(f"Error reading file: {e}")
    
    
    whitespace_character = "\u200B"  # Four-Per-Em Space character

    # count of non-encoded characters
    score = 0

    # count of encoded characters
    encoded = 0

    # count of whitespaces
    whitespace = 0

    # count of words
    word_count = 0

   

    # iterate through each word and each character in text file
    for word in words:
        for ch in word:
            if ch in "АаВеցіΚӏΜΝոΟΡрԛЅѕΤՍԜԝΥу‚;꞉ǃʾ":
                encoded += 1
            elif ch == whitespace_character:
                whitespace += 1
            else:
                score += 1
        word_count += 1

    

    proportion_of_encoded_characters = str(round(encoded/(encoded + score),4))

    if whitespace > word_count:
         proportion_of_whitespace = str(round(whitespace/score,4))     # whitespace is after every character
    else:
         proportion_of_whitespace = str(round(whitespace/word_count,4))  # whitespace is after every word

    return [proportion_of_encoded_characters, proportion_of_whitespace]
