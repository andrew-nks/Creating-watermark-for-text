# Creating watermark for AI-generated text
For effective watermarks within AI-generated text, several key features are essential: they should be hard to remove, easily detectable and non-disruptive to the content's readability and usability (i.e code snippets).

These Python functions take in a text string and encodes the string via changing letters and punctuation marks. They are designed as part of a Python library for Generative AI platforms such as Chat GPT, Copilot, Bard etc., which rely on Large Language Models, can watermark their generated text. When generated texted is copied wholesale from these platforms, a detector can detect the unusual letters and punctuation used in the text and thus determine how much of a written piece is AI-generated.

A total of 28 characters will be substituted with new homoglyphs (Refer to Encoding Matrix to see the full list). These homoglyph substitutes are letters and punctuation marks from other languages (e.g Cyrillic, Armenian, Greek, etc.) and appear virtually identical to their English counterparts. All homoglyphs use different ASCII keys, which will be flagged up instantly by a detector. Each homoglyph can only be written using Unicode, ALT keystroke or a non-English keyboard, thus authors of written work in English cannot justify their use in articles as "accidental" typing.z

For AI-generated text, whitespaces with zero-spaces are included either between each character or after every word. This acts an additional layer of watermarking, to combat against human efforts to substitute commonly-used words in their AI-generated writing with synonyms.

In the case of AI-generated code snippets, only code comments can be encoded as substituting characters in code itself would render the code unusable.




Example 1:

Original text generated and copied from Chat GPT:

According to "Wikipedia", the smallest countries in the world by land mass are: Vatican City, Monaco, Nauru* (it is worth noting this is an island), and Tuvalu; this is fact-checked by the 'CIA Factbook'.

Encoded text from function:

Аccordіոց to "Ԝіkіреdіа"‚ thе ѕmаllеѕt couոtrіеѕ іո thе ԝorld bу lаոd mаѕѕ аrе꞉ Vаtіcаո Cіtу‚ Μoոаco‚ Νаuru* (іt іѕ ԝorth ոotіոց thіѕ іѕ аո іѕlаոd)‚ аոd Τuvаlu; thіѕ іѕ fаct-chеckеd bу thе ʾCӏА Fаctbookʾ.


