from django.shortcuts import render


from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def materiais(request):
    return render(request, 'materiais.html')

def como_funciona(request):
    return render(request, 'como_funciona.html')

def mapa(request):
    return render(request, 'mapa.html')

def contato(request):
    return render(request, 'contato.html')