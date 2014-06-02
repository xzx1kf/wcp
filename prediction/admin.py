from django.contrib import admin
from prediction.models import Team, Match, Result, Prediction

# Register your models here.
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Result)
admin.site.register(Prediction)
