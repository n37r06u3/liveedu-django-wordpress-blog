from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import WpCommentmeta, WpComments, WpLinks, WpOptions, WpPostmeta, WpPosts, WpTermmeta, \
    WpTermRelationships, WpTerms, WpTermTaxonomy, WpUsermeta, WpUsers

admin.site.register(WpCommentmeta)
admin.site.register(WpComments)
admin.site.register(WpLinks)
admin.site.register(WpOptions)
admin.site.register(WpPostmeta)
admin.site.register(WpTermmeta)
admin.site.register(WpTermRelationships)
admin.site.register(WpTerms)
admin.site.register(WpTermTaxonomy)
admin.site.register(WpUsermeta)
admin.site.register(WpUsers)

from django import forms
from django.contrib import admin



class PostAdminForm(forms.ModelForm):
    post_content = forms.CharField(widget=CKEditorUploadingWidget())
    post_password = forms.CharField(required=False)
    post_excerpt = forms.CharField(required=False)
    to_ping = forms.CharField(required=False)
    pinged = forms.CharField(required=False)
    post_content_filtered = forms.CharField(required=False)
    post_mime_type = forms.CharField(required=False)
    class Meta:
        model = WpPosts
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(WpPosts, PostAdmin)