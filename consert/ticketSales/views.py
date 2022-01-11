from django.shortcuts import render, get_object_or_404, redirect

from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def consertList(request):
    context = {
        "conserts": Consert.objects.all(),
    }
    return render(request, 'ticketSales/consert_list.html', context=context)


def consertDetail(request, pk):
    consert = get_object_or_404(Consert, pk=pk)
    user_favorites = Favorite(consert=consert, user=request.user)

    if user_favorites:
        has_consert_favorite = True
    else:
        has_consert_favorite = False

    context = {
        "consert": consert,
        "has_consert_favorite": has_consert_favorite,
    }
    return render(request, 'ticketSales/consert_detail.html', context=context)


def timeConsertList(request):
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        consert_name = searchForm.cleaned_data['consert_name']
        # therefore model__ForeignKeyModel__fields
        timeConserts = TimeConsert.objects.filter(
            consert__name__contains=consert_name)

    else:
        timeConserts = TimeConsert.objects.all()
    context = {
        "TimeConserts": timeConserts,
        "searchForm": searchForm
    }

    return render(request, 'ticketSales/timeConsert_list.html', context=context)


def timeConsertDetail(request, pk):
    context = {
        'consert': get_object_or_404(TimeConsert, pk=pk)
    }
    return render(request, 'ticketSales/timeConsert_detail.html', context=context)


def consertEditView(request, pk):
    if request.user.is_superuser or request.user.is_stuff:
        consert = get_object_or_404(Consert, pk=pk)

        if request.method == "POST":
            # edit with django forms
            # request.POST for bind data
            # request.FILES for bind files , img and etc
            consertForm = ConsertForm(
                request.POST, request.FILES, instance=consert)

            if consertForm.is_valid:
                consertForm.save()

                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))

                else:
                    return redirect('ticketSales:consert-detail', pk=pk)
            else:
                messages.error('data is invalid')
                return redirect('ticketSales:consert-edit', pk=pk)
        else:
            # for inputs fill with previous values we can write inputs by hands(and fill value attribute)!! or better
            # way use django forms ->
            # instance=consert => fill previous value for inputs
            consertForm = ConsertForm(instance=consert)

            context = {
                'consertForm': consertForm,
                'consert': consert,
            }
            return render(request, 'ticketSales/consert_edit.html', context=context)
    else:
        messages.error('access dinied')

        if request.GET.get('next'):
            return redirect(request.GET.get('next'))

        else:
            return redirect('ticketSales:consert-list')


def locationEditView(request, pk):
    if request.user.is_superuser or request.user.is_stuff:
        location = get_object_or_404(Location, pk=pk)

        if request.method == "POST":
            # edit with django forms
            # request.POST for bind data
            # request.FILES for bind files , img and etc
            locationForm = LocationForm(request.POST, instance=location)

            if locationForm.is_valid:
                locationForm.save()

                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))

                else:
                    return redirect('ticketSales:consert-detail', pk=location.timeLocation.pk)
            else:
                messages.error('data is invalid')
                return redirect('ticketSales:location-edit', pk=pk)
        else:
            # for inputs fill with previous values we can write inputs by hands(and fill value attribute)!! or better
            # way use django forms ->
            # instance=consert => fill previous value for inputs
            locationForm = LocationForm(instance=location)

            context = {
                'locationForm': locationForm,
                'location': location,
            }
            return render(request, 'ticketSales/location_edit.html', context=context)
    else:
        messages.error('access dinied')

        if request.GET.get('next'):
            return redirect(request.GET.get('next'))

        else:
            return redirect('ticketSales:consert-list')


def timeConsertEditView(request, pk):
    if request.user.is_superuser or request.user.is_stuff:
        timeConsert = get_object_or_404(TimeConsert, pk=pk)

        if request.method == "POST":
            # edit with django forms
            # request.POST for bind data
            # request.FILES for bind files , img and etc
            timeConsertForm = TimeConsertForm(
                request.POST, instance=timeConsert)

            if timeConsertForm.is_valid:
                timeConsertForm.save()

                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))

                else:
                    return redirect('ticketSales:consert-detail', pk=pk)
            else:
                messages.error('data is invalid')
                return redirect('ticketSales:timeConsert-edit', pk=pk)
        else:
            # for inputs fill with previous values we can write inputs by hands(and fill value attribute)!! or better
            # way use django forms ->
            # instance=consert => fill previous value for inputs
            timeConsertForm = ConsertForm(instance=timeConsert)

            context = {
                'timeConsertForm': timeConsertForm,
                'timeConsert': timeConsert,
            }
            return render(request, 'ticketSales/timeConsert_edit.html', context=context)
    else:
        messages.error('access dinied')

        if request.GET.get('next'):
            return redirect(request.GET.get('next'))

        else:
            return redirect('ticketSales:consert-list')


@login_required
def addToFavorites(request, pk):
    favorite, created = Favorite.objects.update_or_create(
        user=request.user, consert=get_object_or_404(Consert, pk=pk))

    if created:
        messages.error(request, 'add successfully')
    else:
        messages.error(request, "previously added")

    if request.GET.get('next'):
        return redirect(request.GET.get('next'))

    context = {
        "consert": get_object_or_404(Consert, pk=pk)
    }
    return render(request, 'ticketSales/consert_detail.html ', context=context)


@login_required
def consertsInUserLocation(request):
    user = request.user
    if user.location:
        location = get_object_or_404(Location, name=user.location)
        ExistConserts = location.timeLocation.filter(
            set_status=['sales', 'start'])

        if ExistConserts:
            context = {
                "location": location,
                "timeConserts": ExistConserts,
            }

        else:
            messages.error(
                request, "doesn't exist any consert in your location")

    else:
        if request.method == "POST":
            consertsInUserLocationForm = ConsertsInUserLocationForm(
                request.GET)

            if consertsInUserLocation.is_valid():
                location = consertsInUserLocation.cleaned_data['location']
                user.location = location
                user.save()
                return redirect("ticketSales:consertsInUserLocation")

            else:
                messages.error(request, "please enter correct location")
                return redirect("ticketSales:consertsInUserLocation")
        else:
            consertsInUserLocationForm = ConsertsInUserLocationForm()
            context = {
                "consertsInUserLocationForm": consertsInUserLocationForm,
            }
    return render(request, 'ticketSales/consertsInUserLocation.html', context=context)
