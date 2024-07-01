from django.contrib import admin
from .models import Contact, Document
# Register your models here.
import os
from django.conf import settings
admin.site.register(Contact)

class DocumentAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Remove all existing PDF files
        pdf_dir = os.path.join(settings.MEDIA_ROOT, 'static/pdf/')
        for filename in os.listdir(pdf_dir):
            if filename.endswith('.pdf'):
                pdf_path = os.path.join(pdf_dir, filename)
                os.remove(pdf_path)

        # Save the new PDF file with the name "tadecv.pdf"
        obj.pdf_file.name = 'tadecv.pdf'

        obj.save()

admin.site.register(Document, DocumentAdmin)