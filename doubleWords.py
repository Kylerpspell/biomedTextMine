import os
commonWords = ['to', 'and', 'with', 'of', 'for', 'on', 'in', 'the', 'a', 'is', 'that', 'this', 'it', 'as', 'was', 'are', 'be', 'have', 'by', 'or', 'an', 'from', 'at', 'not', 'but', 'they', 'their', 'which', 'we', 'can']

def createCourpus():
	"""Creates a corpus from the participant texts folder."""

	corpus = []
	for filename in os.listdir('biomedTextMine/participantTexts/'):
		if filename.endswith('.txt'):
			with open('biomedTextMine/participantTexts/' + filename, 'r') as f:
				data = f.read()
				data = data.split('.')
				for sentence in data:
					corpus.append(sentence)
	return corpus


def searchCorpus(corpus, word):
	"""Searches the corpus for a word and returns a list of sentences containing the word."""
	
	sentences = []
	for sentence in corpus:
		if word in sentence:
			sentences.append(sentence)
	return sentences


def findCloseWords(word, corpus):
	"""Finds words that are used in proximity to the word in the corpus."""

	proxWords = {}
	for sentence in searchCorpus(corpus, word):
		sentence = sentence.split()
		try:
			for i in range(len(sentence)):
				if sentence[i] == word:
					if sentence[i-1] not in proxWords:
						proxWords[sentence[i-1]] = 1
					else:
						proxWords[sentence[i-1]] += 1
					if sentence[i+1] not in proxWords:
						proxWords[sentence[i+1]] = 1
					else:
						proxWords[sentence[i+1]] += 1
		except IndexError:
			pass
	return proxWords


if __name__ == '__main__':
	import csv
	corpus = createCourpus()

	with open('biomedTextMine/pairedFreqs.csv','w') as g:
		writer = csv.writer(g)

		with open('biomedTextMine/freqs.csv','r') as f:
			reader = csv.reader(f)
			freqs = list(reader)

			for word in freqs:
				freq = int(word[1])
				word = word[0]
				if word not in commonWords and freq > 10:
					proxWords = findCloseWords(word, corpus)
					proxWords = sorted(proxWords.items(), key=lambda x: x[1], reverse=True)
					writerow = [word] + proxWords
					writer.writerow(writerow)

					
				


