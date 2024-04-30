from Encoding.encoding_text import text_encoder
from Encoding.encoding_text_file import *
from Detection.detection_text_file import *
from Encoding.encoding_code_file import encode_code_file
from Detection.detection_code_file import *

is_encoding_or_detection = input("Do you wish to encode or detect AI-generated text?: A. Encode B. Detect  Ans: ")

if is_encoding_or_detection == "A":
    encode_method = input("Choose A. Encode text manually, B. Upload text file, c. Upload code file Ans: ")

    if encode_method == "A":
        original_text_input = input("Please enter your text here: ")
        encoded_text = text_encoder(original_text_input)[0]
        proportion_of_encoding = text_encoder(original_text_input)[1]
        encoded_characters = text_encoder(original_text_input)[2]
        whitespace_characters = text_encoder(original_text_input)[3]

        print("This is the encoded text: " + encoded_text)
        print("This is the original text: " + original_text_input)
        print("This is the proportion of encoding: "+ proportion_of_encoding)
        print("This is the characters encoded: "+ encoded_characters)
        print("This is the proportion of whitespaces: " + whitespace_characters)
        


    elif encode_method == "B":
        input_file_path = "/Creating-watermark-for-text/Functions/Input/Original text.docx" # Replace with the path to your input Word file
        output_file_path = "/Creating-watermark-for-text/Functions/Output/Encoded text.docx"   # Replace with the path to the output Word file
    
        paragraph_list = read_words_from_word_file_with_paragraphs(input_file_path)

        # Write words to output file with paragraph structure
        write_words_to_word_file_with_paragraphs(paragraph_list, output_file_path)

    elif encode_method == "C":
        source_path = " /Creating-watermark-for-text/Functions/Input/Original code.py"   # Replace with the path to the output Word file
        dest_path = "/Creating-watermark-for-text/Functions/Output/Encoded code.py"   # Replace with the path to the output Word file

        encode_code_file(source_path, dest_path)

if is_encoding_or_detection == "B":
    detection_medium = input("Choose A. Detection for Text file., B. Detection for Code file. Ans: ")

    if detection_medium == "A":
        file_path = "/Creating-watermark-for-text/Functions/Output/Encoded text.docx"  # Replace with the path to input file for AI detection
        homoglyph_proportion = read_encoded_characters_from_word_file_with_paragraphs(file_path)[0]
        whitespace_proportion = read_encoded_characters_from_word_file_with_paragraphs(file_path)[1]
        
        
        print("Proportion of homoglyphs within text: " + homoglyph_proportion)
        print("Proportion of text generated from AI: " + whitespace_proportion)
        
    