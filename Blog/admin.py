from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import post, Comment

#Adding summernote editor to text in post
class Summer(SummernoteModelAdmin):
    summernote_fields = ('content')
# Register your models here.

admin.site.register(post,Summer)
admin.site.register(Comment)