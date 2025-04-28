from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='html', static_folder='styles')

@app.route('/')
def home():
  return render_template('main.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/eduxp')
def eduxp():
  return render_template('eduxp.html')

@app.route('/porto')
def porto():
  return render_template('porto.html')

if __name__ == '__main__':
  app.run(debug=True, port=5555)