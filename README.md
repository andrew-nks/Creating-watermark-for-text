# Creating watermark for AI-generated text
For effective watermarks within AI-generated text, several key features are essential: they should be hard to remove, easily detectable and non-disruptive to the content's readability.

This Python function takes in a text string and encodes the string via changing punctuation marks. This is designed as part of a Python library for Generative AI platforms such as Chat GPT, Copilot, etc., which rely on Large Language Models, can watermark their generated text. When generated texted is copied wholesale from these platforms, a detector can detect the unusual punctuation used in the text and thus determine how much of a written piece is AI-generated.

A total of 28 characters will be substituted with new alternatives (Refer to Encoding Matrix to see the full list). These substitutes are letters and punctuation marks from other languages (e.g Cyrillic, Armenian, Greek, etc.) and appear virtually identical to their English counterparts. All substitute characters use different ASCII keys, which will be flagged up instantly by a detector. Each substitute character can only be written using Unicode, ALT keystroke or a non-English keyboard, thus authors of written work in English cannot justify their use in articles as "accidental" typing.



Example 1:

Original text generated and copied from Chat GPT:

According to "Wikipedia", the smallest countries in the world by land mass are: Vatican City, Monaco, Nauru* (it is worth noting this is an island), and Tuvalu; this is fact-checked by the 'CIA Factbook'.

Encoded text from function:

Аccordіոց to "Ԝіkіреdіа"‚ thе ѕmаllеѕt couոtrіеѕ іո thе ԝorld bу lаոd mаѕѕ аrе꞉ Vаtіcаո Cіtу‚ Μoոаco‚ Νаuru* (іt іѕ ԝorth ոotіոց thіѕ іѕ аո іѕlаոd)‚ аոd Τuvаlu; thіѕ іѕ fаct-chеckеd bу thе ʾCӏА Fаctbookʾ.


