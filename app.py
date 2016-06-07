from flask import Flask, render_template, request


app = Flask(__name__)

# Home page
@app.route("/")
def home():
  template = 'index.html'
  return render_template(template)

# Results page
@app.route("/results")
def results():
  template = 'results.html'
  return render_template(template)

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)