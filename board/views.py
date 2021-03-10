from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Board


class BoardList(ListView):
    model = Board
    ordering = '-pk'


class BoardDetail(DetailView):
    model = Board


class BoardCreate(CreateView):
    model = Board
    fields = ['title', 'content', 'board_image', ]
