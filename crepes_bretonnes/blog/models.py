from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):

    titre = models.CharField(max_length=80)
    slug = models.SlugField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "article"
        ordering = ['date']

    def __str__(self):
        return "{0}, par {1}".format(self.titre, self.auteur)

class Categorie(models.Model):
    nom = models.CharField(max_length=30, default="non_categorise")

    def __str__(self):
        return self.nom

class Voiture(models.Model):
    nom = models.CharField(max_length=30, default="Renault")
    moteur = models.OneToOneField('Moteur', on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Moteur(models.Model):
    nom = models.CharField(max_length=30, default="Turbofan")

    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=30, default="Pâtes")

    def __str__(self):
        return self.nom

class Vendeur(models.Model):
    nom = models.CharField(max_length=30, default="Amazon")
    produits = models.ManyToManyField('Produit', through="Offre", related_name='+')

    produits_sans_prix = models.ManyToManyField('Produit', related_name="Vendeur")

    def __str__(self):
        return self.nom

class Offre(models.Model):
    prix = models.IntegerField()
    produit = models.ForeignKey('Produit', on_delete=models.CASCADE)
    vendeur = models.ForeignKey('Vendeur', on_delete=models.CASCADE)

    def __str__(self):
        return "{0} vendu par {1}".format(self.produit, self.vendeur)