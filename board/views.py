from django.shortcuts import render
from django.views.generic import ListView
from .models import Board


class BoardList(ListView):
    model = Board
    ordering = '-pk'
