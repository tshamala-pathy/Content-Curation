from django.contrib import admin
from .models import Portfolio, Subscription, Article_News, Stock

# Register your models here.
admin.site.register(Portfolio)
admin.site.register(Subscription)
admin.site.register(Article_News)
admin.site.register(Stock)