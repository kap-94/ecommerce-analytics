from django.contrib import admin
from .models import WebsitePageviews, WebsiteSessions

# Register your models here.

admin.site.register([WebsitePageviews, WebsiteSessions])
