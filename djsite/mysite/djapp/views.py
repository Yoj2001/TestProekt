from django.shortcuts import render
from .models import *
from django.shortcuts import Http404, HttpResponseRedirect
from django.urls import reverse
from djapp import admin

admin.Question.objects.get(pk=1)

def index(request):
    a = {"Country": Question.objects.all()}
    return render(request, "djapp/index.html", a)


def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, "djapp/detail.html", {"question": question})


def vote(request, question_id):
    voted = Question.objects.get(pk=question_id)
    try:
        selected_choice = voted.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(
            request,
            "djapp/detail.html",
            {
                "question": voted,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse("my_dj:result", args=(question_id,)))


def result(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Http404:
        raise Http404
    return render(request, "djapp/result.html", {"question": question})
