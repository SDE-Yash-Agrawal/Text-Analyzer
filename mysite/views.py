  # i have created this file - Yash
from django.http import HttpResponse
from django.shortcuts import render

def new(request):
    return render(request, 'index.html')

def analyzed(request):
    djtext = request.GET.get('text', 'Default')
    value = request.GET.get('removepunc', 'off')
    charcount = request.GET.get('charcount', 'off')
    capitalize = request.GET.get("capital", 'off')
    newlineremover = request.GET.get('lineremove', 'off')
    spaceremover = request.GET.get('spaceremover', 'off')
    count = 0
    if value == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(charcount == 'on'):
        for char in djtext:
            if char == ' ':
                pass
            else:
                count += 1
        params = {'analyzed_text': count, 'texting': 'Characters in your text is '}
        return render(request, 'analyze.html', params)

    elif(capitalize == 'on'):
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (newlineremover == 'on'):
        analyzed = ''
        for char in djtext:
            if char !='\n':
                analyzed = analyzed + char
        params = {'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (spaceremover == 'on'):
        analyzed = ''
        for char in djtext:
            if char !=' ':
                analyzed = analyzed + char
        params = {'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')