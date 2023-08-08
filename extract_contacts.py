import requests
from bs4 import BeautifulSoup
import re

output_file = open("emleandphon.csv", "w", encoding="utf-8")
output_file.write("Email,Phone\n")

try:
    websites = [
        "https://iru.university/wt/language/ar/",
        "https://www.merit-tc.com/",
        "https://oacademi.org/",
        "https://germanboard.org/index-ar.php",
        "https://mornvest.com/ar/?gclid=Cj0KCQjw_7KXBhCoARIsAPdPTfih4TO6i6GYNWMUwbkBpux8enEAD4BXN9zturlur9PpbqGBpEK-j6saAnCSEALw_wcB"
    ]
except Exception as exp:
    print(exp)
    print(type(exp))

email_list = []
phone_list = []

for website in websites:
    r = requests.get(website)
    soup = BeautifulSoup(r.content, "html.parser")
    
    for email_link in soup.find_all("a", attrs={"href": re.compile("^mailto:")}):
        email_list.append(email_link.get('href'))
    
    for phone_link in soup.find_all("a", attrs={"href": re.compile("^tel:")}):
        phone_list.append(phone_link.get("href"))

# Ensure both lists have the same length
min_length = min(len(email_list), len(phone_list))
email_list = email_list[:min_length]
phone_list = phone_list[:min_length]

# Write data to the output file
for i in range(min_length):
    output_file.write(email_list[i] + " , " + phone_list[i] + "\n")

output_file.close()
