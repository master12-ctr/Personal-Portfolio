from django.contrib import admin
from .models import experience, certificates, education, skills, languages

admin.site.register(experience)
admin.site.register(certificates)
admin.site.register(education)
admin.site.register(skills)
admin.site.register(languages)