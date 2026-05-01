from django.urls import path
from .views import (
                    home,
                    about,
                    create_article,
                    article_view,
                    update_article,
                    delete_article,
                    article_detail
                    )

urlpatterns = [
    path('home/',home,name='blog-home'),
    path('articles/', article_view, name='article-view'),
    path('about/',about),
    path('create-article/',create_article,name = 'create-article'),
    path('update-article/<int:id>/',update_article,name = 'update-article'),
    path('delete-article/<int:id>/',delete_article,name = 'delete-article'),
    path('article-detail/<int:id>/',article_detail,name = 'article-detail')


    #careers 
    #newsletter
]