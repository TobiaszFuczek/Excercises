import re

def verify_email(tekst):
    pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    match = re.search(pattern, tekst)
    if match:
        return match.group()
    else:
        return None

tekst = "bob1234@gmail.com ajajajha akaakjdkjhdhdgjhgs, anakajkjahjhsjsgjgs, jajajjkahkjahah"
print(verify_email(tekst))
