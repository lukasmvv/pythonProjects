import csv

with open('test.csv', 'w', newline='') as csvfile:
	csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	csvwriter.writerow('[1 2 3]')