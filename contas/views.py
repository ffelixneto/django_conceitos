from django.shortcuts import render, redirect

from django.http import HttpResponse
from datetime import datetime

from .models import Transacao
from .forms import TransacaoForm

def home(request):
    """
    VIEW HOME EXIBE A HORA ATUAL
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
    VIEW PARA LISTAGEM DE TRANSAÇÕES
    """

    tran_data = {}
    tran_data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', tran_data)

def nova_transacao(request):
    """
    VIEW DE NOVA TRANSAÇÃO COM FORM
    """

    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("url_listagem")
    

    return render(request, 'contas/form.html', {'form' : form})

def update(request, pkey):
    """
    VIEW PARA UPDATE DE TRASAÇÕES
    """
    data = {}
    transacao = Transacao.objects.get(pk=pkey)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    
    data['form'] = form
    data['transacao'] = transacao
    return render(request, 'contas/form.html', data)

def delete(request, pkey):
    """
    VIEW PARA DELETE DE TRASAÇÕES
    """

    transacao = Transacao.objects.get(pk=pkey)
    transacao.delete()
    return redirect('url_listagem')
    
    
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
    
    data['form'] = form
    return render(request, 'contas/form.html', data)
