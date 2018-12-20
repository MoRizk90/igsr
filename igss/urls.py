"""igss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from igss_app import views
# from django.contrib.auth.views import login
admin.site.site_header = 'IGSSR MEETINGS ADMIN'                    # default: "Django Administration"
admin.site.index_title = 'Features area'                 # default: "Site administration"
admin.site.site_title = 'HTML title from adminsitration '

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.user_login, name='user_login'),
    path('index', views.index, name='index'),
    path('logout', views.user_logout, name='logout'),
    path('addAgenda', views.add_agenda_func, name='addAgenda'),
    path('viewAgenda', views.get_agenda, name='viewAgenda'),
    path('addItems', views.add_Item_func, name='addItems'),
    path('items/<agendaId>', views.get_Items, name='items'),
    path('FindAgenda', views.agend_search, name='FindAgenda'),
    path('goToAgendaSearch', views.go_agend_search, name='goToAgendaSearch'),
    path('agendaAction', views.agenda_action, name='agendaAction'),
    path('itemsaction/<agendaId>', views.item_action, name='itemaction'),
    path('actionUpdate/<itemId>', views.item_action_update, name='actionUpdate'),
]
