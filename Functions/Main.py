from Encoding.encoding_text import text_encoder
from Encoding.encoding_text_file import *
from Detection.detection_text_file import *
from Encoding.encoding_code_file import encode_code_file

is_encoding_or_detection = input("Do you wish to encode or detect AI-generated text?: A. Encode B. Detect  Ans: ")

if is_encoding_or_detection == "A":
    encode_method = input("Choose A. Encode text manually, B. Upload text file, C. Upload code file Ans: ")

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
        input_file_path = "C:/Users/Andrew/OneDrive - Singapore Management University/SMU stuff/Exchange/Social Innovation/Creating-watermark-for-text/Functions/Input/Original text.docx" # Replace with the path to your input Word file
        output_file_path = "C:/Users/Andrew/OneDrive - Singapore Management University/SMU stuff/Exchange/Social Innovation/Creating-watermark-for-text/Functions/Output/Encoded text.docx"   # Replace with the path to the output Word file
    
        paragraph_list = read_words_from_word_file_with_paragraphs(input_file_path)

        # Write words to output file with paragraph structure
        write_words_to_word_file_with_paragraphs(paragraph_list, output_file_path)

    elif encode_method == "C":
        source_path = "C:/Users/Andrew/OneDrive - Singapore Management University/SMU stuff/Exchange/Social Innovation/Creating-watermark-for-text/Functions/Input/Original code.py" # Replace with the path to your input code file
        dest_path = "C:/Users/Andrew/OneDrive - Singapore Management University/SMU stuff/Exchange/Social Innovation/Creating-watermark-for-text/Functions/Output/Encoded code.py" # Replace with the path to your output code file

        encode_code_file(source_path, dest_path)

if is_encoding_or_detection == "B":
    file_path = "C:/Users/Andrew/OneDrive - Singapore Management University/SMU stuff/Exchange/Social Innovation/Creating-watermark-for-text/Functions/Output/Encoded text.docx"  # Replace with the path to input file for AI detection
    result = read_encoded_punctuation_from_word_file_with_paragraphs(file_path)

    print("Proportion of characters generated from AI: " + result)