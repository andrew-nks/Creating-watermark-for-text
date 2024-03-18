# detect encoded punctuation
from docx import Document

def read_encoded_punctuation_from_word_file_with_paragraphs(file_path):
    
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
    
    
    # count of non-encoded punctuation
    score = 0

    # count of encoded punctuation
    encoded = 0

    # iterate through each word and each character in text file
    for word in words:
        for ch in word:
            
            if ch in [",",";",":","*","'","’"]:
                score += 1
        
            if ch in ["‚",";","꞉","⃰","῾"]:
                encoded += 1
        
    return [score, encoded]


