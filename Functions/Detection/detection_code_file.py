# detect encoded characters

def read_encoded_characters_from_code_file(file_path):
    
    # Initialize an empty string to store each line of code
    current_line = ''

    with open(file_path, 'r', encoding='utf-8') as file:

        # count of non-encoded characters
        score = 0

        # count of encoded characters
        encoded = 0

        whitespace_character = "\u200B"  # Four-Per-Em Space character

        # count of whitespaces
        whitespace = 0

        # Flag to track if we are currently inside a comment block
        inside_comment = False

        # Iterate through each character
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

            elif char == "!" and not inside_comment: # checking if "<!--" is present i.e HTML comment
                if current_line and current_line[-1] == "<":
                    inside_comment = True
                current_line += char

            # Check if current character is the end of a comment
            elif char == '\n' and inside_comment:
                inside_comment = False  # if char is end of line, flag indicates end of comment i.e out of comment block
                current_line = ''

            # Check if the current letter is inside the comment block
            elif inside_comment:
                if char in "АаВеցіΚӏΜΝոΟΡрԛЅѕΤՍԜԝΥу‚;꞉ǃʾ":  # if char is encoded, +1 to encoded count
                    encoded += 1
                elif char == whitespace_character:
                    whitespace += 1
                else:                                      # else, +1 to non-encoded score
                    score += 1
    
        if score + encoded > 0:
            proportion_of_encoded = str(round(encoded/(score + encoded), 4))
            proportion_of_whitespace = str(round(whitespace/(score + encoded), 4))
        else:
            proportion_of_encoded = '0'
            proportion_of_whitespace = '0'

        return [proportion_of_encoded, proportion_of_whitespace]