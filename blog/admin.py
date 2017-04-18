from django.contrib import admin
from .models import Post

admin.site.register(Post) # pour qu’il soit visible dans notre interface d’admin
