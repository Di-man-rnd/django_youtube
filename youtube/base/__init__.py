import urllib

from html.parser import HTMLParser
from html.entities import name2codepoint


# def uplode_img(url):
#     urllib.request.urlretrieve(url, img)


class MyHTMLParser(HTMLParser):
    tag = []

    def handle_starttag(self, tag, attrs):
        if tag in ['a', 'img']:
            print("Start tag:", tag)
            self.tag.append(attrs)
            for attr in attrs:
                print("     attr:", attr)


parser = MyHTMLParser()
parser.feed('<img src="python-logo.png" alt="The Python logo">')
