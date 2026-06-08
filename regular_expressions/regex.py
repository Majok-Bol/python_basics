#import regular expressions module
import re

#re.match()
#checks only at the beginning of the string
text="Python is awesome"
result=re.match(r"Python",text)
#capturing
#Groups allow you to extract specific parts of a match.
print(result.group()) 
#Python
#Match found Because Python is at the start.


text2="I love Python"
result2=re.match(r"Python",text2)
# print(result2.group()) #No match found..error;AttributeError: 'NoneType' object has no attribute 'group'


#re.search()
#searches the entire string
text3="I love Python"
search_text=re.search(r"Python",text3)
print(search_text.group())
#Python
 #Match found..Python is in the string text3


#re.findall()

contact="""
bashbytes@gmail.com
alex@yahoo.com
jonte@gmail.com
0723984576
0823123456

"""
print("Contact: ",contact)
'''
Contact:  
bashbytes@gmail.com
alex@yahoo.com
jonte@gmail.com
0723984576
0823123456
'''

#seach for email addresses
emails=re.findall(r"\w+@\w+\.\w+",contact)
print(emails)
print("\nFetching email addresses....")
for email in emails:
    print(email)
'''
Fetching email addresses....
bashbytes@gmail.com
alex@yahoo.com
jonte@gmail.com
'''
#search for phone numbers
phone=re.findall(r"\d{10}",contact)
print("Phone: ",phone) #Phone:  ['0723984576', '0823123456']


