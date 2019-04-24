# program to decode a webpage

# Use the BeautifulSoup and requests Python packages to print out a list of
# all the article titles on the New York Times homepage.


# First, install the requests library according to the official
# documentation and your operating system, then import the library into the program.
import requests
from bs4 import BeautifulSoup


# These lines make the request to the New York Times homepage.
# Making a request is simple, according to the documentation you
# supply a URL and make a GET request.

base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

# r.text returns all the html from the returned request
# BeautifulSoup is the tool we use to recode the HTML.
# Now that we know we are looking for all elements on the page
# with the class story-heading, so we need to find the
# documentation for how to do that, with special instructors for
#  how to do this for a class. We end up with:
# soup.find_all(class_="story-heading")
# This returns a list of all tags with story-heading as a class.
#  What we need to do is loop through all of them with a for loop
# and see what format the output is in.
# And then remove the text from the link and the title
# from the list of contents:


for story_heading in soup.find_all(class_="story-heading"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())

# The only thing missing is the formatting -
# if you scroll through the list of outputs,
# the formatting of some titles farther down the list.
# There are an excess of spaces, so stripping the strings
# and replacing all instances of new lines and tabs with regular spaces should do the trick.
# in the soup variable, you should use "html.parser"

