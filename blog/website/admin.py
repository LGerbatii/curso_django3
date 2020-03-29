from django.contrib import admin
from .models import Post, Contact

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'full_name', 'categories', 'deleted']
    search_fields = ['title', 'subtitle', 'content']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
    search_fields = ['name', 'email', 'message']




    #def get_queryset(self, request):
    #  return Post.objects.filter(deleted=False)


admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
