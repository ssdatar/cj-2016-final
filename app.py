from flask import Flask, render_template, request
import csv


app = Flask(__name__)

def get_data():
  with open('static/data/data.csv', 'r') as r:
    data = list(csv.DictReader(r))
  return data

def get_filtered_data(data, filters):
  temp = data
  filters = filters
  f1 = [d for d in temp if d['county'] == filters[0]]
  
  if filters[1] != 'all':
    f1 = [d for d in f1 if d['category'] == filters[1]]
  
  if filters[2] != 'all':
    f1 = [r for r in f1 if r['ethnicity'] == filters[2]]
  return f1



# Home page
@app.route("/")
def home():
  template = 'index.html'
  return render_template(template)

# Results page
@app.route("/results")
def results():
  args = request.args
  _county = request.args.get('county')
  _categ = request.args.get('categ-name')
  _race = request.args.get('ethnicity')

  filters = [_county,_categ,_race]

  if not _county:
    return """
            <h1>Error</h1>
            <p>Must have either a state abbreviation or zipcode value</p>
            <p>Go <a href="{url}">back</a></p>
        """.format(url=request.referrer)

  else:
    data = get_data()
    filtered_data = get_filtered_data(data, filters)
  for row in filtered_data:
    if not row['lat']:
      row['lat'] = 0.0
    if not row['lon']:
      row['lon'] = 0.0
    row['offense_desc'] = row['offense_desc'].lower().capitalize()

  template = 'results.html'
  return render_template(template, results=filtered_data, f=filters)

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)