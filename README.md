# Encoding-function
Python function that takes in a text string and can encode the string via changing punctuation marks.

List of punctuation marks altered:
Encoding 1
,‚
hello, (alt 44)
hello‚ (alt 0130)

Encoding 2
hello; (alt 59)
hello; (U+037E – Greek question mark)
; ; 

Encoding 3

hello: (colon)
hello꞉ (A789)
꞉::

Encoding 4
⃰*   
hello⃰ (u+20f0)
hello*(asterisk)

Encoding 5
‘῾
‘hello’ (original)
῾hello’ (u+1ffe)

Encoding 6
“‟
“hello” (normal)
‟hello” (u+201F)


