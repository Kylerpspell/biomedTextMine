participant = ""

path = '/Volumes/Crucial X6/ABC/ABCTools/biomedTextMine/participantTexts/'+participant+'.txt'
with open(path, 'r') as f:
	text = f.read()
	text = text.lower()
	text = text.split()
	wordFreq = {}
	for word in text:
		if word not in wordFreq:
			wordFreq[word] = 1
		else:
			wordFreq[word] += 1

	wordFreqs = []
	for key in wordFreq:
		wordFreqs.append([key, wordFreq[key]])

	wordFreqs.sort(key=lambda x: x[1], reverse=True)
	for pair in wordFreqs:
		print(pair[0], pair[1])


#walk through the directory and get all the files 

import os
totalFreqs = {}
path = '/Volumes/Crucial X6/ABC/ABCTools/biomedTextMine/participantTexts/'
files = os.listdir(path)
for file in files:
	with open(path+file, 'r') as g:
		text = g.read()
		text = text.lower()
		text = text.split()

		for word in text:
			if word not in totalFreqs:
				totalFreqs[word] = 1
			else:
				totalFreqs[word] += 1

listFreqs = []
for key in totalFreqs:
	listFreqs.append([key,totalFreqs[key]])

listFreqs.sort(key=lambda x: x[1], reverse=True)


import csv
with open('freqs.csv','w') as m:
	writer = csv.writer(m)
	writer.writerows(listFreqs)


commonWords = ['to', 'and', 'with', 'of', 'for', 'on', 'in', 'the', 'a', 'is', 'that', 'this', 'it', 'as', 'was', 'are', 'be', 'have', 'by', 'or', 'an', 'from', 'at', 'not', 'but', 'they', 'their', 'which', 'we', 'can']

for pair in listFreqs:
	if pair[0] not in commonWords:
		print(pair[0],',',pair[1], end="")