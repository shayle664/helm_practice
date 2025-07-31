from flask import Flask, render_template
import platform

app = Flask(__name__)

def get_os():
    return platform.system()

@app.route('/')
def home():
    os_name = get_os()
    return render_template("index.html", os_name=os_name)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/category')
def category():
    return render_template("category.html")

@app.route('/work')
def work():
    return render_template("work.html")

if __name__ == '__main__':
    app.run(debug=True)