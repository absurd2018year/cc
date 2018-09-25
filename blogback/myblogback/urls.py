
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from myblogback import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'article/', login_required(views.article), name='article'),
    url(r'^add_article/', login_required(views.add_article), name='add_article')
]