from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Portfolio, Subscription, New_Article, Stock
from .serializers import PortfolioSerializer, SubscriptionSerializer, NewsArticleSerializer, StockSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PortfolioForm, SubscriptionForm, NewsArticleForm, StockForm


class Create_Port_List(generics.ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class Create_Sub_List(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class Create_N_A_List(generics.ListCreateAPIView):
    queryset = New_Article.objects.all()
    serializer_class = NewsArticleSerializer

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class Create_Stock_Lis(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@login_required
def user_dashboard(request):
    user = request.user

    portfolios = Portfolio.objects.filter(user=user)
    subscriptions = Subscription.objects.filter(user=user)
    news_articles = New_Article.objects.all()
    stocks = Stock.objects.all()

    portfolio_form = PortfolioForm()
    subscription_form = SubscriptionForm()
    new_article_form = NewsArticleForm()
    stock_form = StockForm()

    context = {
        'user': user,
        'portfolios': portfolios,
        'subscriptions': subscriptions,
        'news_articles': news_articles,
        'stocks': stocks,
        'portfolio_form': portfolio_form,
        'subscription_form': subscription_form,
        'new_article_form': new_article_form,
        'stock_form': stock_form,
    }

    return render(request, 'registre_v/dashboard.html', context)

@login_required
def create_portfolio(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = request.user
            portfolio.save()
            return redirect('user_dashboard')
    else:
        form = PortfolioForm()
    return render(request, 'registre_v/create_portfolio.html', {'form': form})

@login_required
def create_subscription(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save(commit=False)
            subscription.user = request.user
            subscription.save()
            return redirect('user_dashboard')
    else:
        form = SubscriptionForm()
    return render(request, 'registre_v/create_subscription.html', {'form': form})

@login_required
def create_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save()
            return redirect('user_dashboard')
    else:
        form = StockForm()
    return render(request, 'registre_v/create_stock.html', {'form': form})

@login_required
def create_news_article(request):
    if request.method == 'POST':
        form = NewsArticleForm(request.POST)
        if form.is_valid():
            news_article = form.save()
            return redirect('user_dashboard')
    else:
        form = NewsArticleForm()
    return render(request, 'registre_v/create_news_article.html', {'form': form})


