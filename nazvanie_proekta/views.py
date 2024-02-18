from django.http import HttpResponse
from django.shortcuts import render


def first_page(request):
    a = 'Привет, хуй'
    text = 'new text'
    return render(request, './index.html', {
        'a': a,
        'text': text}
    )
