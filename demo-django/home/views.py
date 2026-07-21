from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from .models import Tag, Mensagem
from .forms import MensagemForm
from django.contrib import messages
# Create your views here.

def _aplicar_tags(mensagem, tags_texto):
    mensagem.tags.clear()
    for pedaco in tags_texto.split(","):
        nome = slugify(pedaco)
        if nome:
            tag, _ = Tag.objects.get_or_create(nome=nome)
            mensagem.tags.add(tag)

def index(request):
    mensagens = Mensagem.objects.all()
    return render(request, "home/index.html", {"mensagens": mensagens})

def sobre(request):
    return render(request, "home/sobre.html")

def nova_mensagem(request):
    if request.method == "POST":
        form = MensagemForm(request.POST)
        if form.is_valid():
            mensagem = form.save()

            #transforma o texto em objetos tag 
            tags_texto = form.cleaned_data["tags"]
            for pedaco in tags_texto.split(","):
                nome = slugify(pedaco)
                if nome:
                    tag, _ = Tag.objects.get_or_create(nome=nome)
                    mensagem.tags.add(tag)

            messages.success(request, "Mensagem publicada com sucesso!")
            return redirect("index")
    else:
        form = MensagemForm()
    
    return render(request, "home/nova.html", {"form": form})

def editar_mensagem(request, id):
    mensagem = get_object_or_404(Mensagem, id=id)

    if request.method == "POST":
        form = MensagemForm(request.POST, instance=mensagem)
        if form.is_valid():
            mensagem = form.save()
            _aplicar_tags(mensagem, form.cleaned_data["tags"])
            messages.success(request, "Mensagem atualizada com sucesso!")
            return redirect("index")
    else:
        tags_atuais = ", ".join(tag.nome for tag in mensagem.tags.all())
        form = MensagemForm(instance=mensagem, initial={"tags": tags_atuais})

    return render(request, "home/editar.html", {"form": form, "mensagem": mensagem})

def remover_mensagem(request, id):
    mensagem = get_object_or_404(Mensagem, id=id)

    if request.method == "POST":
        mensagem.delete()
        messages.success(request, "Mensagem removida.")
        return redirect("index")

    return render(request, "home/remover.html", {"mensagem": mensagem})
    