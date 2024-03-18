from encoding_function import text_encoder
from encoding_file import *
from detection_function import *

is_encoding_or_detection = input("Do you wish to encode or detect AI-generated text?: A. Encode B. Detect  Ans: ")

if is_encoding_or_detection == "A":
    encode_method = input("Choose A. Encode manually, B. Upload text file  Ans: ")

    if encode_method == "A":
        original_text_input = input("Please enter your text here: ")
        encoded_text = text_encoder(original_text_input)[0]
        proportion_of_encoding = text_encoder(original_text_input)[2]
        encoded_characters = text_encoder(original_text_input)[3]

        print("This is the encoded text: " + encoded_text)
        print("This is the original text: " + original_text_input)
        print("This is the proportion of encoding: "+ proportion_of_encoding)
        print("This is the characters encoded: "+ encoded_characters)
        
    

    elif encode_method == "B":
        input_file_path = "Original text.docx" # Replace with the path to your input Word file
        output_file_path = "Encoded text.docx"   # Replace with the path to the output Word file
    
        paragraph_list = read_words_from_word_file_with_paragraphs(input_file_path)

        # Write words to output file with paragraph structure
        write_words_to_word_file_with_paragraphs(paragraph_list, output_file_path)

if is_encoding_or_detection == "B":
    file_path = "Encoded text.docx"  # Replace with the path to input file for AI detection
    result = read_encoded_punctuation_from_word_file_with_paragraphs(file_path)

    print("Proportion of characters generated from AI: " + str(round(result[1]/(result[0] + result[1]),2)))