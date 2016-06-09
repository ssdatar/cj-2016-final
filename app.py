from flask import Flask, render_template, request
import csv


app = Flask(__name__)

def get_data():
  with open('static/data/master-2.csv', 'r') as r:
    data = list(csv.DictReader(r))
  return data

# Return data based on parameters chosen
def get_filtered_data(data, filters):
  f1 = data

  if filters[0] != 'all': 
    f1 = [d for d in data if d['county'] == filters[0]]
  
  if filters[1] != 'all':
    f1 = [e for e in f1 if e['category'] == filters[1]]
  
  if filters[2] != 'all':
    f1 = [r for r in f1 if r['ethnicity'].lower() == filters[2]]

  if filters[3] != 'all':
    f1 = [r for r in f1 if r['gender'].lower() == filters[3]]
  return f1



# Home page
@app.route("/")
def home():
  template = 'index.html'

  with open('static/data/offender.csv', 'r') as r:
    off = list(csv.DictReader(r))
  return render_template(template, o=off)



# Results page
@app.route("/results")
def results():
  with open('static/data/county_income.csv', 'r') as r:
    counties = list(csv.DictReader(r))
  args = request.args
  _county = request.args.get('county').lower()
  _categ = request.args.get('categ-name')
  _race = request.args.get('ethnicity')
  _sex = request.args.get('sex')

  filters = [_county, _categ, _race, _sex]

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
    row['Description'] = row['Description'].lower().capitalize()

  template = 'results.html'
  return render_template(template, results=filtered_data, f=filters, c=counties, county=_county)

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)