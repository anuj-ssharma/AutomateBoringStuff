import re,pyperclip



#Create regex for phone numbers

PhoneRegex = re.compile(r'''
#415-555-0000,555-0000,(415) 555-0000,555-0000 ext 12345, ext. 12345, c12345
(
((\d\d\d)|(\(\d\d\d\)))?    #area code (optional)
(\s|-)?                      #first separator
\d\d\d                      #first 3 digits
-                           #separator
\d\d\d\d                    #last 4 digits
(ext(\.)?\s|x)?              #extension word part (optional)
((\d{2,5}))?                #extension number part (optional)
)
''', re.VERBOSE)



#Create regex for email addresses

emailRegex = re.compile(r'''
#some.+_thing@something.com
[a-zA-Z0-9_.+]+              # name part
@                            # @ symbol
[a-zA-Z0-9_.+]+              # domain name part
''',re.VERBOSE)

#Get the text off the clipboard

text = '515-565-5656 anuj576@gmail.com'


#Extract the email/phone from the text

extractedPhone = PhoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

print extractedPhone
print extractedEmail

#TO DO - Copy the extracted email/phone to the clipboard

