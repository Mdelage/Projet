
from django.http import HttpResponse, Http404
from django.shortcuts import redirect

from django.shortcuts import render, get_object_or_404
from datetime import datetime

from blog.models import Article

from .forms import ContactForm

# Create your views here.

def home(request):
    return HttpResponse("""
        <h1>Bienvenue!</h1>
        <p>Comment allez-vous?</p>
    """)

def view_article(request, id_article=1):
    if id_article > 100:
        raise Http404

    return HttpResponse(
        "Vous avez demandé l'article {0}".format(id_article)
    )

def redirection(request):
    return redirect("voir_articles", id_article=2)


def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def addition(request, x=1 , y=1):
    total = x + y

    return render(request, 'blog/addition.html', locals())

def bienvenue(request, sexe):
    couleurs_dico = {
        'FF0000': 'rouge',
        'ED7F10': 'orange',
        'FFFF00': 'jaune',
        '00FF00': 'vert',
        '0000FF': 'bleu',
        '4B0082': 'indigo',
        '660099': 'violet',
    }

    iterable_chiffre = [i for i in range(10)]

    return render(request, 'blog/bienvenue.html', locals())

def accueil(request):
    articles = Article.objects.all()

    return render(request, "blog/accueil.html", {"dernier_articles": articles})

def lire(request, id, slug):
    # try:
    #     article = Article.objects.get(id = id)
    # except Article.DoesNotExist:
    #     raise Http404

    article = get_object_or_404(Article, id=id, slug=slug)

    return render(request, "blog/lire.html", locals())

def contact(request):
    #Construction du formulaire
    form = ContactForm(request.POST or None)

    #vérification que les données sont valides
    if form.is_valid():
        #traitement des champs du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        #Ici, on pourrait envoyer l'email
        envoi = True

    return render(request, "blog/contact.html", locals())