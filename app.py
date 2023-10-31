from flask import Flask, render_template, flash, url_for
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route('/select.html')
def select():
  imagelist = os.listdir(os.path.join(app.static_folder,"images"))
  return render_template("select.html", imagelist=imagelist)
  
@app.route('/share.html')  
def share():  
    return render_template('share.html')
  
@app.route('/versus.html')
def versus():
  return render_template("versus.html")
  
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)