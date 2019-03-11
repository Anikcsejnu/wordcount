from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	return render(request, 'home.html', {'hithere':'this is Anik'})
def about(request):
	return render(request, 'about.html')

def count(request):

	fulltext = request.GET['fulltext']

	wordcount = fulltext.split()

	wordDictionary = {}

	for word in wordcount:
		if word in wordDictionary:
			wordDictionary[word] += 1
		else:
			wordDictionary[word] = 1

	sortedWord = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)


		




	return render(request, 'count.html', {'fulltext': fulltext, 'wordcount': len(wordcount), 

	'sortedWord': sortedWord})

