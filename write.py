import requests

from bs4 import BeautifulSoup

base_url = requests.get("https://www.nytimes.com/2019/04/24/technology/facebook-ftc-fine-privacy.html?action=click&module=Top%20Stories&pgtype=Homepage")

# create a beautiful soup object

soup = BeautifulSoup(base_url.text, "html.parser")

# I am going to pull all the text from the body

headers_list = soup.find(class_="css-v89234")

# pull all the texts from the <p> tag within the div
headers_list_words = headers_list.find_all("p")


filename = input("File to save to:")
with open(filename,"w") as f:
    for words in headers_list_words:
        paragraphs = str(words.contents)
        f.write(paragraphs)


