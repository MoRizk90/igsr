from django import forms
from igss_app.models import MeetingAgenda, Items, Actions

class NewAgendaForm(forms.ModelForm):

    class Meta():
        model = MeetingAgenda
        fields = '__all__'


class NewItemForm(forms.ModelForm):

    class Meta():
        model = Items
        fields = '__all__'


class UpdatediTemActionForm(forms.ModelForm):

    class Meta():
        model = Items
        fields = '__all__'



class NewActionsForm(forms.ModelForm):

    class Meta():
        model = Actions
        fields = '__all__'