from django.contrib import admin
from .models import Movie,Category,Rate,Country


class MoviesInline(admin.StackedInline):
    model = Movie
    extra=1
    max_num=5
class CountryAdmin(admin.ModelAdmin):
    inlines = [MoviesInline]

class MovieAdmin(admin.ModelAdmin):
    list_display = ("title","overview","year")
    list_filter = ("year",)

# Register your models here.
admin.site.register(Movie,MovieAdmin)
admin.site.register(Category)
admin.site.register(Rate)
admin.site.register(Country,CountryAdmin)


     

