from django.contrib import admin

from .models import TodoItem
from .models import House
from .models import Post
admin.site.register(TodoItem)
admin.site.register(House)
admin.site.register(Post)
