from django.db import models
from django.contrib.auth.models import User

class Portfolio(models.Model):
    """
    A model to represent a user's portfolio.
    
    Attributes:
        name (str): The name of the portfolio.
        user (User): The user who owns the portfolio.
    """

    name = models.CharField(max_length=70)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the portfolio."""
        return self.name  # Return the name of the portfolio as the string representation
    

class Subscription(models.Model):
    """
    A model to represent a user's subscription to a portfolio.
    Attributes:
        user (User): The user who is subscribing to the portfolio.
        portfolio (Portfolio): The portfolio being subscribed to.
        frequency (str): The frequency of updates for the subscription (daily or weekly).
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE)
    frequency = models.CharField(max_length=25, choices=[('daily', 'Daily'), ('weekly', 'Weekly')])

    def __str__(self):
        """Return a string representation of the subscription."""
        return f"{self.user.username} subscribed to {self.portfolio.name} ({self.frequency})"

class Article_News(models.Model):
    """
    A model to represent a news article.
    
    Attributes:
        title (str): The title of the article.
        content (str): The content of the article.
        source (str): The URL of the article source.
        time_created (DateTime): The time when the article was created.
        stocks (ManyToManyField): The stocks related to the news article.
    """
    title = models.CharField(max_length=300)
    content = models.TextField()
    source = models.URLField()
    time_created = models.DateTimeField(auto_now_add=True)
    stocks = models.ManyToManyField('Stock', related_name='news_articles')
    
    def __str__(self):
        """Return a string representation of the article."""
        return self.title

class Stock(models.Model):
    """
    A model to represent a stock.
    
    Attributes:
        symbol (str): The symbol of the stock.
        name (str): The name of the stock.
    """
    symbol = models.CharField(max_length=20)
    name = models.CharField(max_length=80)
    
    def __str__(self):
        """Return a string representation of the stock."""
        return self.symbol
