import re

tekst= "bob1234@gmail.com"

def verify_email(tekst):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    mail= re.findall(pattern, tekst)
    return mail

print(verify_email(tekst))
