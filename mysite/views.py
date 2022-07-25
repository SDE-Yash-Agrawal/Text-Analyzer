  # i have created this file - Yash
from django.http import HttpResponse
from django.shortcuts import render

def new(request):
    return render(request, 'index.html')

def analyzed(request):
    global params, analyzed, count
    djtext = request.POST.get('text', 'Default')
    value = request.POST.get('removepunc', 'off')
    charcount = request.POST.get('charcount', 'off')
    capitalize = request.POST.get("capital", 'off')
    newlineremover = request.POST.get('lineremove', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    count = 0
    if value == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'analyzed_text': analyzed}
        djtext = analyzed

    if(charcount == 'on'):
        for char in djtext:
            if char == ' ':
                pass
            else:
                count += 1
        params = {'analyzed_text': count, 'texting': 'Characters in your text is '}
        djtext = analyzed

    if(capitalize == 'on'):
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == 'on'):
        analyzed = ''
        for char in djtext:
            if char !='\n' and char !="\r":
                analyzed = analyzed + char
        params = {'analyzed_text': analyzed}
        djtext = analyzed

    if (spaceremover == 'on'):
        analyzed = ''
        for char in djtext:
            if char !=' ':
                analyzed = analyzed + char
        params = {'analyzed_text': analyzed}
        djtext = analyzed

    if(spaceremover !="on" and newlineremover !="on" and capitalize != 'on' and charcount != 'on' and value != 'on'):
        return HttpResponse("Error!! You haven't choose any function, Try again!")

    if(djtext == ''):
        return HttpResponse("Error!, You haven't enter any text...")

    return render(request, 'analyze.html', params)
def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')