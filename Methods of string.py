# METHODS OF A STRING

# LEN FUNCTION WILL RETURN THE LENGTH OF A STRING
Name="Prince"
print(len(Name))

# UPPER()
# IT WILL CONVERT YOUR STRING IN UPPERCASE
a="prince"
print(a.upper())


# LOWER IT WILL CONVERT YOUR STRING IN LOWERCASE
b="PRINCE"
print(b.lower())

# SWAPCASE ITS WILL CONVERT YOUR UPPERCASE IN TO LOWERCASE AND VISE VERSA
C="MaGGi"
print(C.swapcase())


# THE STRIP() METHOD REMOVES ANY WHITESPACE FROM THE BEGINNING OR THE END:
D = " Hello, World! "
print(D.strip()) # returns "Hello, World!"


# THE REPLACE() METHOD REPLACES A STRING WITH ANOTHER STRING:
E = "Hello, World"
print(E.replace("Hello", "Namaste"))

# THE SPLIT() METHOD SPLITS THE STRING INTO SUBSTRINGS IF IT FINDS INSTANCES OF THE SEPARATOR:
f= "Hello World!"
print(f.split(",")) # returns ['Hello', ' World!']

# CAPITALIZED()
A="timesodindia"
print(A.capitalize())

# CENTER ALIGN THE STRING IN TO THE CENTER
B="Hindu times"
print(B.center(50))
print(len(B.center(50)))

# COUNT() IT WILL  RETURN THE HOW MANY TIMES THE GIVEN VALUE OCCURED IN THE STRING
C="Prrince"
print(C.count("r"))

# ENDSWITH() IT WILL THE CHECK THE LAST LETTER OR WORD AND ANS IN BOOLEAN
a="maratha"
print(a.endswith("a"))
print(a.endswith("s"))

# STARTSWITH 
clzname="universal msg sgkm"
print(clzname.startswith("universal"))

# FIND() RETURN INDEXING IF NOT FOUND THEN IT WILL RETURN -1
txt = "Hello, welcome to my world."
print(txt.find("H"))
print(txt.find("C"))

# ISLOWER
a="andy"
print(a.islower())

# ISUPPER
a="andy"
print(a.isupper())
b="MADE"
print(b.isupper())

# ISPRINTABLE
a="hi i am prince tiwari \n"
print(a.isprintable())
c="hi i am prince tiwari "
print(c.isprintable())

# ISTITLE ITS WILL CHECK THE FIRST WORLD OF A LETTER IS CAPITAL OR NOT AND RETURN BOOLEEN RESULT
a="Mango  Yellow Yes"
print(a.istitle())

# TITLE IT WILL CONVERT LOWER CASE IN UPPER CASE OF FIRST ALPHABET
z="python is very intreasting"
print(z.title())

# ISALNUM  RETURN TRUE ONLY IF STRIG CONTAIN A-Z ,A-Z,0-9.
str1="welcometothehomeDon2"
print(str1.isalnum())

# ISALPHA IT SHOULD ONLY CONTAIN  A-Z ,A-Z.
str2="welcometothehomeDon2"
print(str2.isalpha())
str1="welcometothehomeDon"
print(str1.isalnum())