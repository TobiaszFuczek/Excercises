# Utwórz program, który czyta plik tekstowy i wyodrębnia określone informacje,
# na przykład numery telefonów, adresy e-mail, daty itp.

import re

def extract_information(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'

    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    phones = re.findall(phone_pattern, text)

    emails = re.findall(email_pattern, text)

    return phones, emails

file_path = 'sample.txt'  
phones, emails = extract_information(file_path)

print("Numery telefonów znalezione w pliku:")
for phone in phones:
    print(phone)

print("\nAdresy e-mail znalezione w pliku:")
for email in emails:
    print(email)