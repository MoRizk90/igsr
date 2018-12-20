from django.contrib import admin
from igss_app.models import IgsrUser, MeetingAgenda,Users_type,Deparments,Agenda_State,Items,Actions
# Register your models here.

admin.site.register(IgsrUser)
admin.site.register(MeetingAgenda)
admin.site.register(Users_type)
admin.site.register(Deparments)
admin.site.register(Agenda_State)
admin.site.register(Items)
admin.site.register(Actions)
