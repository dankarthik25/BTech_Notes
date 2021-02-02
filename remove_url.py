import re
new_file = open('text.org', 'w')
with open("text.org",encoding="'Latin-1'") as f:
    text = re.sub(r'(?:(?:http|https):\/\/)?([-a-zA-Z0-9.]{2,256}\.[a-z]{2,4})\b(?:\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?',"",f.read(),flags=re.MULTILINE)
    text = '\n'.join([a for a in text.split("\n") if a.strip()])
    new_file.write(text)

new_file.close()   
