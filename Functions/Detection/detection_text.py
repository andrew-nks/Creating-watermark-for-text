# Detection of homoglyphs in manually input text
def homoglyph_detection(encoded_text_input):
    homoglyphs = []
    homoglyph_list = "АаВеցіΚӏΜΝոΟΡрԛЅѕΤՍԜԝΥу‚;꞉ǃʾ"

    whitespace_character = "\u200B"  # Four-Per-Em Space character

    # count of non-encoded characters
    score = 0

    # count of encoded characters
    encoded = 0

    # count of whitespaces
    whitespace = 0

    # count of words
    word_count = 0

    
    for ch in encoded_text_input:
        if ch in homoglyph_list:
            encoded += 1
            homoglyphs.append(ch)
        elif ch == whitespace_character:
            whitespace += 1
        else:
            score += 1

    
    
    homoglyph_proportion = str(round(encoded / (score + encoded),2))
    whitespace_proportion = str(round(whitespace/(score + encoded - 1),2))

    homoglyphs = ''.join(homoglyphs)

    return [homoglyph_proportion, whitespace_proportion,homoglyphs]
       