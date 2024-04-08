from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_dashboard, name='user_dashboard'),
    path('portfolios/', views.Create_Port_List.as_view(), name='portfolio_list'),
    path('subscriptions/', views.Create_Sub_List.as_view(), name='subscription_list'),
    path('news/', views.Create_N_A_List.as_view(), name='news_article_list'),
    path('stocks/', views.Create_Stock_Lis.as_view(), name='stock_list'),
    path('create_portfolio/', views.create_portfolio, name='create_portfolio'),
    path('create_subscription/', views.create_subscription, name='create_subscription'),
    path('create_news_article/', views.create_news_article, name='create_news_article'),
    path('create_stock/', views.create_stock, name='create_stock'),
]
