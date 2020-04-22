from django.urls import path
from . import views

urlpatterns = [
    path('accueil',views.home, name="accueil"),
    #path('article/<int:id_article>', views.view_article, name="voir_articles"),
    path('redirection', views.redirection, name="redirection_vers_articles"),

    path('date', views.date_actuelle, name="voir_date_actuelle"),
    path('addition', views.addition, name="voir_addition_1_1"),
    path('addition/<int:x>/<int:y>', views.addition, name="voir_addition_x_y"),
    path('bienvenue/<sexe>', views.bienvenue, name="acceuillir_le_visiteur"),

    path('', views.accueil, name="voir_accueil"),
    path('article/<int:id>-<slug:slug>$', views.lire, name="lire"),

    path('contact/', views.contact, name="contact")
]