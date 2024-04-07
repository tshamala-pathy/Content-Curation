from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Portfolio, Subscription, New_Article, Stock
from .serializers import PortfolioSerializer, SubscriptionSerializer, NewsArticleSerializer, StockSerializer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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

    context = {
        'user': user,
        'portfolios': portfolios,
        'subscriptions': subscriptions,
        'news_articles': news_articles,
        'stocks': stocks,
    }

    return render(request, 'registre_v/dashboard.html', context)

