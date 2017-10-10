from django.contrib import admin
from .models import Post
from .models import Link

admin.site.register(Post)
admin.site.register(Link)