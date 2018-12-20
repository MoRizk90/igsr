from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from igss_app.forms import NewAgendaForm, NewItemForm, NewActionsForm
from igss_app.models import MeetingAgenda, Items, Agenda_State, Actions
from django.db.models import Q
from django.shortcuts import get_object_or_404

# Create your views here.


def get_Items(request, agendaId):

    items = Items.objects.filter(Agenda_id=agendaId)
    item_dict = {'Items_rec':items}
    return render(request, 'items.html', context=item_dict)


def get_agenda(request):
    agendas = MeetingAgenda.objects.order_by('Agenda_date')
    agenda_dict = {'agenda_recoreds': agendas}
    return render(request, 'viewAgenda.html', context=agenda_dict)


def index(request):
    return render(request, 'index.html')


def login(request):
    my_dict = {'insert_me': 'this is what was inserted'}
    return render(request, 'login.html', context=my_dict)




@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        # print(user.is_authenticated)
        if user:
            if user.is_active:
                login(request)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("This account is not active")
        else:
            print("someone tried to login and failed ")
            return HttpResponse("Invaild login")
    else:
        return render(request,'login.html')


def add_agenda_view(request):
    return render(request, 'addAgenda.html')



def display_agenda_view(request):
    return render(request, 'viewAgenda.html')


def add_agenda_func(request):

    form = NewAgendaForm()

    if request.method == 'POST':
        form = NewAgendaForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FROM INVALID")

    return render(request, 'addAgenda.html',{'form':form})


def add_Item_func(request):

    item_form = NewItemForm()

    if request.method == 'POST':
        item_form = NewItemForm(request.POST)

        if item_form.is_valid():
            item_form.save(commit=True)
            return index(request)
        else:
            print("ERROR FROM INVALID")

    return render(request, 'addItems.html', {'item_form': item_form})


def agend_search(request):
    query = request.GET.get('q')
    print(query)
    results = MeetingAgenda.objects.filter(Q(agenda_title__icontains=query))
    print(results)
    # fContext=list(results)
    results_dict = {'agenda_results': results}
    return render(request, 'FindAgenda.html', results_dict)


def go_agend_search(request):
    return render(request, 'goToAgendaSearch.html')


def agenda_action(request):
    action_result = MeetingAgenda.objects.filter(Q(agenda_state_Id=1))
    action_result_dict = {'action_results': action_result}
    return render(request, 'agendaActoms.html', action_result_dict)


def item_action(request, agendaId):

    state = Actions.objects.all()
    items = Items.objects.filter(Agenda_id=agendaId)
    item_dict = {'Items_rec': items}
    state_dict = {'state_rec': state}
    all_dict = {'item_dict': item_dict, 'state_dict': state_dict}
    return render(request, 'itemActions.html', all_dict)


def item_action_update(request, itemId):

    instance = get_object_or_404(Items, Item_id=int(itemId))
    # instance = Items.objects.filter(Item_id=itemId)
    form = NewItemForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        state = Actions.objects.all()
        item_agenda_id = instance.Agenda_id
        print(item_agenda_id)
        items = Items.objects.filter(Agenda_id=item_agenda_id)
        item_dict = {'Items_rec': items}
        state_dict = {'state_rec': state}
        all_dict = {'item_dict': item_dict, 'state_dict': state_dict}
        return render(request, 'itemActions.html', all_dict)

    return render(request, 'updateActions.html', {'item_form': form})









