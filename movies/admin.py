from django.contrib import admin

from movies.models import Director, Movie

# Register your models here.

admin.site.register(Director)
admin.site.register(Movie)
