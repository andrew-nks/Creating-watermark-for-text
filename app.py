import os
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from Functions.Encoding.encoding_text import text_encoder
from Functions.Encoding.encoding_text_file import *
from Functions.Encoding.encoding_code_file import encode_code_file
from Functions.Detection.detection_text_file import *
from Functions.Detection.detection_code_file import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

# Encoding text manually typed in the box
@app.route('/process_form', methods=['POST'])
def process_form():
    original_text_input = request.form['encode']
    
    encoded_output = text_encoder(original_text_input)[0]
    proportion_of_encoding = text_encoder(original_text_input)[1]
    encoded_characters = text_encoder(original_text_input)[2]
    whitespace_characters = text_encoder(original_text_input)[3]
    
    # Encoding and returning the details of homoglyphs
    return render_template('form.html', encoded_output=encoded_output, 
                           proportion_of_encoding = proportion_of_encoding,
                           encoded_characters = encoded_characters,
                           whitespace_characters = whitespace_characters)

# Encoding text file
@app.route('/upload_text', methods=['POST'])
def upload_text_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    if file:
        # Save the uploaded file to a temporary location
        input_file_path = secure_filename(file.filename)
        file.save(input_file_path)

        # Define the output file path
        output_file_path = "C:/Users/Andrew/OneDrive - Singapore Management University/SMU stuff/3.2 Exchange/Social Innovation/Creating-watermark-for-text/Functions/Output/Encoded text.docx"   # Replace with the path to the output Word file
        
        # Modify the Word document
        paragraph_list = read_words_from_word_file_with_paragraphs(input_file_path)
        
        # Write words to the output file 
        write_words_to_word_file_with_paragraphs(paragraph_list, output_file_path)

        # Send the modified document as a file download
        return send_file(output_file_path, as_attachment=True)
    
# Encoding code file
@app.route('/upload_code', methods=['POST'])
def upload_code_file():
    if 'code_file' not in request.files:
        return "No file part"
    
    file = request.files['code_file']
    print(file)

    if file.filename == '':
        return "No selected file"
    

    if file:
        # Save the uploaded file to a temporary location
        input_file_path = secure_filename(file.filename)
        file.save(input_file_path)

        # Get the suffix of the code file
        file_extension = os.path.splitext(input_file_path)[1]

        # Define the output file path
        output_file_path = "C:/Users/Andrew/OneDrive - Singapore Management University/SMU stuff/3.2 Exchange/Social Innovation/Creating-watermark-for-text/Functions/Output/Encoded code"+file_extension   # Replace with the path to the output Word file
        
        
        # Write code to the output file 
        encode_code_file(input_file_path, output_file_path)
        print(output_file_path)

        # Send the modified document as a file download
        return send_file(output_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
