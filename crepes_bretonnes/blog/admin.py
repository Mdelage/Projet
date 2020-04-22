from django.contrib import admin
from .models import Article, Categorie
from django.utils.text import Truncator

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date', 'apercu_contenu')
    list_filter = ('auteur', 'categorie',)
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('titre', 'contenu')
    prepopulated_fields = { 'slug' : ('titre',), }

    fieldsets = (
        #Fieldset 1 : Méta-info
        ('Général', {
            'classes' : ['collapse',],
            'fields' : ('titre', 'slug', 'auteur', 'categorie','date',),
         }),
        #Fieldset 2 : contenu
        ('Contenu de l\'article', {
            'description' : 'Le formulaire accepte les balises HTML, utilisez-les à bon escient!',
            'fields' : ('contenu',),
        }),
    )

    def apercu_contenu(self, article):
        return Truncator(article.contenu).chars(30, truncate="...")

    apercu_contenu.short_description = "Aperçu du contenu"

admin.site.register(Article, ArticleAdmin)
admin.site.register(Categorie)