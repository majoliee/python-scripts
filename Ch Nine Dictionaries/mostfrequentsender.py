# Write a program to read through the mbox-short.txt and figure out who has sent 
# the greatest number of mail messages. The program looks for 'From ' lines and 
# takes the second word of those lines as the person who sent the mail. The program 
# creates a Python dictionary that maps the sender's mail address to a count of 
# the number of times they appear in the file. After the dictionary is produced, 
# the program reads through the dictionary using a maximum loop to find the most 
# prolific committer.

sender = dict()
committer = None
email_list = []
frequency_check = 0

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

for line in handle:
    if line.startswith("From "):
        text =line.strip().split(" ")
        email_list.append(text[1])
    else: 
        continue
    
for address in email_list: 
    sender[address] = sender.get(address,0) + 1
    
for key,value in sender.items():
    if value > frequency_check:
        frequency_check = value
        committer = key
        
    else: 
        continue

print(committer,frequency_check)
