# from urllib.parse import quote_plus
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Experiment
from .forms import AddNewForm


# Create your views here.

def list_view(request):
    query_set_list = Experiment.objects.all()

    paginator = Paginator(query_set_list, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        query_set = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        query_set = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        query_set = paginator.page(paginator.num_pages)

    context = {
        "object_list": query_set,
        "title": "Experiments",
    }

    return render(request, 'posts/experiment_list.html', context)


def detail_view(request, slug=None):
    instance = get_object_or_404(Experiment, slug=slug)
    # shareable_link = quote_plus(instance.content)
    query_set = {
        "title": instance.title,
        "instance": instance,
        # "shareable_link": shareable_link,
    }

    return render(request, 'posts/experiment_details.html', query_set)


def edit_post(request, slug=None):
    # admin authentication is need to be added

    instance = get_object_or_404(Experiment, slug=slug)
    form = AddNewForm(request.POST or None, request.FILES or None, instance=instance)

    query_set = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    return render(request, "posts/add_new.html", query_set)


def add_new(request):
    # admin authentication is need to be added

    form = AddNewForm()

    if request.method == "POST":
        form = AddNewForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse("posts:list_view"))

    query_set = {
        "title": "Add new post to the list",
        "form": form,
    }
    return render(request, "posts/add_new.html", query_set)


def delete_post(request, slug=None):
    instance = get_object_or_404(Experiment, slug=slug)
    instance.delete()

    return redirect("posts:list_view")
