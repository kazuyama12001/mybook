from django.urls import path
from cms import views

app_name = 'cms'
urlpatterns = [
    # 書籍
    path('book/', views.book_list, name='book_list'),   # 一覧
    path('create/', views.create, name='create'),   # 一覧
    path('update/<int:num>', views.update, name='update'),
    path('delete/<int:num>', views.delete, name='delete'),
]