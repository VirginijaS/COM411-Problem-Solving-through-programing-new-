import csv
with open("fold1/fold2/data.csv") as d:
  reader = csv.reader(d,delimiter = ",", quotechar = "'")
  for row in reader:
    