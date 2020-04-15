from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()

    results = dict()
    for word in words:
        if word in results.keys():
            results[word] += 1
        else:
            results[word] = 1
    results = sorted(results.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'words': len(words), 'results': results})


def clear(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')
