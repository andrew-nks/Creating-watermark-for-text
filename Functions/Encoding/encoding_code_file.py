# Function to encode .py files 
def encode_code_file(source_path, dest_path):
    
    try:
        # Open the Python file in read mode
        with open(source_path, 'r', encoding='utf-8') as file:
            # Open the new document in write mode
            with open(dest_path, 'w', encoding='utf-8') as new_file:
                # Initialize variables to store the current line and lines of code
                current_line = ''
                ref_dict = {char: index for index, char in enumerate("AaBegiKIMNnOPpqSsTUWwYy,;:!'")}
                encoding_dict = {char: index for index, char in enumerate("АаВеցіΚӏΜΝոΟΡрԛЅѕΤՍԜԝΥу‚;꞉ǃʾ")}

                # encoding alphabet & punctuation
                invert_ref_dict = {value: key for key, value in ref_dict.items()}
                invert_encoding_dict = {value: key for key, value in encoding_dict.items()}

                # Use a unicode whitespace character to separate each letter
                whitespace_character = "\u200B"  # Four-Per-Em Space character

                '''
                These characters denote comments in most  languages:
                #, //, /*, --
                e.g Python, Java, Javascript, C, C++, Rust, Go, Typescript, PHP, CSS and SQL
                '''
                # Flag to track if we are currently inside a comment block
                inside_comment = False

                # Iterate through each character in the file
                for char in file.read():
                                
                    # Check if current character is the start of a comment
                    if char == "#" and not inside_comment:
                        inside_comment = True   # if char is a comment character, flag indicates we are inside a comment block
                        current_line += char

                    elif char == "/" and not inside_comment: # checking if "//" is present e.g Javascript comment
                        if current_line and current_line[-1] == "/":
                            inside_comment = True   
                        current_line += char
                    
                    elif char == "*" and not inside_comment: # checking if "/*" is present i.e CSS comment
                        if current_line and current_line[-1] == "/":
                            inside_comment = True   
                        current_line += char
                    
                    elif char == "-" and not inside_comment: # checking if "--" is present i.e SQL comment
                        if current_line and current_line[-1] == "-":
                            inside_comment = True   
                        current_line += char


                    # Check if current character is the end of a comment
                    elif char == '\n' and inside_comment:
                        inside_comment = False  # if char is end of line, flag indicates end of comment i.e out of comment block
                        # Write the current line to the new file
                        new_file.write(current_line + '\n')
                        # Reset the current line for the next line of code
                        current_line = ''


                    # Check if the current letter is inside the comment block
                    elif inside_comment:
                        if char in ref_dict:    # If char can be encoded, add the encoded character to current line
                            index = ref_dict[char]
                            current_line += invert_encoding_dict[index] 
                            
                        elif char == " ":
                            current_line += char
                            current_line += whitespace_character    # add whitespace only at the start of words within comments
                            

                        else:
                            current_line += char # If not, add the current character to the current line
                            

                    # For all characters that are outside comment blocks entirely
                    elif not inside_comment:
                        current_line += char # Add the current character to the current line


                    # Check if the current character is a newline character
                    if char == '\n' and not inside_comment:   
                        # Write the current line to the new file
                        new_file.write(current_line)
                        # Reset the current line for the next line of code
                        current_line = ''

        print("Contents copied from source file to destination file.")
        return True
    
    except Exception as e:
        print("An error occurred:", str(e))
        return False



