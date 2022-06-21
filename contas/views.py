from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from datetime import datetime

def home(request):
    """
    PAGNA HOME RETORNA A HORA ATUAL
    """

    # html = "<html><body>Quando são exactamente... %s.</body></html>" % agora
    # return HttpResponse(html)
    
    # DICIONARIO DE DADOS PARA RETORNO
    page_data = {}

    page_data["agora"] = datetime.now()
    page_data["nomes"] = ["Felix", "Paulo", "Adelson"]
    return render(request, "contas/home.html", page_data)