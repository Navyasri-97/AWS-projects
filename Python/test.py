#String-concat
str1 = "Hello"
str2 = "World"
result = str1 + str2
print(result)

#string-len
text = "Welcome to the python class"
length = len(text)
print("Length of the line:", length)

#string-uppercase&lowercase
sentence = "Python World"
uppercase = sentence.upper()
lowercase = sentence.lower()
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)

#string-replace
sentence1 = "python is awesome"
new_sentence = sentence1.replace("awesome", "great")
print("modified sentence is:", new_sentence)

#string-split
text1 = "Python is awesome"
words = text1.split()
print("Words:", words)

#string-strip
text2 = "   Some spaces around   "
stripped_text = text2.strip()
print("Stripped text:", stripped_text)

#string-substring
text3 = "Python is awesome"
substring = "is"
if substring in text3:
    print(substring, "found in the text")
else:
    print("not found")

#float
# Float variables
num1 = 5.0
num2 = 2.5

# Basic Arithmetic
result1 = num1 + num2
print("Addition:", result1)

result2 = num1 - num2
print("Subtraction:", result2)

result3 = num1 * num2
print("Multiplication:", result3)

result4 = num1 / num2
print("Division:", result4)

# Rounding
result5 = round(3.14159265359, 2)  # Rounds to 2 decimal places
print("Rounded:", result5)


#int
# Integer variables
num1 = 10
num2 = 5

# Integer Division
result1 = num1 // num2
print("Integer Division:", result1)

# Modulus (Remainder)
result2 = num1 % num2
print("Modulus (Remainder):", result2)

# Absolute Value
result3 = abs(-7)
print("Absolute Value:", result3)


#regex-findall
import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")

#regex-match
import re

text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")

#regex-replace
import re

text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)

#regex-search
import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")

#regex-split
import re

text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)