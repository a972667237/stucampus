from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.views import generic

from stucampus.lecture.models import LectureMessage


def index(request):
    return render_to_response(
        'lecture/index.html',
        {'table': LectureMessage.get_messages_table()},
        )
