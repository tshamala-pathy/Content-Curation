from django.contrib import admin
from .models import Portfolio, Subscription, New_Article, Stock

# Register your models here.
admin.site.register(Portfolio)
admin.site.register(Subscription)
admin.site.register(New_Article)
admin.site.register(Stock)