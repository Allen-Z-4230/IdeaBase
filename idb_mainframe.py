from flask import Flask, render_template
import urllib.request, urllib.parse

link = 'https://calendar.ucsd.edu/search/category/talks-lectures'
html_doc = urllib.request.urlopen(link).read()

app = Flask(__name__)
@app.route("/")
@app.route("/home")
def main_page():
    return render_template('base.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
