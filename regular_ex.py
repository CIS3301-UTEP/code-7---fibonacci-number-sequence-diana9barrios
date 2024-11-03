import re

file_object = open("social_media_users.csv")
text_from_file = file_object.read()
emails = re.findall('[a-z]+@[a-z]{7,}\.com',text_from_file)
# print(text_from_file)
print(emails)

are_emails = re.search('[a-z]+@gmail\.com',text_from_file)
print(are_emails)