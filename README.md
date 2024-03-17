# Encoding-function
For effective watermarks within generative AI text, several key features are essential: they shoyld be hard to remove, easily detectable and non-disruptive to the content's readability.

This Python function takes in a text string and encodes the string via changing punctuation marks. This is designed as part of a Python library for Generative AI platforms such as Chat GPT, Copilot, etc., which rely on Large Language Models, can watermark their generated text. When generated texted is copied wholesale from these platforms, a detector can detect the unusual punctuation used in the text and thus determine how much of a written piece is AI-generated.

Six different punctuation marks are used in the encoding. Four are almost identical to the original punctuation and requires a detector i.e comma, semicolon, colon and double quotation marks. Two are visible to the naked eye i.e single quotation mark and asterisk. This allows human readers to detect hints of AI-generated text copied onto written pieces without a detector. All six encoded punctuation marks use different ASCII keys, which will be flagged up instantly. Each punctuation can only be written using Unicode, thus authors of written work cannot justify their use in written articles as "accidental" typing.

Example 1:

Original text generated and copied from Chat GPT:

According to "Wikipedia", the smallest countries in the world by land mass are: Vatican City, Monaco, Nauru* (it is worth noting this is an island), and Tuvalu; this is fact-checked by the 'CIA Factbook'.

Encoded text from function:

According to "Wikipedia"‚ the smallest countries in the world by land mass are꞉ Vatican City‚ Monaco‚ Nauru⃰ (it is worth noting this is an island)‚ and Tuvalu; this is fact-checked by the ῾CIA Factbook῾.


