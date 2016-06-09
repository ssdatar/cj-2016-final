import csv
from datetime import date, datetime
from os.path import join

# http://stackoverflow.com/questions/2217488/age-from-birthdate-in-python
def calculate_age(born):
  today = date.today()
  return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

with open('../static/data/master.csv', 'r') as m:
  datarows = list(csv.DictReader(m))
  # Loop through each data row to add the age variable
  for row in datarows:
    row['county'] = row['county'].lower()
    d = datetime.strptime(row['dob'], '%m-%d-%Y')
    temp = calculate_age(d)
    row['age'] = temp

    # Add age category variable
    if temp < 18:
      row['category'] = 'Minor'
    elif temp >= 18 and temp < 40:
      row['category'] = 'Young'
    elif temp >= 40 and temp < 55:
      row['category'] = 'Middle age'
    else:
      row['category'] = 'Old'

    # Add compliance variable
    if not row['violation_date']:
      row['compliance_status'] = 'Compliant'
    else:
      row['compliance_status'] = 'In violation'


# After we are done adding, write a new csv file with the new categories
headers = datarows[0].keys()
with open('../static/data/master-2.csv', 'w') as w:
  writer = csv.DictWriter(w, fieldnames=headers)
  writer.writeheader()
  for row in datarows:
    writer.writerow(row)