

from django.urls import path
from meetings.views import detail, create, update, delete


urlpatterns = [
    # Detail sayfası için örnek bir url
    # http://127.0.0.1:8000/meeting/detail/1
    path('detail/<int:id>', detail, name='detail'),


    # http://127.0.0.1:8000/meeting/create/
    path('create', create, name='create'),

    # http://127.0.0.1:8000/meeting/update/1
    path('update/<int:id>', update, name='update'),

    # http://127.0.0.1:8000/meeting/delete/5
path('delete/<int:id>', delete, name='delete')
]