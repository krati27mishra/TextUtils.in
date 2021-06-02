#I have created this file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')


def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    uppercase=request.POST.get('uppercase','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')
    if(removepunc=="on"):
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char

        params={'purpose':'Remove Punctuations','analyzed_text':analyzed}
        djtext=analyzed

    if(uppercase=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Convert to Upper Case','analyzed_text':analyzed}
        djtext=analyzed

    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed=analyzed+char

        print("pre",analyzed)
        params={'purpose':'Remove New Line','analyzed_text':analyzed}
        djtext=analyzed

    if(extraspaceremover=="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if djtext[index] ==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed=analyzed+char
        params={'purpose':'Remove Extra Space','analyzed_text':analyzed}
        djtext=analyzed

    if(charcount=="on"):
        c=0
        analyzed=""
        for char in djtext:
            c=c+1

        params={'purpose':'Character Counter','analyzed_text':analyzed}


    if(removepunc!="on" and uppercase!="on" and newlineremover!="on" and extraspaceremover=="on" and charcount=="on"):
        return HttpResponse("Please select any operation")


    return render(request,'analyze.html',params)
