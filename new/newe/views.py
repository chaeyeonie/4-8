from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def results(request):
    wordcounts = request.GET['text']
    splittedtext = wordcounts.split()
    wordcount = len(splittedtext)
    a ={}
    for i in splittedtext:
        if i in a:
            a[i] += 1 
        else :
            a[i] = 1
    countedword = a.items()
    return render(request,'results.html', {
        'wordcount':wordcount,
        'countedword':countedword,
        'wordcounts' : wordcounts,
    })
