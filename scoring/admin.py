from django.contrib import admin
from .models import Tournament,Team,Match
# Register your models here.

admin.site.register(Tournament)
admin.site.register(Team)
admin.site.register(Match)