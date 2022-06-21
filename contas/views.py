from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from datetime import datetime

def home(request):
    '''
    PAGNA HOME RETORNA A HORA ATUAL
    '''
    agora =  datetime.now()
    html = "<html><body>Quando são exactamente... %s.</body></html>" % agora
    # return HttpResponse(html)

    return render(request, 'contas/home.html')