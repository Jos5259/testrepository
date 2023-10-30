from flask import Flask, render_template, flash

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route('/select.html')
def select():
  return render_template("select.html")
  

@app.route('/versus.html')
def versus():
  return render_template("versus.html")
  
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)