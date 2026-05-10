#You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
#print('He is called "Johnny"')
#print("He is called 'Johnny'")
#print("It's alright")

#Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
#a = "Hello"
#print(a)

#Multiline Strings
#a = """Lorem ipsum dolor sit amet,
#consectetur adipiscing elit,
#sed do eiusmod tempor incididunt
#ut labore et dolore magna aliqua."""
#print(a)

#a = '''Lorem ipsum dolor sit amet,
#consectetur adipiscing elit,
#sed do eiusmod tempor incididunt
#ut labore et dolore magna aliqua.'''
#print(a)

#Strings are arrays
#a = "Hello World!"
#print(a[1])

#Looping Through a String
#for x in "banana":
 #   print(x)

#String Length
#a = "Hello, World!"
#print(len(a))

#Check String
#txt = "The best things in life are free!"
#print("free" in txt)

#txt = "The best things in life are free!"
#if "free" in txt:
 #   print("Yes, 'free' is present")

#Check if not
#txt = "The best things in life are free!"
#print("expensive" not in txt)

#txt = "The best things in life are free!"
#if "expensive" not in txt:
#    print("No, 'expensive' is NOT present.")

#Slicing
#b = "Hello, World!"
#print(b [2:5])

#Slicing from the start
#b = "Hello, World!"
#print(b [:5])

#Slice to the end
#b = "Hello, World!"
#print(b[2:])

#Negative Indexing
#b = "Hello, World!"
#print(b[-5:-2])

#Upper case
#a = "Hello, World!"
#print(a.upper())

#Lower Case
#a = "Hello, World!"
#print(a.lower())

#Remove Whitespace
#a = "Hello, World"
#print(a.strip()) #Returns "Hello, World!"

#Replace string
#a = "Hello, World!"
#print(a.replace("H", "J"))

#Split String
#a = "Hello, World!"
#print(a.split(" ")) #Returns ['Hello,', 'World!']

#String concatenation
#a = "Hello"
#b = "World"
#c = a + b
#print(c)

#a = "Hello"
#b = "World"
#c = a + " " + b
#print(c)

#String Format
#In Python cannot combine string and numbers, but we can combine string and numbers by using f-strings or the format() method!

#f-strings
#age = 36
#txt = f"My name is John, I am {age} years old."
#print(txt)

#Placeholders and modifiers
#price = 59
#txt = f"The price is {price} dollars."
#print(txt)

#price = 59
#txt = f"The price is {price:.2f} dollars."
#print(txt)

#txt =f"The price is {20 * 59} dollars"
#print(txt)

#Escape the character
#txt = "We are so-called \"Vikings\" from the north."
#print(txt)

#Escape the characters
#\' - Single quote
#txt = 'It\'s alright.'
#print(txt)

#\\ - Backslash
#txt = "This will insert one \\ (Backslash)."
#print(txt)

#\n - New Line
#txt = "Hello\nWorld!"
#print(txt)

#\r - Carriage Return
#txt = "Hello\rWorld!"
#print(txt)

#\t - Tab
#txt = "Hello\tWorld!"
#print(txt)

#\b - Backspace
#txt = "Hello \bWorld!"
#print(txt)

#\f - Form Feed

#\ooo - Octal value
#txt = "\110\145\154\154\157"
#print(txt)

#\xhh - Hex value
#txt = "\x48\x65\x6c\x6c\x6f"
#print(txt)

#String methods

#Converts the first character to upper case
#txt = "hello, and welcome to my world."
#x = txt.capitalize()
#print(x)

#Converts string into lower case
#txt = "Hello, And Welcome To My World."
#x = txt.casefold()
#print(x)

#Returns a centered string
#txt = "banana"
#x = txt.center(20)
#print(x)

#txt = "Banana"
#x = txt.center(20, "O")
#print(x)

#Returns the number of times a specified value occurs in a string
#txt = "I love apples, apple is my favorite fruit"
#x = txt.count("apple")
#print(x)

#Returns an encoded version of the string
#txt = "My name is Ståle"
#x = txt.encode()
#print(x)

#These examples uses ascii encoding, and a character that cannot be encoded, showing the result with different errors:
#txt = "My name is Ståle"

#print(txt.encode(encoding="ascii",errors="backslashreplace"))
#print(txt.encode(encoding="ascii",errors="ignore"))
#print(txt.encode(encoding="ascii",errors="namereplace"))
#print(txt.encode(encoding="ascii",errors="replace"))
#print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))


#Returns true if the string ends with the specified value
#txt = "Hello, welcome to my world."
#x = txt.endswith(".")
#print(x)

#txt = "Hi, welcome to my castle."
#x = txt.endswith(("world.", "castle."))
#print(x)

#Sets the tab size of the string
#txt = "H\te\tl\tl\to"
#x = txt.expandtabs(2)
#print(x)

#txt = "H\te\tl\tl\to"

#print(txt)
#print(txt.expandtabs())
#print(txt.expandtabs(2))
#print(txt.expandtabs(4))
#print(txt.expandtabs(10))

#Searches the string for a specified value and returns the position of where it was found
#txt = "Welcome, to my world."
#x = txt.find("Welcome")
#print(x)

#txt = "Hello, welcome to my world."
#x = txt.find("e")
#print(x)

#Formats specified values in a string
#txt = "For only {price:.2f} dollars!"
#print(txt.format(price=49))

#txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 23)
#txt2 = "My name is {0}, I'm {1}".format("John", 23)
#txt3 = "My name is {}, I'm {}".format("John", 23)

#print(txt1)
#print(txt2)
#print(txt3)

#Formating types
#txt = "We have {:<8} chickens."
#print(txt.format(49))

#txt = "We have {:>8} chickens."
#print(txt.format(49))

#txt = "We have {:^8} chickens."
#print(txt.format(49))

#txt = "The temperature is {:=8} degrees celsius."
#print(txt.format(-5))

#txt = "The temperature is between {:+} and {:+} degrees celsius."
#print(txt.format(-3, 7))

#txt = "The temperature is between {:-} and {:-} degrees celsius."
#print(txt.format(-3, 7))

#txt = "The temperature is between {: } and {: } degrees celsius."
#print(txt.format(-3, 7))


#txt = "The universe is {:,} years old."
#print(txt.format(13800000000))

#txt = "The universe is {:_} years old."
#print(txt.format(13800000000))

#txt = "The binary version of {0} is {0:b}"
#print(txt.format(5))

#txt = "We have {:d} chickens."
#print(txt.format(0b101))

#txt = "We have {:e} chickens."
#print(txt.format(5))

#txt = "We have {:E} chickens."
#print(txt.format(5))

#txt = "The price is {:.2f} dollars."
#print(txt.format(45))

#txt = "The price is {:f} dollars."
#print(txt.format(45))

#x = float('inf')
#txt = "The price is {:F} dollars."
#print(txt.format(x))

#txt = "The price is {:f} dollars."
#print(txt.format(x))

#txt = "The octal version of {0} is {0:o}"
#print(txt.format(10))

#txt = "The Hexadecimal version of {0} is {0:x}"
#print(txt.format(255))

#txt = "The Hexadecimal version of {0} is {0:X}"
#print(txt.format(255))

#txt = "You scored {:%}"
#print(txt.format(0.25))

#txt = "You scored {:.0%}"
#print(txt.format(0.25))

#Searches the string for a specified value and returns the position of where it was found
#txt = "Hello, welcome to my world."
#x = txt.index("welcome")
#print(x)

#txt = "Hello, welcome to my world."
#x = txt.index("e")
#print(x)

#Returns True if all characters in the string are alphanumeric
#txt = "Company12"
#x = txt.isalnum()
#print(x)

#txt = "Company 12"
#x = txt.isalnum()
#print(x)

#Returns True if all characters in the string are in the alphabet
#txt = "CompanyX"
#x = txt.isalpha()
#print(x)

#txt = "Company12"
#x = txt.isalpha()
#print(x)

#Returns True if all characters in the string are ascii characters
#txt = "Company123"
#x = txt.isascii()
#print(x)

#Returns True if all characters in the string are decimals
#txt = "1234"
#x = txt.isdecimal()
#print(x)

#a = "\u0030"
#b = "\u0047"

#print(a.isdecimal())
#print(b.isdecimal())

#Returns True if all characters in the string are digits
#txt = "50800"
#x = txt.isdigit()
#print(x)

#a = "\u0030"
#b = "\u00B2"

#print(a.isdigit())
#print(b.isdigit())

#Returns True if the string is an identifier
#txt = "Demo"
#x = txt.isidentifier()
#print(x)

#a = "MyFolder"
#b = "Demo002"
#c = "2bring"
#d = "my demo"

#print(a.isidentifier())
#print(b.isidentifier())
#print(c.isidentifier())
#print(d.isidentifier())

#Returns True if all characters in the string are lower case
#txt = "hello world"
#x = txt.islower()
#print(x)

#a = "Hello world!"
#b = "hello 123"
#c = "mynameisPeter"

#print(a.islower())
#print(b.islower())
#print(c.islower())

#Returns True if all characters in the string are numeric
#txt = "555643"
#x = txt.isnumeric()
#print(x)

#Returns True if all characters in the string are printable
#txt = "Hello! Are you #1"
#x = txt.isprintable()
#print(x)

#txt = "Hello!\nAre you #1?"
#x = txt.isprintable()
#print(x)

#Returns True if all characters in the string are whitespaces
#txt = "   "
#x = txt.isspace()
#print(x)

#Returns True if the string follows the rules of a title
#txt = "Hello, And Welcome To My World!"
#x = txt.istitle()
#print(x)

#a = "HELLO, AND WELCOME TO MY WORLD"
#b = "Hello"
#c = "22 Names"
#d = "This Is %'!?"

#print(a.istitle())
#print(b.istitle())
#print(c.istitle())
#print(d.istitle())

#Returns True if all characters in the string are upper case
#txt = "THIS IS NOW!"
#x = txt.isupper()
#print(x)

#Joins the elements of an iterable to the end of the string
#myTuple = ("John", "Peter", "Vicky")
#x = "#".join(myTuple)
#print(x)

#MyDict = {"name": "John", "country": "Norway"}
#mySeparator = "TEST"
#x = mySeparator.join(MyDict)
#print(x)

#Returns a left justified version of the string
#txt = "banana"
#x = txt.ljust(20)
#print(x, "is my favorite fruit")

#txt = "banana"
#x = txt.ljust(20, "O")
#print(x)

#Converts a string into lower case
#txt = "Hello my FRIENDS"
#x = txt.lower()
#print(x)

#Returns a left trim version of the string
#txt = "      banana       "
#x = txt.lstrip()
#print("of all fruits", x,"is my favorite")

#txt = ",,,,,,,ssaaww.......banana"
#x = txt.lstrip(",.saw")
#print(x)

#Returns a translation table to be used in translations
#txt = "Hello Sam!"
#myTable = str.maketrans("S", "P")
#print(txt.translate(myTable))

#txt = "Hi Sam!"
#x = "mSa"
#y = "eJo"
#myTable = str.maketrans(x, y)
#print(txt.translate(myTable))

#txt = "Good night Sam!"
#x = "mSa"
#y = "eJo"
#z = "odnght"
#mytable = str.maketrans(x, y, z)
#print(txt.translate(mytable))

#Returns a tuple where the string is parted into three parts
#txt = "I could eat bananas all day"
#x = txt.partition("bananas")
#print(x)

#Returns a string where a specified value is replaced with a specified value
#txt = "I like bananas"
#x = txt.replace("bananas", "apples")
#print(x)

#txt = "one one was a race horse, two two was one too"
#x = txt.replace("one", "three", 2)
#print(x)

#Searches the string for a specified value and returns the last position of where it was found
#txt = "Mi casa, su casa"
#x = txt.rfind("casa")
#print(x)
#Method is almost the same like rindex()

#Searches the string for a specified value and returns the last position of where it was found
#txt = "Mi casa, su casa."
#x = txt.rindex("casa")
#print(x)

#txt = "Hello, welcome to my world."
#x = txt.rindex("e")
#print(x)

#txt = "Hello, welcome to my world."
#x = txt.rindex("e", 5, 10)
#print(x)

#Returns a right justified version of the string
#txt = "banana"
#x = txt.rjust(20)
#print(x,  "is my favorite fruit")

#Returns a tuple where the string is parted into three parts
#txt = "I could eat bananas all day, bananas are my favorite fruit"
#x = txt.rpartition("bananas")
#print(x)

#Splits the string at the specified separator, and returns a list
#txt = "apple, banana, cherry"
#x = txt.rsplit(", ")
#print(x)

#txt = "apple, banana, cherry"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
#x = txt.rsplit(", ", 1)
#print(x)

#Returns a right trim version of the string
#txt = "     banana     "
#x = txt.rstrip()
#print("of all fruits", x, "is my favorite")

#txt = "banana,,,,,ssqqqww....."
#x = txt.rstrip(",.qsw")
#print(x)

#Splits the string at the specified separator, and returns a list
#txt = "welcome to the jungle"
#x = txt.split()
#print(x)

#Splits the string at line breaks and returns a list
#txt = "Thank you for the music\nWelcome to the jungle"
#x = txt.splitlines()
#print(x)

#Returns true if the string starts with the specified value
#txt = "Hello, welcome to my world."
#x = txt.startswith("Hello")
#print(x)

#Returns a trimmed version of the string
#txt = "     banana     "
#x = txt.strip()
#print("of all fruits", x, "is my favorite")

#Swaps cases, lower case becomes upper case and vice versa
#txt = "Hello My Name Is PETER"
#x = txt.swapcase()
#print(x)

#Converts the first character of each word to upper case
#txt = "Welcome to my world"
#x = txt.title()
#print(x)

#Returns a translated string
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
#mydict = {83:  80}
#txt = "Hello Sam!"
#print(txt.translate(mydict))

#Converts a string into upper case
#txt = "Hello my friends"
#x = txt.upper()
#print(x)

#Fills the string with a specified number of 0 values at the beginning
#txt = "50"
#x = txt.zfill(10)
#print(x)

#a = "hello"
#b = "welcome to the jungle"
#c = "10.000"

#print(a.zfill(10))
#print(b.zfill(10))
#print(c.zfill(10))
