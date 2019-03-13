from flask import Flask
import urllib.request, urllib.parse

link = 'https://calendar.ucsd.edu/search/category/talks-lectures'
html_doc = urllib.request.urlopen(link).read()

app = Flask(__name__)
@app.route("/")
def main_page():
    return html_doc
