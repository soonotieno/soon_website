from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Board


class BoardList(ListView):
    model = Board
    ordering = '-pk'


class BoardDetail(DetailView):
    model = Board
