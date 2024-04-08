from django import forms
from .models import Portfolio, Subscription, New_Article, Stock

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['name']

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['portfolio', 'frequency']

class NewsArticleForm(forms.ModelForm):
    class Meta:
        model = New_Article
        fields = ['title', 'content', 'source', 'stocks']

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['symbol', 'name']
