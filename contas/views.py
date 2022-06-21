from django.shortcuts import render, redirect

from django.http import HttpResponse
from datetime import datetime

from .models import Transacao
from .forms import TransacaoForm

def home(request):
    """
    PAGINA HOME RETORNA A HORA ATUAL
    """

    # html = "<html><body>Quando são exactamente... %s.</body></html>" % agora
    # return HttpResponse(html)
    
    # DICIONARIO DE DADOS PARA RETORNO
    page_data = {}

    page_data["agora"] = datetime.now()
    page_data["nomes"] = ["Felix", "Paulo", "Adelson"]
    return render(request, "contas/home.html", page_data)

def listagem(request):
    """
    PAGINA PARA LISTAGEM DE TRANSAÇÕES
    """

    tran_data = {}
    tran_data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', tran_data)

def nova_transacao(request):
    """
    PAGINA DE NOVA TRANSAÇÃO COM FORM
    """

    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("url_listagem")
    

    return render(request, 'contas/form.html', {'form' : form})
