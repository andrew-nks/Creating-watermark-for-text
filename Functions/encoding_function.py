# function to encode text
def text_encoder():
    original_text_input = input("Please enter text: " )
    encoded_text = []
    for char in original_text_input:
        if char == ",":
            encoded_text.append("‚")   # this is unrecognizable
        elif char == ";":
            encoded_text.append(";")   # this is unrecognizable
        elif char == ":":
            encoded_text.append("꞉")   # this is unrecognizable
        elif char == "*":
            encoded_text.append("⃰")   # this appears different
        elif char == "'" or char == "‘" or char == "’":
            encoded_text.append("῾")   # this appears different
       
        else:
            encoded_text.append(char)

    final_text = ''.join(encoded_text)

    return [final_text, original_text_input]

