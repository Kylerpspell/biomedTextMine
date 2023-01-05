import csv

with open('/Volumes/Crucial X6/ABC/ABCTools/biomedTextMine/KylerData.csv','r') as f:
	reader = csv.reader(f)
	data = list(reader)
	
	patients = []

	for row in data:
		name = row[0].lower()
		if name not in patients:
			patients.append(name)
	
	for patient in patients:
		with open('/Volumes/Crucial X6/ABC/ABCTools/biomedTextMine/participantTexts/' + patient + '.txt', 'a') as g:
			for row in data:
				if row[0].lower() == patient:
					g.write(row[1] + " " + row [2] + " " + row[3] + " " + row[4] + " "+ row[5] + " " + row[6] + "\n" + row[7] + "\n")