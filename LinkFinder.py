from html.parser import HTMLParser
from urllib import parse
class LinkFinder(HTMLParser):
    def __init__(self):
        super().__init__()

    def handle_starttag(self, tag, attrs):
        print(f"Start tag: {tag}")

    def error(self, message):
        pass

finder = LinkFinder()
finder.feed('<html><head><title>test</title></head>'
            '<body><h1>parse me</h1></body></html>')