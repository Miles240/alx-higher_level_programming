import re

text_to_search = """
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + { } [ ] / | ( )

coreyms.com

321-555-4321
123.555.1234
800.555.1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson

"""

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

urls = '''
https://www.google.com
http://coreyms.com
https://www.nasa.gov
https://youtube.com
'''

sentence = "Start a sentence and then bring it to an end"


# pattern_1= re.compile(r'[a-zA-Z0-9-]+@[a-zA-Z-]+\.(com|edu|net)')
# matches = pattern_1.finditer(emails)

pattern_2 = re.compile(r'https?://(www\.)?(\w+)?(\.\w+)')
matches = pattern_2.finditer(urls)

for match in matches:
    print(match.group(2))